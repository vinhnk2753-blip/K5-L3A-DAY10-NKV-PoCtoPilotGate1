"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
"""
from . import helpers as H
from .tools import Verdict

_PII_KEYS = ("recipient_contact", "name", "phone", "street", "address", "recipient")


def _active_policy(ctx):
    """Lấy chính sách đang có hiệu lực theo ngày hệ thống `ctx.as_of`."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _valid_approval(ctx, approval_id: str | None, order_id: str, amount_vnd: int) -> bool:
    """Xác thực mã phê duyệt: đúng ticket, đúng đơn, trạng thái valid, còn hạn và đủ hạn mức."""
    if not approval_id:
        return False
    for a in ctx.tools.lookup_approvals(approval_id=approval_id):
        if (
            a.get("status") == "valid"
            and a.get("ticket_id") == ctx.ticket.get("ticket_id")
            and a.get("order_id") == order_id
            and (a.get("expires_at") or "") >= ctx.as_of
            and int(a.get("max_vnd", 0)) >= int(amount_vnd)
        ):
            return True
    return False


def _scrub_pii(text: str, order: dict | None) -> str:
    """Che SĐT, tên, địa chỉ người nhận khỏi chuỗi ghi chú gửi bên thứ ba."""
    if not text or not order:
        return text
    rc = order.get("recipient") or {}
    cleaned = text
    phone = H.digits(rc.get("phone", ""))
    if len(phone) >= 9:
        for variant in (rc.get("phone", ""), phone, phone[-9:]):
            if variant and variant in cleaned:
                cleaned = cleaned.replace(variant, "[REDACTED-PHONE]")
    for field, tag in (("name", "[REDACTED-NAME]"), ("street", "[REDACTED-ADDR]")):
        val = (rc.get(field) or "").strip()
        if len(val) >= 3 and val.lower() in cleaned.lower():
            idx = cleaned.lower().find(val.lower())
            while idx != -1:
                cleaned = cleaned[:idx] + tag + cleaned[idx + len(val):]
                idx = cleaned.lower().find(val.lower(), idx + len(tag))
    return cleaned


def _gate_issue_refund(ctx, action):
    """Cổng 1 & 2: chống hoàn trùng, đối chiếu quyền lợi từ DB/policy và kiểm duyệt vượt hạn mức."""
    order_id = action.get("order_id")
    order = ctx.tools.lookup_order(order_id)
    pol = _active_policy(ctx)
    if order is None or pol is None or order.get("customer_id") != ctx.ticket.get("customer_id"):
        ctx.log("refund_invalid_order_or_policy", order_id=order_id)
        return Verdict.escalate("đơn hàng, chủ đơn hoặc chính sách hiệu lực không hợp lệ")

    ticket_id = action.get("ticket_id")
    if (
        order.get("refund_status") == "REFUNDED"
        or ctx.tools.ledger_rows(ticket_id=ticket_id)
        or ctx.tools.ledger_rows(order_id=order_id)
    ):
        ctx.log("refund_duplicate_blocked", order_id=order_id, ticket_id=ticket_id)
        return Verdict.deny("đơn hàng hoặc ticket đã có giao dịch hoàn tiền trước đó")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    db_delay = H.db_delay_days(parcel, ctx.as_of)
    expected = H.entitlement_vnd(pol, order, db_delay, parcel.get("delay_cause"))
    if expected <= 0:
        ctx.log("refund_not_eligible_db", db_delay=db_delay, cause=parcel.get("delay_cause"))
        return Verdict.deny("không đủ điều kiện hoàn tiền theo tracking DB và chính sách hiệu lực")

    approval_id = action.get("approval_id")
    if expected > pol["auto_limit_vnd"]:
        if not _valid_approval(ctx, approval_id, order_id, expected):
            ctx.log("refund_invalid_approval", approval_id=approval_id, expected=expected)
            return Verdict.escalate("khoản hoàn vượt hạn mức tự động thiếu mã phê duyệt hợp lệ")
    else:
        cust_cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
        if cust_cap is not None and not approval_id:
            cust_today = sum(
                r["amount_vnd"]
                for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                if not r.get("approval_id") and not str(r.get("ticket_id", "")).startswith("T-OLD-")
            )
            if cust_today + expected > cust_cap:
                ctx.log("refund_customer_daily_cap", cust_today=cust_today, expected=expected, cap=cust_cap)
                return Verdict.escalate("tổng hoàn tự động cho khách trong ngày vượt ngưỡng Ops")

    if (
        int(action.get("amount_vnd", 0)) != expected
        or action.get("payer", "LOGIX") != "LOGIX"
        or action.get("basis") == "fail_open"
    ):
        ctx.log(
            "refund_aligned_to_db",
            proposed=action.get("amount_vnd"),
            expected=expected,
            proposed_payer=action.get("payer"),
        )
        return Verdict.modify(
            "điều chỉnh số tiền và người trả đúng theo tracking DB và chính sách hiệu lực",
            amount_vnd=expected,
            payer="LOGIX",
            basis="policy",
        )
    return Verdict.allow()


def _gate_carrier_fault(ctx, action):
    """Cổng 3a: chỉ ghi lỗi hãng khi đúng kiện trễ và có nguyên nhân hợp lệ theo tracking DB."""
    order = ctx.tools.lookup_order(action.get("order_id"))
    pol = _active_policy(ctx)
    if order is None or pol is None:
        ctx.log("fault_missing_order_or_policy")
        return Verdict.deny("không tìm thấy đơn hoặc chính sách để đối chiếu lỗi hãng")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    db_delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(pol, parcel, db_delay):
        ctx.log("fault_no_db_basis", parcel_id=parcel["parcel_id"], cause=parcel.get("delay_cause"), db_delay=db_delay)
        return Verdict.deny("không có nguyên nhân lỗi hãng hợp lệ theo tracking DB")

    if (
        action.get("parcel_id") != parcel["parcel_id"]
        or action.get("carrier_id") != parcel["carrier_id"]
        or int(action.get("delay_days", -1)) != db_delay
    ):
        ctx.log("fault_aligned_to_db", parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"], db_delay=db_delay)
        return Verdict.modify(
            "đối chiếu đúng kiện hàng, hãng vận chuyển và số ngày trễ từ tracking DB",
            parcel_id=parcel["parcel_id"],
            carrier_id=parcel["carrier_id"],
            driver_id=parcel.get("driver_id"),
            delay_days=db_delay,
        )
    return Verdict.allow()


def _gate_notify_carrier(ctx, action):
    """Cổng 3b: chặn rò rỉ dữ liệu cá nhân người nhận trong thông báo gửi hãng vận chuyển."""
    payload = dict(action.get("payload") or {})
    order_id = payload.get("order_id") or ctx.ticket.get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    changed = False
    clean = {}
    for k, v in payload.items():
        if k in _PII_KEYS:
            changed = True
            continue
        if k == "customer_note" and isinstance(v, str):
            scrubbed = _scrub_pii(v, order)
            if scrubbed != v:
                changed = True
            clean[k] = scrubbed
        else:
            clean[k] = v
    if changed:
        ctx.log("pii_scrubbed_carrier_notice", order_id=order_id)
        return Verdict.modify("loại bỏ thông tin cá nhân người nhận khỏi thông báo hãng", payload=clean)
    return Verdict.allow()


def pre_guard(ctx):
    """Ghim đúng phiên bản chính sách hiệu lực tại `ctx.as_of` trước khi trợ lý đọc ticket."""
    pol = _active_policy(ctx)
    if pol is not None:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_issue_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_carrier_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify_carrier(ctx, action)
    return Verdict.allow()
