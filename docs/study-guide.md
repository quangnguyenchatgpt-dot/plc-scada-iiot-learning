# Phương pháp học linh hoạt — 3 buổi × 120 phút / tuần

**Tự chọn bất kỳ 3 ngày nào mỗi tuần.** Đây là nhịp học dự kiến, **không có ngày/giờ cố định**. Nếu một tuần học ít hơn 3 buổi, giữ nguyên buổi chưa hoàn thành và tiếp tục khi có thời gian. Không bắt buộc học bù, không tự đánh dấu vắng mặt.

| Thứ tự trong tuần nội dung | Thời lượng 120 phút | Sản phẩm |
|---|---|---|
| Buổi 1/3 — Giảng + ví dụ | 15' ôn + 35' lý thuyết + 25' ví dụ + 35' tự giải + 10' kiểm tra | Ghi chú và bài giải |
| Buổi 2/3 — Mô phỏng | 10' ôn + 20' hướng dẫn + 65' thực hành + 15' thử lỗi + 10' nhật ký | Lab và log |
| Buổi 3/3 — Tích hợp | 15' ôn + 65' mini-project + 30' quiz + 10' tổng kết | Mini-project và báo cáo |

**104 tuần nội dung × 3 buổi × 2 giờ = 624 giờ**, không cam kết hoàn thành trong 104 tuần lịch nếu nghỉ học hoặc học chậm hơn.

## Quy tắc tiến độ
- `learning/progress.json` là trạng thái chính xác; trạng thái `passed` chỉ có sau chấm điểm dựa trên bài thật.
- `python scripts/progress.py status` tìm buổi chưa `passed` đầu tiên.
- Không dùng ngày lịch để xác định buổi học; `Ngày học thực tế` trên Google Sheets chỉ ghi khi buổi đó thật sự diễn ra.
- Học bằng mô phỏng trước (Wokwi, LTspice, CODESYS), không đấu điện công nghiệp trực tiếp vào ESP32 GPIO.
- Bài nộp ở `submissions/`; mã mẫu tham khảo ở `labs/`.
