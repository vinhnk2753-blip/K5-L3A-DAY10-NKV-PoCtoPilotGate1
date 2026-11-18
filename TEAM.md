# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `NKV`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-NKV-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): *(chưa bốc — chờ phút 125)*

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Khánh Vinh | 2A202603390 | Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý | Có |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenKhanhVinh-2A202603390

### Phần việc phụ trách

- Làm việc độc lập nên kiêm cả 3 vai: **Kỹ sư cổng**, **Sản phẩm và kinh doanh**, **Vận hành và pháp lý**.
- Phụ trách toàn bộ câu 1.1–1.6 (Phiếu A, `config/acceptance_criteria.json`), câu 2.1–2.10 và quyết định v1 (Phiếu B, `lab10/guards.py`, `config/operating_gates.json`), và chuẩn bị Vòng 2 (`lab10/monitors.py`, Phiếu C, `submission/submission.json`).
- Có sử dụng trợ lý AI (Antigravity / Gemini) hỗ trợ rà soát codebase, kiểm tra ngưỡng kinh doanh/vận hành từ `data/world.json`, đề xuất cấu trúc guard và soát phiếu (mọi ngưỡng, thiết kế cổng và quyết định đều được kiểm chứng bằng số liệu chạy thực tế).

### Đóng góp cụ thể

- Thiết lập repo, cấu hình git và đối chiếu tài liệu Lab 9 (`PRD_v1.1.md`, `eval_card.md`, `failure_taxonomy.md`).
- Xây dựng Bản tiêu chí chấp nhận (`config/acceptance_criteria.json`) và điền Phiếu A trước khi chạy đánh giá.
- Phân tích rủi ro (bảng soát lỗi, bản đồ dữ liệu & drift, HAZOP, checklist 9 nhóm việc, pre-mortem), cài đặt cổng phòng ngừa vòng 1 (`lab10/guards.py`), cấu hình cổng vận hành/kinh doanh/pháp lý (`config/operating_gates.json`), chốt mốc `prepared` và lập quyết định Gate 1 v1.

### Bằng chứng

- *(Cập nhật mã commit, mã lần chạy `runs/<mã>` và dòng trong phiếu sau khi hoàn thành từng mốc Vòng 1 và Vòng 2.)*

### Exit ticket

- **Một điều học được:** *(cập nhật sau khi hoàn thành Vòng 2)*
- **Một điều còn chưa chắc:** *(cập nhật sau khi hoàn thành Vòng 2)*
