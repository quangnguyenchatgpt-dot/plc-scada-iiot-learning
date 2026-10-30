# Báo cáo review và chuẩn hóa cấu trúc

## Phạm vi
Đối chiếu cây thư mục GitHub, README, AGENTS.md, tài liệu nghiệp vụ, CLI quản lý tiến độ và bộ test. **Không** sửa/xóa trạng thái học đã ghi; không thay đổi nội dung Excel đã version hóa.

## Các vấn đề được phát hiện
| Mức độ | Vấn đề | Hướng khắc phục |
|---|---|---|
| Cao | AGENTS.md nhắc `progress.md` là nguồn chính ở đầu, nhưng cuối file xác định `progress.json` mới là nguồn chuẩn | Xác định rõ JSON là canonical ở đầu, dẫn tới tài liệu quy trình |
| Cao | README chứa nhiều phần hướng dẫn trùng lặp và ví dụ dẫn tới file report chưa tồn tại | Rút gọn README, phân chia quickstart và manual |
| Trung bình | `labs/` được dùng như ví dụ bài đã làm, dễ khiến agent chấm mã mẫu | Xác định labs=sample, submissions=student work |
| Trung bình | Không có bản đồ kiến trúc/canonical source rõ ràng | Thêm docs/architecture.md và index |
| Trung bình | `progress.json` và Google Sheets không tự đồng bộ nhưng một số mô tả dễ làm người dùng hiểu là có | Ghi rõ ranh giới và quy trình cập nhật |
| Trung bình | Giáo án có 3 tuần khởi đầu; Excel lên lịch đủ 312 buổi | Index liệt kê giáo án thật, không khẳng định đã viết hết |
| Thấp | Test và README nằm phân tán | Tổ chức bằng index và liên kết, không đổi path gây lỗi |

## Tiêu chuẩn acceptance
1. Giữ 104 tuần, 312 buổi, 624 giờ, lịch thứ Hai/Tư/Sáu.
2. `AGENTS.md` định nghĩa rõ nguồn trạng thái `learning/progress.json`.
3. Không xóa/di chuyển tệp giáo án hiện có và bản Excel.
4. Skills, Codex, Antigravity, Cursor, Copilot dùng chung hợp đồng giảng viên.
5. Có hướng dẫn `start → submit → grade → git commit/push` minh bạch.
6. Không tạo điểm hoặc bài nộp giả. Chỉ đẩy dữ liệu học tập khi có sự cho phép.
7. Có CI kiểm thử CLI tiến độ; phải xác minh kết quả chạy CI riêng, không coi file workflow tồn tại là tests passed.

## Còn cần triển khai
- Biên soạn giáo án có nguồn bài giảng cụ thể cho 309 tuần/đầu mục chưa có tệp (thực chất là 101 tuần chưa có file riêng, không phải 309 tuần).
- Nâng chất lượng bài lab và bộ test chuyên ngành.
- Công cụ đồng bộ Google Sheets có kiểm soát/xử lý xung đột nếu học viên yêu cầu.
