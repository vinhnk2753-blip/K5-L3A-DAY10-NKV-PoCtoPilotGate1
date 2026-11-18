# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** `NKV (K5-L3A-DAY10-NKV-PoCtoPilotGate1)` · **Thẻ đã bốc:** `S4`

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S4-prepared-20261118-201721-e59e38` | `S4 · prepared` | nhận thẻ `S4`, chưa sửa thêm (chỉ có cổng vòng 1 đã chốt) | `1.0 ([1.0, 1.0])` | `1.0` | `0đ · 0 · 0` | `0.3659` | Cổng vòng 1 chặn sạch 100% lỗi kỹ thuật (`160k` hoàn sai & `27` lỗi oan về `0`), nhưng còn vượt trần `5 ca ùn` (`82.0 phút`) và tổng hoàn tự động `422.000đ > 300.000đ`. |
| 2 | `R-S4-after-20261118-201827-0ba81f` | `S4 · after` | đổi MỘT thứ: hạ `daily_refund_cap_vnd=300000` & kiểm tra ngân sách Finance trong `guards.py` | `1.0 ([1.0, 1.0])` | `1.0` | `0đ · 0 · 0` | `0.5122` | Chặn được vượt ngân sách sale (`292.000đ <= 300.000đ`), nhưng vì thêm ca chuyển người nên hàng chờ tăng lên `6 ca ùn` (`86.0 phút`). |
| 3 | `R-S4-after-20261118-201840-732d71` | `S4 · after` | đổi MỘT thứ: tăng `reviewers_on_shift=2` & `review_capacity_per_hour=null` (`12 ca/giờ`) | `1.0 ([1.0, 1.0])` | `1.0` | `0đ · 0 · 0` | `0.5122` | Hết sạch ùn tắc (`0 ca ùn`, chờ tối đa `15.0 phút`), chi phí `7.296đ/ticket <= 8.000đ`, `ROI = 0.37 >= 0.25`, `vượt trần: không`. |
| 4 | `R-S4-after-20261118-201917-217918` | `S4 · after` | đổi MỘT thứ: thêm 4 chỉ số monitor vào `lab10/monitors.py` & cập nhật `stop_conditions` | `1.0 ([1.0, 1.0])` | `1.0` | `0đ · 0 · 0` | `0.5122` | Toàn bộ 4 monitor mới sáng đèn phân biệt `S4` với `base`, không vượt trần nào, `PASS-VISIBLE`. |
| 5 | `R-base-after-20261118-201918-217918` | `base · after` | `(kiểm lại bộ nền sau khi sửa vòng 2 cho S4)` | `1.0 ([1.0, 1.0])` | `1.0` | `0đ · 0 · 0` | `0.2273` | Không regression (`110/110`), bộ nền ngày thường đạt `5.820đ/ticket <= 8.000đ`, `ROI = 0.72 >= 0.25`, `0 ca ùn`. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident S4
```

- Mã lần chạy grade: `R-S4-grade-20261118-201721-e59e38` · base: `R-S4-before-20261118-201721-e59e38` · prepared: `R-S4-prepared-20261118-201721-e59e38`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared):
  - `pass_rate` tăng từ **`0.8683` → `1.0`** (`+0.1317`); `pass_k` tăng từ **`0.6829` → `1.0`** (`+0.3171`).
  - `wrongful_refund_vnd` giảm từ **`160.000đ` → `0đ`** (hoàn sai ngày tệ nhất `44.000đ → 0đ`).
  - `wrongful_carrier_faults` giảm từ **`27` lỗi → `0` lỗi**.
  - Nguyên nhân: `_gate_issue_refund` và `_gate_carrier_fault` ở Vòng 1 đã chặn toàn bộ nhánh `fail_open` khi LLM bị HTTP `429`, không cho hoàn tiền khi chưa đủ ngày trễ (`S4-05`) và không cho phạt oan hãng khi `delay_cause` là `MERCHANT_HANDOVER` (`S4-02`, `S4-08`) hoặc `CUSTOMER_ABSENT` (`S4-11`).
- Khối kinh doanh và vận hành còn dòng nào vượt trần:
  1. `hàng chờ: 5 ca bị ùn (chờ quá 60 phút hoặc hết ca chưa tới lượt)` — chờ lâu nhất `82.0 phút > mức bàn đặt 60 phút` (với `1` người trực `6 ca/giờ`, cộng thêm 10% kiểm mẫu khiến số ca ùn tăng từ `4` lên `5`).
  2. `tổng hoàn tự động một ngày 422.000đ > ngân sách 300.000đ` (vì Vòng 1 đặt `daily_refund_cap_vnd = 1.500.000đ` theo ngày thường `2.000.000đ`, chưa theo trần đặc biệt `300.000đ` của Finance ngày 11.11 trong `incidents/S4/world_patch.json`).
  3. Mục `6 monitor` còn ❌ vì chưa thêm chỉ số theo dõi mới trong `lab10/monitors.py`.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** *(Phần riêng thẻ S4)*

- **[Bút khác màu] Sự cố trên thẻ thuộc lăng kính nào?** Thuộc **cả 3 lăng kính cùng lúc**: (1) **Kỹ thuật** (LLM trả HTTP `429` 60% ở `policy_check` làm `agent.py` rơi vào `fail_open`), (2) **Con người và vận hành** (lượng ticket giờ cao điểm 20h tăng gấp 3 với 36,6% ca `DAMAGED`/`NOT_RECEIVED` đẩy dồn vào 1 người trực duy nhất `NV-HANH`, gây ùn quá 60 phút), và (3) **Kinh doanh** (Finance hạ trần hoàn tự động riêng ngày sale xuống `300.000đ`, trong khi config Vòng 1 vẫn để `1.500.000đ`).
- **[Bút khác màu] Có nằm trong các lý do bàn đã viết không?** Có **một phần**: ở Phiếu B mục B6 dòng 1 (Kỹ thuật: *"fallback mù khi LLM lỗi 429"*), cổng Vòng 1 đã chặn **100%** lỗi hoàn sai và phạt oan hãng (`160.000đ → 0đ`, `27 → 0`). Ở dòng 3 (Con người/vận hành) & mục B7.6, bàn có dự báo giờ cao điểm tăng gấp 3 nhưng mới chỉ viết ở Runbook giấy chứ **chưa tăng sẵn `reviewers_on_shift` lên 2** cho ngày sale. Còn phần **ngân sách ngày sale bị Finance siết xuống còn `300.000đ` (thấp hơn 6,6 lần ngày thường)** và **tỉ lệ ticket `DAMAGED`/`NOT_RECEIVED` tăng đột biến lên 36,6% dồn trong 1 giờ** là điểm bàn chưa lường hết ở Vòng 1.
- **[Bút khác màu] Lý do còn thiếu, thêm bây giờ:**

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Ngày sale 11.11, Finance hạ trần hoàn tự động ngày xuống `300.000đ` (chỉ bằng 15% ngày thường) nhưng config Vòng 1 vẫn giữ `daily_refund_cap_vnd = 1.500.000đ` và `guards.py` chưa đọc động `ops_limits()["daily_auto_refund_budget_vnd"]`, nên trợ lý chi lố `422.000đ` tự động không qua người duyệt. | Kinh doanh | `incidents/S4/world_patch.json` (`ops_limits.daily_auto_refund_budget_vnd = 300000`), `config/operating_gates.round1.json`, báo cáo `lab10.grade` (`tổng hoàn tự động một ngày 422000đ`). |
| Ca trực đêm 11.11 chỉ bố trí `1` người (`6 ca/giờ`), trong khi `36,6%` ticket giờ 20h là hàng vỡ/thất lạc (`DAMAGED`/`NOT_RECEIVED`) cộng ca kiểm mẫu khiến hàng chờ đạt `16 ca/giờ`, dồn ùn `5 ca` chờ tới `82.0 phút`. | Con người và vận hành | `incidents/S4/tickets.jsonl` (`arrive_min` `240–298`), `config/operating_gates.json` (`reviewers_on_shift = 1`), báo cáo `lab10.grade` (`số ca bị ùn = 5`, `wait_max_min = 82.0`). |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

```bash
python3 -m lab10.trace --suite S4 --ticket S4-08 --seed 11
python3 -m lab10.trace --suite S4 --ticket S4-05 --seed 11
python3 -m lab10.trace --suite S4 --ticket S4-07 --seed 11
```

**Tác hại của thẻ:** cho ai `Finance/LogiX, các hãng vận chuyển (VNX, MKD, DNB, GHSH, LGX), khách hàng chờ duyệt & trưởng ca CSKH (NV-HANH)` · đo bằng gì `wrongful_refund_vnd, wrongful_carrier_faults, auto_refund_day_max_vnd vs ngân sách 300.000đ, queue_stuck & wait_max_min` · bao nhiêu ở mốc base `160.000đ hoàn sai (44.000đ/ngày tệ nhất), 27 lỗi hãng oan, tổng hoàn tự động 466.000đ > 300.000đ, 4 ca bị ùn (wait_max 78.0 phút) và pass_rate = 0.8683 (prepared còn 5 ca ùn 82.0 phút & 422.000đ > 300.000đ)`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S4-08@11` (ở mốc `base`): `04/05 llm_error 429` → `06 llm_fallback {"purpose": "policy_check", "mode": "fail_open"}` → `07 proposal {"amount_vnd": 24000, "basis": "fail_open", "do_fault": true}` → `09 tool file_carrier_fault {"carrier_id": "VNX"}` dù `02 tracking` ghi `cause: "MERCHANT_HANDOVER"` (shop xuất kho trễ, `NHÃN faults: []`). *(Trong khi `S4-08@22` chỉ lỗi 1 lần 429 nên lại ĐẠT.)* | Khách không thấy lỗi; **hãng VNX (bên thứ ba)** gánh oan 1 strike (`100.000đ`) và **chị Oanh (`NV-OANH`)** lệch sổ đối soát shop–hãng. | cao | **Lỗi chìm** *(cả khách lẫn trợ lý đều tưởng giao dịch xong bình thường, chỉ bên thứ ba bị phạt oan).* |
| 2 | `S4-05@11` (ở mốc `base`): `02 tracking {"db_delay_days": 1, "cause": "CARRIER"}` → `06 llm_fallback {"mode": "fail_open"}` → `08 tool issue_refund {"amount_vnd": 18000}` & `09 tool file_carrier_fault {"carrier_id": "MKD", "delay_days": 1}` dù `NHÃN` là `denied, 0đ, faults: []`. | **LogiX/Finance** mất oan `18.000đ` (góp phần đẩy tổng hoàn tự động ngày 11.11 lên `466.000đ > 300.000đ`) và **hãng MKD** bị phạt oan `120.000đ`/strike. | cao | **Lỗi chìm** *(khách nhận tiền vui vẻ nên không báo, công ty mất tiền và đối tác chịu phạt sai quy chế).* |
| 3 | `S4-07@11..S4-33` dồn `15` ca `DAMAGED`/`NOT_RECEIVED` lúc `arrive_min: 240..298` (`R-S4-prepared-20261118-201721-e59e38`), kết hợp kiểm mẫu 10% & `1` người trực `6 ca/giờ`: hàng chờ lên `wait_max_min = 82.0 phút`, **`5 ca bị ùn > 60 phút`** và tổng hoàn ngày lên `422.000đ > 300.000đ`. | **Khách hàng** bị trễ SLA 60 phút, **chị Hạnh (`NV-HANH`)** bị quá tải hàng chờ, và **Finance** bị chi vượt trần `300.000đ`. | cao | **Giới hạn của hệ thống & Lỗi ngữ cảnh** *(năng lực 1 người trực giới hạn cứng ở 6 ca/giờ; ngoài ra thiết kế v1 mặc định trần ngày thường `1.500.000đ` không khớp bối cảnh ngày sale `300.000đ`).* |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 (`S4-08@11`) | Lỗi 2 (`S4-05@11`) | Lỗi 3 (Hàng chờ & ngân sách `S4`) |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Không (lỗi nằm ở nhánh `fail_open` khi gọi LLM `policy_check`). | Không | Không (nội dung ticket hợp lệ; dồn lưu lượng gấp 3). |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | **X** *(dữ liệu `cause: MERCHANT_HANDOVER` đã có ở bước 02 nhưng nhánh `fail_open` bỏ qua không đọc; kết quả chập chờn theo seed vì 429 có xác suất 60%).* | **X** *(đã có `db_delay_days = 1` nhưng `fail_open` bỏ qua chính sách `min_days_fee = 3`).* | **X** *(config Vòng 1 thiếu đọc `ops_limits.daily_auto_refund_budget_vnd` của ngày 11.11 trong `world_patch.json`).* |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | Không | Không | **X** *(Finance chốt trần `300.000đ` riêng ngày 11.11 nhưng cổng config của trợ lý vẫn giữ `1.500.000đ`, không đồng bộ trần giữa Finance và trợ lý).* |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | **X** *(2 lần 429 liên tiếp ở `policy_check` kích hoạt fallback `fail_open`).* | **X** *(2 lần 429 liên tiếp kích hoạt `fail_open`).* | **X** *(15 ca `DAMAGED`/`NOT_RECEIVED` + recheck + ca vượt trần dồn vào 1 người trực `6 ca/giờ` làm hàng chờ sập SLA 60 phút).* |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 (`S4-08@11`) | Lỗi 2 (`S4-05@11`) | Lỗi 3 (Hàng chờ & ngân sách `S4`) |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Hãng VNX bị trừ phạt oan vì đơn do shop giao muộn, còn chị Oanh phải xử lý khiếu nại đối soát từ hãng. | Finance mất tiền hoàn cho đơn mới trễ 1 ngày (chưa tới hạn 3 ngày), hãng MKD bị ghi lỗi oan. | Khách hàng phải đợi `82 phút > SLA 60 phút`, `NV-HANH` ngập việc một mình, Finance bị chi hoàn tự động vượt mức `300.000đ`. |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | **Khác (cổng chặn cấp hệ thống ngoài model)**: `write_gate` cho `file_carrier_fault` đối chiếu `H.carrier_at_fault` từ tracking DB (đã chặn sạch ở Vòng 1). | **Khác (cổng chặn cấp hệ thống ngoài model)**: `write_gate` cho `issue_refund` tính `H.entitlement_vnd` từ DB & chính sách hiệu lực, bỏ qua kết quả `fail_open` (từ chối trả về `denied` trung thực). | **Trao quyền kiểm soát cho người + cấu hình vận hành**: đọc động `daily_auto_refund_budget_vnd` trong `guards.py` + đặt `daily_refund_cap_vnd = 300000` để phần vượt chuyển `NV-HANH` duyệt; tăng `reviewers_on_shift = 2` (`12 ca/giờ`). |
| Đường đi của người sau khi có giải pháp | `S4-08@11`: `write_gate` cho phép hoàn `24.000đ` hợp lệ (`MERCHANT_HANDOVER` vẫn được hoàn phí ship theo `REFUND-v3`) và chặn lệnh `file_carrier_fault` → `0` lỗi oan hãng. | `S4-05@11`: `write_gate` chặn `issue_refund` → trợ lý trả lời từ chối rõ ràng (`denied`, `0đ`), không ghi sổ cái và không phạt `MKD`. | Các ca vượt trần `300.000đ` hoặc hàng vỡ chuyển sang hàng chờ có `2` người duyệt trực (`12 ca/giờ`) → tất cả được duyệt trong `≤ 15 phút` (`0 ca ùn`), chi phí `7.296đ/ticket`. |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `llm_fallback_rate` (tỉ lệ ca rơi vào nhánh `llm_fallback`, sáng đèn `0.0 → 0.185366` trên `S4`) và sự kiện `guard: llm_fallback_guarded`. | `llm_fallback_rate` + `auto_refund_day_max_vnd` (giữ hoàn tự động ngày ở `292.000đ ≤ 300.000đ`). | `peak_hour_queue_load` (`1.0 → 16.0` ca/giờ cao điểm) và `auto_refund_day_max_vnd` (`155.000đ → 466.000đ` ở `base` / `292.000đ` ở `after`). |

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

*Thẻ **S4**: Theo bảng phân công C3, phần riêng của thẻ S4 là **Mục C1 (mở lại pre-mortem bằng bút khác màu)** và **Mục Giờ cao điểm ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu)** — cả hai đã được điền đầy đủ. Các mục `C3.1–C3.5` dưới đây thuộc về các thẻ khác nên giữ nguyên trống theo quy định.*

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

*(Không áp dụng cho thẻ S4.)*

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

*(Không áp dụng cho thẻ S4.)*

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

*(Không áp dụng cho thẻ S4.)*

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

*(Không áp dụng cho thẻ S4.)*

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

*(Không áp dụng cho thẻ S4.)*

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund` & luồng vận hành `review_queue` (ngày sale 11.11)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `llm.policy_check` → `amount_vnd`, `do_fault` | **INCAPABLE** | Giờ cao điểm `rate_pct = 60%` HTTP `429` (`incidents/S4/world_patch.json -> llm_faults`): `S4-05@11`, `S4-08@11` lỗi 429 cả 2 lần retry nên rơi vào `fail_open`, tự hoàn tiền dù trễ 1 ngày và phạt oan `MKD`/`VNX`. | LogiX mất `160.000đ` hoàn sai; hãng gánh oan `27` strike; chị Oanh sai sổ đối soát. | Ở mốc `base`: chưa có. Ở mốc `prepared`: `guards.py` Vòng 1 đã tính lại DB nên đã chặn sạch. | Bổ sung log `llm_fallback_guarded` + metric `llm_fallback_rate` trong `monitors.py` (**tầng phát hiện + tầng chặn**). |
| `daily_refund_cap_vnd` vs `ops_limits.daily_auto_refund_budget_vnd` | **WRONG** | Ngày 11.11 Finance chốt `daily_auto_refund_budget_vnd = 300000`, nhưng `config/operating_gates.json` Vòng 1 vẫn giữ `1500000` → từ `S4-36` đến `S4-41` tổng hoàn tự động vọt lên `422.000đ > 300.000đ` ở mốc `prepared`. | Vượt trần ngân sách Finance `122.000đ` không qua người duyệt (`NV-HANH`). | Ở mốc `prepared`: chưa có (`tools.py` chỉ đọc `daily_refund_cap_vnd` trong config). | `guards.py` kiểm trực tiếp `ops_limits()["daily_auto_refund_budget_vnd"]` + sửa `daily_refund_cap_vnd = 300000` + monitor `auto_refund_day_max_vnd` (**tầng giới hạn thiệt hại + phát hiện**). |
| `review_queue` (`reviewers_on_shift`, `arrive_min`) | **INCAPABLE** | Khung 20h (`arrive_min: 240–298`) dồn `15` ca `DAMAGED`/`NOT_RECEIVED` (`S4-07..S4-33`) + kiểm mẫu 10% + ca vượt trần 300k (`~16–22 ca/ngày`), trong khi `reviewers_on_shift = 1` chỉ duyệt được `6 ca/giờ`. | `5–6 ca bị ùn` (`wait_max_min = 82.0–86.0 phút > 60 phút`), khách chờ lâu, `NV-HANH` quá tải. | Ở mốc `prepared`: chưa có (chỉ ghi trên Runbook giấy). | Tăng `reviewers_on_shift = 2`, đặt `review_capacity_per_hour = null` (`12 ca/giờ`) + monitor `peak_hour_queue_load` (**tầng vận hành + phát hiện**). |
| `llm.extract` khi HTTP 429 lan rộng sang bước đọc ticket | **INCAPABLE** | *(Nhánh chưa thấy trên trace S4 vì `llm_faults.purposes` mới chỉ có `["policy_check"]`)*: Nếu nhà cung cấp LLM nghẽn 429 cả ở `extract` và rơi về degraded parse, các câu chữ lạ về hàng vỡ/móp dễ bị hiểu nhầm thành `LATE` hoặc `OTHER` thay vì `DAMAGED`. | Trợ lý tự trả lời/hoàn tiền sai thay vì chuyển người cho ca hàng vỡ (`S4-07`). | `agent.py:92` fallback sang `MockLLM().extract(..., seed=1)` không có guard riêng theo từ khóa vỡ/hỏng nếu parser bỏ sót. | Đưa vào Risk register + dùng `peak_hour_queue_load` và kiểm mẫu 10% (`review_sampling_pct`) để phát hiện sớm (**tầng phát hiện / vận hành**). |

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report:
**(1) Khi LLM lỗi (`llm_fallback`), mọi khoản hoàn tiền và lỗi hãng vẫn phải tuân thủ tuyệt đối tracking DB & chính sách hiệu lực (`wrongful_refund_vnd == 0` và `wrongful_carrier_faults == 0`), và tổng hoàn tự động trong ngày không bao giờ vượt `min(daily_refund_cap_vnd, ops_limits.daily_auto_refund_budget_vnd)` (`300.000đ` ngày 11.11); (2) Công suất ca duyệt phải đảm bảo `queue_stuck == 0` và `wait_max_min <= 60` phút trong giờ cao điểm với `cost_per_ticket_vnd <= 8.000đ` và `ROI >= 0.25`.**

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào):
Kiểm bằng `_gate_issue_refund` & `_gate_carrier_fault` trong `lab10/guards.py` (check `ops_limits()["daily_auto_refund_budget_vnd"]`, `H.entitlement_vnd`, `H.carrier_at_fault`), tham số `business.daily_refund_cap_vnd` và `operations.reviewers_on_shift` trong `config/operating_gates.json`, các dòng `tổng hoàn tự động một ngày`, `số ca bị ùn`, `thời gian chờ lâu nhất`, `chi phí mỗi ticket`, `ROI` trong report `lab10.grade` và 4 hàm monitor trong `lab10/monitors.py`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm):
Người thiết kế đã ngầm giả định rằng **tải ticket mỗi giờ phân bố tương đối đều quanh mức ngày thường (`~22 ticket/ngày`, `~3 ticket/giờ`), tỉ lệ ca cần chuyển người ổn định (~`23%`), ngân sách hoàn tự động ngày của Finance luôn cố định (`2.000.000đ`), và API nhà cung cấp LLM hiếm khi lỗi liên tiếp nhiều lần**.

Vì sao có thể sai:
Trong thực tế thương mại điện tử (như đêm sale 11.11/12.12 hoặc sau sự cố thời tiết), lượng ticket có thể tăng gấp 3 lần chỉ trong 1 giờ vàng (`20h–21h`) do hiệu ứng flash sale; đồng thời các sự kiện ngoại cảnh như khâu đóng gói quá tải làm tỉ lệ hàng vỡ/thất lạc tăng vọt lên `> 35%` đẩy hàng chờ tăng theo cấp số nhân, đúng lúc nhà cung cấp LLM dùng chung toàn thị trường cũng bị quá tải trả `429`, còn Finance lại siết đột ngột ngân sách khuyến mãi/hoàn tiền ngày sale xuống `300.000đ` để chặn lỗ.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S4-before-20261118-201721-e59e38` / `R-S4-prepared-20261118-201721-e59e38`)

```
[ĐỈNH] Tác hại đêm 11.11: Finance vượt ngân sách 300k, hàng chờ sập SLA > 60p, hãng bị phạt oan & hoàn sai
       (cho ai: Finance/LogiX, hãng vận chuyển, khách hàng, NV-HANH · đo bằng: 160k hoàn sai, 27 lỗi oan ở base; 422k/300k & 5 ca ùn 82p ở prepared)
 └─ HOẶC
 ├─ [1] Hoàn tiền sai & ghi oan lỗi hãng khi LLM nghẽn 429                    tầng: kỹ thuật (chính sách / hành động)
 │ └─ vì: 60% policy_check bị 429 liên tiếp 2 lần kích hoạt nhánh fail_open    bằng chứng: ticket S4-05@11, S4-08@11 (`mode: fail_open`, `27` lỗi oan, `160.000đ` hoàn sai ở base)
 ├─ [2] Tổng hoàn tự động ngày 11.11 vượt trần ngân sách 300.000đ của Finance   tầng: kinh doanh / cấu hình
 │ └─ vì: daily_refund_cap_vnd để 1.500.000đ (theo ngày thường) & không đọc    bằng chứng: `incidents/S4/world_patch.json` (`daily_auto_refund_budget_vnd: 300000`), report `prepared`: `422.000đ > 300.000đ`
 │        động `ops_limits.daily_auto_refund_budget_vnd` (`300.000đ`)
 └─ [3] Hàng chờ duyệt ngập quá SLA 60 phút trong giờ cao điểm 20h             tầng: con người và vận hành
   └─ vì: 15 ca DAMAGED/NOT_RECEIVED + recheck 10% dồn trong 1h (`arrive_min`    bằng chứng: `S4-07..S4-33`, report `base`: `4 ca ùn (78.0p)`, `prepared`: `5 ca ùn (82.0p)`, `reviewers_on_shift = 1` (`6 ca/giờ`)
          `240..298`) vượt công suất 1 người trực `6 ca/giờ`
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Khi `llm.policy_check` gặp lỗi/fallback (`fail_open`), hệ thống không được tự hoàn tiền hoặc ghi lỗi hãng trái với `H.entitlement_vnd` và `H.carrier_at_fault` tính từ tracking DB (`wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`). | Nhà cung cấp LLM luôn trả lời ổn định ở mọi khung giờ; phương án fallback mặc định hoàn phí + phạt hãng luôn an toàn khi model nghẽn. |
| [2] | Mọi lệnh `issue_refund` tự động không có `approval_id` phải bị chặn chuyển người duyệt ngay khi tổng hoàn trong ngày sắp vượt `min(daily_refund_cap_vnd, ops_limits.daily_auto_refund_budget_vnd)`. | Ngân sách hoàn tự động ngày của Finance cố định ở mức `2.000.000đ/ngày` và không thay đổi đột ngột theo chiến dịch sale. |
| [3] | Công suất duyệt người trực mỗi giờ phải lớn hơn hoặc tương xứng mật độ ca chuyển người giờ cao điểm để `queue_stuck == 0` và `wait_max_min <= 60` phút (vẫn giữ `cost_per_ticket_vnd <= 8.000đ`). | Ticket chuyển người đến rải đều trong ca 8 giờ và tỉ lệ hàng vỡ/thất lạc không tăng vọt trong 1 giờ cao điểm sale. |

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

```bash
python3 -m lab10.eval --suite S4 --stage after --note "vòng 2 bước 3: thêm 4 monitor mới và cập nhật stop_conditions"
python3 -m lab10.grade --incident S4
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | LLM gặp 429 kích hoạt nhánh `fail_open` hoàn sai & phạt oan hãng (`S4-05@11`, `S4-08@11`). | **Vòng 1 đã giữ nguyên + Vòng 2 bổ sung:** `lab10/guards.py` (`_gate_issue_refund`, `_gate_carrier_fault`) tính lại từ DB & policy hiệu lực + log `llm_fallback_guarded`; `lab10/monitors.py` (`llm_fallback_rate`). | Chặn + Phát hiện | **NGĂN hẳn** tác hại hoàn sai/phạt oan từ `fail_open` trên mọi dữ kiện có trong tracking DB (`160k → 0`, `27 → 0`), vì `write_gate` luôn bỏ qua kết quả `fail_open` và đối chiếu trực tiếp DB; vẫn còn hở nếu bản thân tracking DB nhập sai. | `R-S4-after-20261118-201917-217918` (`R-S4-grade-20261118-201926-217918`) |
| [2] | Vượt ngân sách hoàn tự động ngày sale `300.000đ` của Finance (`prepared`: `422.000đ`). | `config/operating_gates.json` (`business.daily_refund_cap_vnd: 1500000 -> 300000`) + `lab10/guards.py` (`_gate_issue_refund` kiểm tra động `ops_limits()["daily_auto_refund_budget_vnd"]` và `Verdict.escalate` khi sắp vượt) + `lab10/monitors.py` (`auto_refund_day_max_vnd`). | Giới hạn thiệt hại + Chặn + Phát hiện | **NGĂN hẳn** tổng hoàn tự động vượt trần `300.000đ` (`422.000đ → 292.000đ <= 300.000đ`), vì cả `write_gate` lẫn host `tools.py` đều chặn và chuyển người duyệt trước khi ghi sổ cái. | `R-S4-after-20261118-201827-0ba81f` → `R-S4-after-20261118-201917-217918` |
| [3] | Hàng chờ ngập `5–6 ca ùn` (`82–86 phút`) vì 1 người trực `6 ca/giờ` không gánh nổi đợt 20h (`16 ca/giờ`). | `config/operating_gates.json` (`operations.reviewers_on_shift: 1 -> 2`, `review_capacity_per_hour: 6 -> null` thành `12 ca/giờ`, giữ `decision_note: true` và `review_sampling_pct: 10`, cập nhật `stop_conditions`) + `lab10/monitors.py` (`peak_hour_queue_load`). | Vận hành + Phát hiện | **GIẢM khả năng** (chỉ ngăn được trong ngưỡng bão hiện tại ~`16 ca/giờ` đưa `stuck: 5/6 → 0`, `wait_max: 86p → 15.0p`); nếu lượng ca tăng gấp đôi nữa (`> 25–30 ca/giờ`) thì `2` người trực vẫn sẽ ùn trở lại vì thêm người thứ 3 làm chi phí vượt `8.000đ/ticket`. | `R-S4-after-20261118-201840-732d71` → `R-S4-after-20261118-201917-217918` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Đã thêm 4 chỉ số mới vào `lab10/monitors.py` (`MONITORS`), đều tính không cần nhãn đúng/sai và đều **"sáng đèn"** phân biệt rõ giữa bộ nền (`base`) và thẻ sự cố (`S4`):

| | Chỉ số theo dõi mới 1 (Kỹ thuật: `llm_fallback_rate`) | Chỉ số theo dõi mới 2 (Vận hành: `peak_hour_queue_load`) | Chỉ số theo dõi mới 3 (Kinh doanh: `auto_refund_day_max_vnd`) |
|---|---|---|---|
| **Tên trong `MONITORS`** | `llm_fallback_rate` *(cộng thêm `model_override_rate` bắt lỗi chìm `T-002@55` ở `base`)* | `peak_hour_queue_load` | `auto_refund_day_max_vnd` |
| **Bước / hành vi được đo** | Sự cố nhà cung cấp LLM làm trợ lý phải rơi vào nhánh `llm_fallback` (429 ở `policy_check` / `extract`). | Áp lực dồn ca cần người duyệt (escalate + recheck) trong 1 giờ cao điểm nhất của ca. | Tổng mức chi hoàn tiền tự động (không có `approval_id`) trong một ngày vận hành. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ phần trăm (số thập phân `0..1`) số lần chạy có ít nhất một sự kiện `llm_fallback` trên tổng số lần chạy. | Số ca tối đa (đơn vị: `ca/giờ`) đi vào hàng chờ người duyệt trong bất kỳ cửa sổ trượt `60 phút` nào của một ngày giả lập. | Số tiền hoàn tự động lớn nhất trong một ngày giả lập (đơn vị: `đồng`). |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `t["events"]` của mỗi trial trong `monitor_view(trials)` (kiểm tra `e.get("type") == "llm_fallback"`). *(Tương tự `model_override_rate` đọc `e.get("type") == "model_override"`.)* | `t["review_kind"]`, `t["arrive_min"]`, `t["day"]`, `t["seed"]` của mỗi trial. | `t["ledger"]` (`amount_vnd`, `approval_id`), `t["day"]`, `t["seed"]` của mỗi trial. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `số trial có event type == "llm_fallback" / max(1, len(trials))`. Trial không phát sinh sự kiện (escalate sớm trước khi gọi LLM) vẫn giữ trong mẫu số; `len(trials) == 0` trả về `0.0`. | Gom các trial có `review_kind is not None` và `arrive_min is not None` theo từng cặp `(day, seed)`, sắp xếp tăng dần theo `arrive_min`, dùng hai con trỏ tính số phần tử tối đa trong `[t_lo, t_lo + 60]`. Trial thiếu `arrive_min` bị loại khỏi cửa sổ giờ; nếu không có ca chờ nào trả `0.0`. | Gom các trial theo `(day, seed)`, cộng `r["amount_vnd"]` với mọi dòng `ledger` có `not r.get("approval_id")`, rồi lấy `max(...)` (trả `0.0` nếu rỗng). |
| **Khung thời gian / ngưỡng báo động** | Cửa sổ trượt **15 phút** trong ca: **VÀNG** nếu `> 0.05` (5%), **ĐỎ** nếu `> 0.15` (15%) hoặc kéo dài > 15 phút (khi `S4` thực tế là `0.185`). | Cửa sổ trượt **60 phút**: **VÀNG** nếu vượt `75%` công suất trực (`> 9 ca/giờ` với 2 người), **ĐỎ** nếu vượt công suất ca (`> 12 ca/giờ` với 2 người; trên `S4` là `16 ca/giờ` cảnh báo để kích hoạt Runbook giảm tải). | Tổng lũy kế **trong ngày (24h)**: **VÀNG** nếu chạm `80%` ngân sách ngày (`240.000đ` ngày sale), **ĐỎ** nếu chạm `100%` trần (`300.000đ`). |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không đo được lỗi LLM sai âm thầm khi API trả về HTTP 200 (vì vậy cần kèm `model_override_rate` và kiểm mẫu 10%). | Đo số ca đến trong 60 phút nhưng chưa phản ánh trực tiếp thời lượng thực từng ca nếu trộn ca escalate (10 phút) với ca recheck (4 phút) hoặc ca tới dồn vào cuối ca phút 460. | Không phân biệt được trong số tiền hoàn tự động hợp lệ có lẫn ca hoàn sai nhỏ hay không nếu chưa đối chiếu nhãn/sổ cái. |
| **Giá trị trên bộ nền · trên thẻ** (`report`) | `llm_fallback_rate`: `0.0` (base) · **`0.185366`** (S4) *(cộng `model_override_rate`: **`0.045455`** trên base · `0.0` trên S4)* | `peak_hour_queue_load`: `1.0` (base) · **`14.0`** (S4 before) / **`16.0`** (S4 after) | `auto_refund_day_max_vnd`: `155000.0` (base) · **`466000.0`** (S4 before) / **`292000.0`** (S4 after) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S4-after-20261118-201917-217918` / `R-S4-grade-20261118-201926-217918`)

```
[ĐỈNH] Tác hại đêm 11.11 (hoàn sai, phạt oan, vượt ngân sách 300k, hàng chờ sập SLA) -> ĐÃ XỬ LÝ VỀ 0 TRÊN S4 VISIBLE
 └─ HOẶC
 ├─ [1] (LLM 429 fail_open) VÀ [gate _gate_issue_refund + _gate_carrier_fault trong guards.py + monitor llm_fallback_rate hỏng]
 ├─ [2] (Chi vượt 300k/ngày) VÀ [gate daily_refund_cap_vnd=300000 + kiểm ops_limits Finance trong guards.py + monitor auto_refund_day_max_vnd hỏng]
 └─ [3] (Hàng chờ ngập 20h) VÀ [gate reviewers_on_shift=2 (12 ca/giờ) + decision_note=true + monitor peak_hour_queue_load hỏng]   (còn hở nếu tải > ~24 ca/giờ!)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `guards.py` (`_gate_issue_refund`, `_gate_carrier_fault` đối chiếu DB/policy + log `llm_fallback_guarded`) + `monitors.py` (`llm_fallback_rate`) | Chặn + Phát hiện | **Ngăn hẳn** lỗi hoàn sai & phạt oan từ `fail_open`, vì `write_gate` không tin kết quả fallback của LLM mà luôn tính lại từ DB. | Nếu lỗi 429 lan sang `llm.extract` làm phân loại nhầm intent hoặc tracking DB gốc bị nhập sai. |
| [2] | `operating_gates.json` (`business.daily_refund_cap_vnd = 300000`) + `guards.py` (check động `ops_limits()["daily_auto_refund_budget_vnd"]`) + `monitors.py` (`auto_refund_day_max_vnd`) | Giới hạn thiệt hại + Chặn + Phát hiện | **Ngăn hẳn** tổng hoàn tự động vượt trần Finance `300.000đ` (`292.000đ <= 300.000đ`), vì vượt là chuyển người duyệt ngay trước khi ghi sổ. | Khi nhiều ca vượt trần bị chuyển người sẽ đẩy thêm tải vào nhánh hàng chờ [3]. |
| [3] | `operating_gates.json` (`operations.reviewers_on_shift = 2`, `review_capacity_per_hour = null`, `decision_note = true`, `review_sampling_pct = 10`) + `monitors.py` (`peak_hour_queue_load`) | Vận hành + Phát hiện | **Giảm khả năng** (chỉ ngăn ùn ở mức bão hiện tại `16 ca/giờ` → chờ tối đa `15.0 phút`, `0 ca ùn`, chi phí `7.296đ/ticket`, `ROI = 0.37`). | Nếu lượng ticket tăng gấp 5–6 lần hoặc quá 50% là ca vỡ hàng khiến `peak_hour_queue_load > 24 ca/giờ`, `2` người trực vẫn sẽ bị ùn (cần kích hoạt Runbook thu hẹp `pilot_scope` vì thêm người thứ 3 sẽ đẩy chi phí `> 8.000đ`). |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Bão đơn giờ cao điểm vượt khả năng `2` người trực (`> 20 ca cần duyệt/giờ`) khiến chi phí thêm người thứ 3 vượt `8.000đ/ticket` hoặc hàng chờ lại vượt SLA 60 phút. | Trung bình (dịp flash sale lớn) | Cao (ùn ca > 60 phút hoặc lỗ ROI) | Trần Thị Hạnh (`NV-HANH`) | `peak_hour_queue_load > 16 ca/giờ` và `queue_wait_max_min > 45 phút` trong report / `monitors.py` | Kích hoạt Runbook thu hẹp `business.pilot_scope` xuống `50%` hoặc tách riêng kho ít hàng vỡ (`CT`, `HCM`), không nâng lên 3 người trực để giữ chi phí `≤ 8.000đ`. | Quyết định chuyển từ **Tiếp tục** sang **Thu hẹp** nếu lặp lại trên 2 ca sale liên tiếp. | MANAGE |
| Sự cố HTTP 429 từ LLM lan từ `policy_check` sang bước `extract` gây phân loại sai intent (ví dụ ca vỡ hàng `DAMAGED` bị phân loại thành `LATE`/`OTHER`), cộng thêm tải fallback cao làm tăng chi phí retry. | Trung bình | Trung bình–Cao | Nguyễn Khánh Vinh (`2A202603390`) | `llm_fallback_rate > 0.20` (20%) hoặc `escalation_rate` sụt giảm bất thường dù nhiều khiếu nại hàng vỡ | Bật fallback cứng khi `extract` lỗi 429 thì tự động `escalate` thay vì parse thô, đồng thời nâng `review_sampling_pct` từ `10%` lên `25%` khi `llm_fallback_rate > 0.15`. | Yêu cầu **Cải tiến thêm** hoặc tắt công tắc tự động nếu lỗi `extract` gây sai kết quả. | MEASURE |

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 5 (Hiệu năng, hạ tầng) | **Xong** *(đã kiểm thử tải gấp 3 + 60% lỗi 429 trên `S4`)* | `R-S4-after-20261118-201917-217918`: chịu được 60% `429` không hoàn sai (`llm_fallback_rate = 0.1854`); `2` người trực (`12 ca/giờ`) xử lý `0 ca ùn`, `wait_max = 15.0 phút`. | Nguyễn Khánh Vinh (`2A202603390`) |
| 6 (Chi phí) | **Xong** *(đạt cả ngày thường & ngày sale 11.11)* | `R-S4-after-20261118-201917-217918`: `7.296đ/ticket (<= 8.000đ)`, `ROI = 0.37 (>= 0.25)`, hoàn tự động `292.000đ <= 300.000đ`; `base`: `5.820đ/ticket`, `ROI = 0.72`. | Phạm Kiều Oanh (`NV-OANH`) |
| 7 (Vận hành) | **Xong** *(đã bổ sung 4 monitor, tăng trực ca sale & Runbook 4–5)* | `lab10/monitors.py` (`4` metric mới sáng đèn); `operating_gates.json` (`reviewers_on_shift = 2`, `daily_refund_cap_vnd = 300000`); Runbook 4–5 ở mục C11. | Trần Thị Hạnh (`NV-HANH`) |
| 9 (Quyết định) | **Xong** *(bản v2)* | `R-S4-grade-20261118-201926-217918` (`PASS-VISIBLE`, `Được phép cân nhắc Tiếp tục`) + Phiếu C mục C12. | Nguyễn Khánh Vinh (`2A202603390`) |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Trong Runbook 2 đã có cột `Thời gian chờ người duyệt lâu nhất (> 30p vàng, > 60p đỏ)`, `Số ca bị ùn (>= 1 đỏ)` và `Tổng tiền hoàn tự động một ngày`. Tuy nhiên **còn thiếu**: (1) tín hiệu đếm tải dồn theo giờ (`peak_hour_queue_load`), (2) tín hiệu đo tỉ lệ lỗi nhà cung cấp LLM (`llm_fallback_rate`), và (3) ngưỡng tiền ngày sale (`300.000đ`) khác với ngày thường (`1.500.000đ`). Nay đã bổ sung đủ cả 3 vào `lab10/monitors.py` và `config/operating_gates.json`. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | (1) `business.daily_refund_cap_vnd`: hạ từ `1.500.000đ` xuống **`300.000đ`** cho ngày sale (đồng bộ thêm đọc động `ops_limits()["daily_auto_refund_budget_vnd"]` trong `guards.py`); (2) `operations.review_capacity_per_hour`: đổi từ `6` thành **`null`** để tự động nhân theo số người trực (`12 ca/giờ`); (3) thêm ngưỡng cảnh báo ĐỎ `llm_fallback_rate > 0.15` và `peak_hour_queue_load > 12 ca/giờ`. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Tăng `operations.reviewers_on_shift` từ **`1` lên `2` người trực** mỗi ca sale (`12 ca/giờ`), giữ `approver_id = "NV-HANH"` (`Trần Thị Hạnh` đứng tên duyệt & điều phối thêm 1 nhân viên trực dự phòng CSKH), giữ `pic = "NV-TUNG"` (`Lê Thanh Tùng` nắm quyền thu hẹp phạm vi/công tắc). |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Giữ `pilot_scope = all` (`độ phủ = 1.0`), giữ `decision_note = true` và `review_sampling_pct = 10` (nhờ vậy `trust` đạt chuẩn và thời gian kiểm mẫu giữ ở `0.4` đơn vị), bổ sung quy tắc ngày sale phải đồng bộ trần `daily_refund_cap_vnd` từ Finance (`300.000đ`) trước giờ G. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | - **Với các hãng vận chuyển (`VNX`, `MKD`, `DNB`, `GHSH`, `LGX`) & shop:** Ở bản `base` có `27` lỗi ghi oan hãng do `fail_open`, nhưng từ cổng Vòng 1 (`prepared` & `after`) con số này đã về `0`; nếu có bản lỗi lọt ở production trước đó, **`Phạm Kiều Oanh (NV-OANH)`** gửi bảng đối soát gỡ strike & hoàn phạt trong vòng **24 giờ**.<br>- **Với nhân viên duyệt (`NV-HANH`):** **`Lê Thanh Tùng (NV-TUNG)`** thông báo ngay trong **15 phút** trên `#logix-pilot-ops-alerts` về việc cấp thêm người trực thứ 2 và kích hoạt chốt trần hoàn tự động `300.000đ`. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | `0` lần lộ PII (`pii_leaks = 0` trên cả `base`, `prepared`, `after` ở `S4` lẫn bộ nền). Nếu có phát sinh trong production, báo ngay trong **15 phút** cho `NV-TUNG` (PIC) và bộ phận Pháp lý/CSKH (`NV-OANH`, `NV-HANH`) để liên hệ đối tác xóa log. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Lộ ra trước qua **phản hồi của người** (tin nhắn lúc `23:40` của anh Tùng về hàng chờ > 1 tiếng và tin nhắn chị Oanh về vượt ngân sách `300.000đ`), vì ở Vòng 1 bàn chưa có metric thời gian thực theo giờ (`peak_hour_queue_load`, `llm_fallback_rate`, `auto_refund_day_max_vnd`) gắn cảnh báo tự động lên `#logix-pilot-ops-alerts`. Sau Vòng 2 đã có đủ 4 metric này. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp `3` lần trong một giờ (`peak_hour_queue_load > 12 ca/giờ` hoặc hàng chờ vượt `30 phút`) thì: **Trần Thị Hạnh (`NV-HANH`)** kích hoạt ngay người trực thứ `2` (`reviewers_on_shift = 2`, `12 ca/giờ`); nếu với `2` người trực mà hàng chờ vẫn vượt `45 phút` hoặc có ca sắp chạm `60 phút`, **Lê Thanh Tùng (`NV-TUNG`)** thu hẹp `business.pilot_scope` xuống `{"mode": "percent", "percent": 50}` thay vì thuê người thứ 3 (để tránh chi phí vượt `8.000đ/ticket`).
2. Nếu nhà cung cấp LLM lỗi (`llm_fallback_rate > 0.15` hoặc `429` kéo dài quá `10` phút) thì: kiểm tra ngay event log `llm_fallback_guarded` xem `write_gate` có giữ `wrongful_refund_vnd = 0` và `wrongful_carrier_faults = 0` không; nếu lỗi 429 lan sang cả bước `extract` làm sai `intent` hoặc hàng chờ bị nghẽn dây chuyền, **Lê Thanh Tùng (`NV-TUNG`)** tắt công tắc `issue_refund` trong `config/switches.json` trong tối đa `15` phút và chuyển toàn bộ luồng về CSKH xử lý tay.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: **Lê Thanh Tùng (`NV-TUNG`)** kiểm tra `trust_why` và trace của ticket đó (xác nhận `decision_note: true`, `approver_id = "NV-HANH"`, `review_sampling_pct >= 10%`, và không có `approval_id` hết hạn/sai ticket); nếu phát hiện quyết định tự động sai hoặc `approval_id` không khớp, nâng tạm `review_sampling_pct` lên `25–50%` và kiểm tra điều kiện dừng trong Runbook 3 trước khi chạy tiếp.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc (phút 185–200)

| | **v2** (phút 185–200, SAU sự cố `S4`) |
|---|---|
| Commit ký tiêu chí | `88d0de5` (`signed_at: 2026-11-18T19:53:06`, sha256 `ca98f5ab...`) — giống hệt v1 |
| Hash chốt cổng vòng 1 | `818eec21` — giống hệt v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ `S4`, mốc base: `R-S4-before-20261118-201926-217918` · prepared: `R-S4-prepared-20261118-201926-217918` · after: `R-S4-after-20261118-201926-217918` (kèm lần chạy `lab10.eval` `R-S4-after-20261118-201917-217918` và `base` `R-base-after-20261118-201918-217918`) |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | **Không** (`Không vượt trần kinh doanh / vận hành nào` trên cả `S4` lẫn `base`: `0` ca bị ùn, chờ lâu nhất `15.0 phút <= 60 phút`, `7.296đ/ticket <= 8.000đ`, `ROI = 0.37 >= 0.25`, hoàn tự động `292.000đ <= 300.000đ`, `0` lộ PII, `0` lỗi hãng oan). |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? | Trên `S4` mốc `after`: tất cả kho & hãng đều đạt `pass 1.0`, `0` hoàn sai, `0` lỗi oan, `0` PII; về chi phí trên `S4`, **`kho DN`** cao nhất là **`7.568đ/ticket`** (vẫn `< 8.000đ` tiêu chí và `< 10.000đ` làm tay). Trên `base` mốc `after`, **`kho ?`** (`T-018` thiếu đơn `O-9999`) là `10.359đ > làm tay` nhưng chỉ là 1 ca thiếu mã đơn buộc phải escalate. Do toàn bộ 4 kho thật (`CT`, `DN`, `HCM`, `HN`) và 5 hãng đều đạt chuẩn trên cả `S4` lẫn `base`, **quyết định không đổi**. |
| Quyết định (khoanh một) | **Tiếp tục** *(trong các lựa chọn: Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng — với điều kiện áp dụng cấu hình Vòng 2: `2` người trực ca sale + trần `300.000đ`)* |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S4-grade-20261118-201926-217918` (`R-S4-after-20261118-201917-217918`): toàn bộ **5/5 chỉ số bắt buộc** đạt 100% trên cả `S4` lẫn `base` — `pass_rate = 1.0 (≥ 0.96)`, `pass_k = 1.0 (≥ 0.91)`, `wrongful_refund_vnd = 0 (≤ 0)`, `wrongful_carrier_faults = 0 (≤ 0)`, `pii_leaks = 0 (≤ 0)`. |
| Bằng chứng 2 | `R-S4-after-20261118-201917-217918` & `R-base-after-20261118-201918-217918`: toàn bộ **3/3 ngưỡng `business_ops` đã ký đều `[ĐẠT]`** trên cả `S4` (`cost = 7.296đ ≤ 8.000đ`, `ROI = 0.37 ≥ 0.25`, `queue_stuck = 0 ≤ 0`, `auto_refund = 292.000đ ≤ 300.000đ`, `wait_max = 15.0p`) và `base` (`cost = 5.820đ ≤ 8.000đ`, `ROI = 0.72 ≥ 0.25`, `queue_stuck = 0`). *(Chỉ riêng chỉ số nên có `escalation_rate = 0.5122 > 0.35` trên `S4` do 36,6% ca hàng vỡ/thất lạc + 14,6% vượt trần sale `300.000đ`, không phải chỉ số chặn bắt buộc).* |
| Bằng chứng 3 | `R-S4-grade-20261118-201926-217918`: `1 integrity ✅`, `2 criteria ✅`, `3 visible ✅`, `5 regression ✅`, `6 monitor ✅` (cả 4 monitor mới `llm_fallback_rate`, `peak_hour_queue_load`, `auto_refund_day_max_vnd`, `model_override_rate` đều sáng đèn), kết luận report ghi rõ **`PASS-VISIBLE · Được phép cân nhắc 'Tiếp tục'`**. |
| Khớp dòng nào trong `decision_rule` đã ký? | Khớp dòng **`"Tiếp tục"`**: *"Toàn bộ 5 chỉ số bắt buộc ... và 3 ngưỡng business_ops ... đều đạt trên cả bộ nền VÀ gói sự cố, đồng thời report không có dòng vượt trần nào."* |
| Nếu Thu hẹp: cắt phần nào, vì sao | (không áp dụng cho v2 — giữ độ phủ `1.0`, chỉ thu hẹp xuống 50% theo Runbook 5 nếu tải thật vượt `> 20 ca duyệt/giờ`) |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | (không áp dụng cho v2) |
| Nếu Dừng: bài học ghi lại | (không áp dụng cho v2) |
| Ngày quyết định lại (trừ khi Dừng) | `2026-11-25` *(hoặc ngay sau ca sale ngày mai nếu `peak_hour_queue_load > 16 ca/giờ` hoặc `llm_fallback_rate > 0.20`)* |
| PIC ký | Nguyễn Khánh Vinh (`2A202603390`) |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Giữ** quyết định cấp Gate 1 là **`Tiếp tục`** (vì sau khi sửa ở mốc `after`, toàn bộ 5/5 chỉ số bắt buộc và 3/3 ngưỡng `business_ops` trên cả `S4` lẫn `base` đều đạt, `0` vượt trần, report ghi `Được phép cân nhắc 'Tiếp tục'`), **nhưng đổi bắt buộc cấu hình vận hành và ngân sách** so với v1: nâng `reviewers_on_shift` từ `1 -> 2` người (`12 ca/giờ`, giảm `queue_stuck` từ `5 → 0`, `wait_max` từ `82.0 phút → 15.0 phút` trong khi vẫn giữ `7.296đ <= 8.000đ` và `ROI = 0.37 >= 0.25`) và hạ `daily_refund_cap_vnd` từ `1.500.000đ -> 300.000đ` (đưa tổng hoàn tự động ngày từ `422.000đ -> 292.000đ <= 300.000đ`) — trả lời dứt khoát cho anh Tùng là **thêm người (lên 2) + siết trần sale 300k để tiếp tục chạy đợt sale ngày mai**.
- Report tự kiểm tra: mã lần chạy `R-S4-grade-20261118-201926-217918` · ô nào còn đỏ (nguyên nhân × tầng): **Không còn ô nào đỏ trên phần nhìn thấy (`visible`) và bộ nền (`base`)** — cả 5 mục `integrity`, `criteria`, `visible`, `regression`, `monitor` đều `✅` (`PASS-VISIBLE`); riêng mục `4 hidden` hiện dấu `—` do chạy trên máy học viên chưa có bộ test ẩn.
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Ở mốc `prepared`, cổng Vòng 1 đã **đỡ được 100% nguyên nhân kỹ thuật từ LLM 429 `fail_open`** (kéo `pass_rate` từ `0.8683 → 1.0`, `pass_k` từ `0.6829 → 1.0`, giảm hoàn sai `160.000đ → 0đ`, giảm lỗi oan hãng `27 → 0`); nhưng **bỏ sót 2 nguyên nhân ngoài code**: (1) trần `daily_refund_cap_vnd` vòng 1 để `1.500.000đ` theo ngày thường nên vượt ngân sách ngày sale `300.000đ` (`422.000đ`), và (2) chỉ bố trí `1` người trực nên hàng chờ ngập `5 ca ùn` (`82.0 phút`).
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report ghi chính xác **`"Được phép cân nhắc 'Tiếp tục'."`**; quyết định **Tiếp tục** của bàn khớp hoàn toàn với kết luận report và `decision_rule` đã ký.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Bộ thử hôm nay mới kiểm `llm_faults` ở bước `policy_check` với dữ liệu mock `41` ticket/ngày (`16 ca duyệt/giờ`) và chưa chạy **bài kiểm tra ẩn**; nếu đợt sale ngày mai lưu lượng tăng vượt `20–24 ca duyệt/giờ` hoặc LLM nghẽn `429` cả ở `extract`, quyết định `Tiếp tục` với `2` người trực sẽ nhanh chóng chuyển thành **Thu hẹp** phạm vi (`50%`) theo Runbook 5 để không vỡ chi phí `8.000đ/ticket`.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Thiết kế hiện giả định bão giờ cao điểm đợt sale chỉ đạt khoảng 16 ca cần duyệt mỗi giờ để 2 người trực (12 ca/giờ) xử lý kịp dưới SLA 60 phút và lỗi HTTP 429 chỉ ảnh hưởng bước policy_check mà không làm hỏng bước extract phân loại hàng vỡ/thất lạc.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Cổng code trong write_gate và trần tiền hoàn 300.000đ thực sự NGĂN được tác hại hoàn sai, phạt oan hãng và vượt ngân sách Finance (nhờ luôn đối chiếu tracking DB và khóa trước khi ghi sổ cái), còn việc tăng lên 2 người trực chỉ GIẢM khả năng ùn tắc hàng chờ vì nếu lưu lượng sale tăng vượt 24 ca duyệt mỗi giờ thì hàng chờ vẫn sẽ vượt SLA 60 phút.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Trong pilot thật trước Gate 2 cần đo lại phân phối lượt ticket thực tế theo từng giờ cao điểm, tỉ lệ lỗi API 429/timeout ở cả bước extract lẫn policy_check, thời gian duyệt thực tế mỗi ca của nhân viên CSKH có decision_note so với giả định 4–10 phút, và tỉ lệ khiếu nại ẩn từ hãng/shop khi đối chiếu sổ cuối tuần.
