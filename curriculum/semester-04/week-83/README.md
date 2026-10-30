# Tuần 83 — ESP32 + IIoT (6 giờ)

**Yêu cầu:** ESP32 GPIO/ADC, Wi-Fi căn bản, MQTT topics/QoS, kiến thức JSON và Node-RED.

**Nguồn học:** [Espressif ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/), [Wokwi ESP32 Wi-Fi](https://docs.wokwi.com/guides/esp32-wifi), [HiveMQ MQTT Essentials](https://www.hivemq.com/mqtt/).

## Thứ Hai: ESP32 Wi-Fi (120 phút)
- Hiểu station mode, DHCP, SSID, reconnect.
- Trong Wokwi, quan sát trạng thái kết nối; ghi IP và sự kiện lỗi.
- Nộp mã, ảnh/log, 3 nhận xét.

## Thứ Tư: Telemetry MQTT (120 phút)
- Xây dựng cấu trúc topic `factory/lab/esp32-01/temperature` và JSON `{device_id,temperature,ts}`.
- Publish thông số cảm biến ảo theo chu kỳ 5 giây đến broker kiểm thử phù hợp.
- Kiểm tra dữ liệu và ghi rõ timestamp đơn vị UTC/local.

## Thứ Sáu: Mini project (120 phút)
- Tạo pipeline ESP32 (Wokwi) → MQTT broker → Node-RED debug/dashboard.
- Test 3 tình huống: bình thường, sensor không hợp lệ, mất kết nối (nếu mô phỏng hỗ trợ).
- Nộp source, flow, ảnh/traces, expected/actual và báo cáo.

**Ghi chú:** việc kết nối đến broker có thể phụ thuộc tính năng Wokwi và điều kiện mạng. Nếu không khả dụng, mô phỏng phần MQTT bằng Python để không bị chặn tiến độ.
