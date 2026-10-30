# PLC / SCADA + IIoT Learning

Chương trình tự học Kỹ thuật điều khiển & Tự động hóa công nghiệp, ưu tiên **mô phỏng trước, thiết bị thật sau**.

## Lịch học
- **104 tuần × 3 ngày/tuần × 2 giờ/ngày = 312 buổi, 624 giờ**
- Thứ Hai, Thứ Tư và Thứ Sáu: học 2 giờ/buổi; các ngày còn lại nghỉ hoặc tự ôn tùy chọn.
- Lịch dự kiến: 02/11/2026–27/10/2028 (có thể đổi).
- [Google Sheets – lộ trình từng ngày](https://docs.google.com/spreadsheets/d/1xPHHIHrBS6cPpaPiYvN9yzLG-ZiGUM93roKuzVM6iMw/edit)

## Bắt đầu
1. Đọc [hướng dẫn học](docs/study-guide.md) và [nguồn tài liệu](resources/README.md).
2. Thực hiện [tuần 01](curriculum/semester-01/week-01/README.md) theo lịch 3 buổi.
3. Lưu bài làm trong `labs/`; ghi kết quả/ảnh chụp vào `notes/`.
4. Cập nhật trạng thái trong Google Sheets; đưa code, test và kết quả vào commit.

## Lộ trình
| Giai đoạn | Tuần | Nội dung |
|---|---:|---|
| HK1 | 1–26 | Toán, điện, mạch, điện tử, Python, ESP32 cơ bản (tuần 23–26) |
| HK2 | 27–52 | Tín hiệu, điều khiển, cảm biến, truyền động, PLC |
| HK3 | 53–78 | PLC nâng cao, PID, HMI/SCADA, mạng công nghiệp, đồ án |
| HK4 | 79–104 | MQTT, bảo mật OT, ESP32 + IIoT (tuần 83–86), Python gateway, database, API, dashboard, capstone |

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

**Lưu ý:** các instruction files được áp dụng tùy agent/IDE và cấu hình phiên làm việc. Chúng không tạo ra một dịch vụ AI chạy thường trực trên GitHub; cần mở repository trong agent có hỗ trợ đọc quy tắc. Lịch 104 tuần ở Google Sheets là kế hoạch, **không đồng nghĩa đã có 312 giáo án chi tiết**. Việc chấm và ghi tiến độ yêu cầu có bài làm thực tế và quyền cập nhật.


## Codex & Google Antigravity (portable instructor skills)

Cả hai nền tảng dùng chung `AGENTS.md` và **4 skills** trong `.agents/skills/`:

| Skill | Nhiệm vụ | Codex | Antigravity |
|---|---|---|---|
| `teach-lesson` | Giảng bài 120 phút | `$teach-lesson` | `/teach-lesson` |
| `prepare-simulation-lab` | Hướng dẫn lab mô phỏng | `$prepare-simulation-lab` | `/prepare-simulation-lab` |
| `grade-submission` | Chấm điểm theo minh chứng /100 | `$grade-submission` | `/grade-submission` |
| `curate-learning-resources` | Tìm tài liệu và bài tập đúng bài | `$curate-learning-resources` | `/curate-learning-resources` |

Antigravity có thêm quy tắc kích hoạt theo ngữ cảnh trong `.agents/rules/`. **Không cần tạo `GEMINI.md` trùng lặp** vì đã có `AGENTS.md` dùng chung.

Xem [hướng dẫn cấu hình và smoke tests cho từng nền tảng](docs/agent-platforms.md). Các skill có thể được gọi tự động hoặc bằng cú pháp trên tùy phiên bản agent. Repository chỉ quy định hành vi; kết nối Google Sheets và khả năng thực thi code phụ thuộc quyền/công cụ của agent.


## Bản Excel trong GitHub
- [Lộ trình chuẩn 104 tuần / 312 buổi (XLSX)](roadmap/PLC_SCADA_IIoT_104_Weeks_3_Days_ESP32.xlsx)
- **Google Sheets** là bản dùng theo dõi tiến độ; **XLSX trong Git** là bản snapshot để lưu phiên bản và làm việc offline. Khi thay đổi một bản cần chủ động đồng bộ bản còn lại.
