"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def llm_fallback_rate(trials):
    """Tỉ lệ lần chạy gặp sự cố LLM phải rơi vào nhánh fallback (429 fail_open hoặc degraded)."""
    hits = sum(
        any(e.get("type") == "llm_fallback" for e in t.get("events", []))
        for t in trials
    )
    return hits / max(1, len(trials))


def peak_hour_queue_load(trials):
    """Số ca vào hàng chờ người duyệt tối đa trong một cửa sổ trượt 60 phút của một ngày giả lập."""
    by_day_seed = {}
    for t in trials:
        if t.get("review_kind") is not None and t.get("arrive_min") is not None:
            key = (t.get("day"), t.get("seed"))
            by_day_seed.setdefault(key, []).append(float(t["arrive_min"]))
    peak = 0
    for times in by_day_seed.values():
        times.sort()
        lo = 0
        for hi, t_hi in enumerate(times):
            while t_hi - times[lo] > 60.0:
                lo += 1
            peak = max(peak, hi - lo + 1)
    return float(peak)


def auto_refund_day_max_vnd(trials):
    """Tổng tiền hoàn tự động (không qua approval_id) lớn nhất trong một ngày giả lập (đồng)."""
    by_day_seed = {}
    for t in trials:
        key = (t.get("day"), t.get("seed"))
        amt = sum(r.get("amount_vnd", 0) for r in t.get("ledger", []) if not r.get("approval_id"))
        by_day_seed[key] = by_day_seed.get(key, 0) + amt
    return float(max(by_day_seed.values(), default=0))


def model_override_rate(trials):
    """Tỉ lệ lần chạy mà LLM lấy số ngày khách tự khai đè lên tracking DB (lỗi chìm)."""
    hits = sum(
        any(e.get("type") == "model_override" for e in t.get("events", []))
        for t in trials
    )
    return hits / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "llm_fallback_rate": llm_fallback_rate,
    "peak_hour_queue_load": peak_hour_queue_load,
    "auto_refund_day_max_vnd": auto_refund_day_max_vnd,
    "model_override_rate": model_override_rate,
}
STARTER_MONITORS = ("escalation_rate",)
