# Báo cáo review & chuẩn hóa cấu trúc dự án

## Phạm vi và nguyên tắc
Đã khảo sát tree GitHub, kiểm tra nội dung README, AGENTS.md, cấu hình agent, CLI và unit tests. Đợt chuẩn hóa này chỉ thay đổi **cấu trúc tài liệu và hướng dẫn**; không xóa/di chuyển giáo án, nguồn Excel hay sửa `learning/progress.json`.

## Phát hiện & xử lý
| Ưu tiên | Phát hiện | Cách xử lý |
|---|---|---|
| Cao | Mâu thuẫn giữa `progress.md` và `progress.json` về nguồn trạng thái chính | Quy định JSON là canonical; Markdown chỉ là hướng dẫn |
| Cao | README cũ dài, lặp vai trò cấu hình và ví dụ đường dẫn chưa tồn tại | Thiết kế quickstart rõ ràng, phân tách sang docs |
| Cao | Dễ chấm nhầm lab mẫu như bài đã nộp | Quy định `labs/` là sample, `submissions/` là bài thật |
| Trung bình | Chưa có sơ đồ cây và quy tắc cập nhật | Tạo `docs/architecture.md` và index |
| Trung bình | Khả năng hiểu nhầm Excel/Sheets tự đồng bộ với Git | Ghi rõ snapshot, tiến độ, chính sách đồng bộ |
| Trung bình | 104 tuần trong roadmap nhưng chưa có 104 giáo án | Index các tuần đã có, yêu cầu đánh dấu draft |
| Trung bình | Adapter Copilot/Cursor/skills còn trỏ tiến độ tới `progress.md` | Chuyển sang `progress.json` |
| Thấp | Các lệnh và tài liệu bị phân tán | Bổ sung link điều hướng và hướng dẫn phân lớp |

## Tiêu chí hoàn thành
- Lịch chuẩn: **104 tuần × 3 buổi × 2 giờ = 312 buổi / 624 giờ**.
- Canonical progress: `learning/progress.json`; evidence từ bài thực tế; agent không tự ghi điểm.
- Giữ nguyên file Excel và các giáo án đã soạn.
- Các adapter Codex, Antigravity, Cursor, Copilot hướng về `AGENTS.md`.
- CI có workflow kiểm thử; **kết quả chạy CI cần được kiểm chứng riêng**.

## Hạn chế còn tồn tại
- **101 tuần** chưa có giáo án Markdown riêng (đã có 3 tuần khởi đầu).
- Lịch Excel/Google Sheets có nhiều đường dẫn tới trang chủ hoặc danh mục, chưa xác minh từng chương/bài.
- Chưa có công cụ đồng bộ trạng thái JSON → Google Sheets; cần xây có quản lý xung đột khi thực sự cần.
- Chưa kiểm thử thao tác end-to-end trên cả bốn IDE hoặc xác minh việc chạy GitHub Actions trong đợt review này.
