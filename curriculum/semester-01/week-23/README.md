# Tuần 23 — ESP32 Embedded Fundamentals (6 giờ)

**Yêu cầu trước:** logic điện tử, digital I/O, nguồn 3.3V và lập trình cơ bản.

**Thiết bị:** chỉ cần máy tính và [Wokwi ESP32 Simulator](https://docs.wokwi.com/guides/esp32). Tài liệu bổ sung: [Arduino core for ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/).

## Thứ Hai (120 phút): ESP32 và GPIO
- Tìm hiểu vai trò GPIO, Input/Output, GND, mức logic 3.3V, chân có giới hạn.
- Mô phỏng LED nhấp nháy với ESP32 ảo; thay đổi chu kỳ 200/500/1000ms.
- Nộp `diagram.json` và source, ghi bảng 3 quan sát.

## Thứ Tư (120 phút): Nút nhấn và debounce
- Kết nối nút nhấn ảo; giải thích pull-up/pull-down.
- Viết mã đổi trạng thái LED sau mỗi lần nhấn, thử 10 lần nhấn.
- Mô phỏng rung phím hoặc nhấn nhanh; đề xuất debounce và thử lại.

## Thứ Sáu (120 phút): Bài tập tích hợp
- Mini-project đèn điều khiển bằng button có chế độ ON/OFF và đếm số lần bấm.
- Nộp sơ đồ, code, kết quả 3 test case và báo cáo.
- Đạt nếu code mô phỏng chạy, đếm đúng, không nhận nhầm khi nút giữ.

**An toàn:** ESP32 GPIO là mức 3.3V; không đấu 5V hay 24V trực tiếp. Đây là mô hình học tập, không phải bộ điều khiển an toàn công nghiệp.
