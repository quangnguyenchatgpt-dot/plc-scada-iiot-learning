# PLC / SCADA + IIoT Learning

Chương trình tự học Kỹ thuật điều khiển & Tự động hóa công nghiệp, ưu tiên **mô phỏng trước, thiết bị thật sau**.

## Lịch học
- **104 tuần × 5 ngày/tuần × 2 giờ/ngày = 520 buổi, 1.040 giờ**
- Thứ Hai–Thứ Sáu: học và thực hành; Thứ Bảy–Chủ Nhật: nghỉ.
- Lịch dự kiến: 02/11/2026–27/10/2028 (có thể đổi).
- [Google Sheets – lộ trình từng ngày](https://docs.google.com/spreadsheets/d/1xPHHIHrBS6cPpaPiYvN9yzLG-ZiGUM93roKuzVM6iMw/edit)

## Bắt đầu
1. Đọc [hướng dẫn học](docs/study-guide.md) và [nguồn tài liệu](resources/README.md).
2. Thực hiện [tuần 01](curriculum/semester-01/week-01/README.md) theo lịch 5 buổi.
3. Lưu bài làm trong `labs/`; ghi kết quả/ảnh chụp vào `notes/`.
4. Cập nhật trạng thái trong Google Sheets; đưa code, test và kết quả vào commit.

## Lộ trình
| Giai đoạn | Tuần | Nội dung |
|---|---:|---|
| HK1 | 1–26 | Toán, điện, mạch, điện tử, Python/mô phỏng |
| HK2 | 27–52 | Tín hiệu, điều khiển, cảm biến, truyền động, PLC |
| HK3 | 53–78 | PLC nâng cao, PID, HMI/SCADA, mạng công nghiệp, đồ án |
| HK4 | 79–104 | MQTT, bảo mật OT, Python gateway, database, API, dashboard, capstone |

[Xem đề bài project](projects/README.md) · [Tiêu chí nghiệm thu](docs/assessment.md) · [Mẫu báo cáo lab](templates/lab-report.md)

> **An toàn:** Không làm việc với điện lưới, tủ điện đang mang điện hoặc thiết bị chuyển động nguy hiểm khi chưa có đào tạo và giám sát phù hợp. Mọi thử nghiệm khởi đầu dùng mô phỏng.


## AI Instructor / Trợ giảng cá nhân

Repo được cấu hình để agent hoạt động như **giảng viên kỹ thuật PLC/SCADA/IIoT**, không chỉ viết code:

- [AGENTS.md](AGENTS.md): hợp đồng hành vi và vai trò giảng viên cho các agent hỗ trợ.
- [.github/copilot-instructions.md](.github/copilot-instructions.md): hướng dẫn dành cho GitHub Copilot.
- [.cursor/rules/technical-instructor.mdc](.cursor/rules/technical-instructor.mdc): project rule dành cho Cursor.
- [Teaching contract](docs/teaching-contract.md): phong cách giảng dạy, an toàn, nguyên tắc không giải hộ.
- [Learning workflows](docs/learning-workflows.md): dạy → làm bài → chấm → chữa → ôn.
- [Learning progress](learning/progress.md): ghi nhận trạng thái học; **hiện bắt đầu ở Not Started**, chưa có điểm.
- [Daily lesson template](templates/daily-lesson.md), [exercise template](templates/exercise.md), [grading report](templates/grading-report.md).

### Cách gọi trong chat của AI agent (mở repository dưới dạng workspace)

```text
Bắt đầu học buổi tiếp theo theo AGENTS.md và learning/progress.md.
```

```text
Hãy giao 3 bài tập về chủ đề hôm nay, cho rubric và chỉ gợi ý khi tôi yêu cầu.
```

```text
Chấm bài trong [đường dẫn file nộp]. Giải thích từng lỗi, điểm /100,
phân biệt test đã chạy và test chưa chạy.
```

GitHub Copilot có prompt files:
- [Start lesson](.github/prompts/start-lesson.prompt.md)
- [Grade assignment](.github/prompts/grade-assignment.prompt.md)
- [Prepare lab](.github/prompts/prepare-lab.prompt.md)

**Lưu ý:** các instruction files được áp dụng tùy agent/IDE và cấu hình phiên làm việc. Chúng không tạo ra một dịch vụ AI chạy thường trực trên GitHub; cần mở repository trong agent có hỗ trợ đọc quy tắc. Lịch 104 tuần ở Google Sheets là kế hoạch, **không đồng nghĩa đã có 520 giáo án chi tiết**. Việc chấm và ghi tiến độ yêu cầu có bài làm thực tế và quyền cập nhật.
