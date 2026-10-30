# PLC / SCADA + IIoT Learning Workspace

Chương trình tự học kỹ thuật **Điện – Điện tử → ESP32 Embedded → PLC / HMI / SCADA → Industrial IoT**, ưu tiên mô phỏng và bài tập có chấm điểm minh bạch.

**Thời lượng:** 104 tuần · 3 buổi/tuần (thứ Hai, Tư, Sáu) · 2 giờ/buổi = **312 buổi / 624 giờ**. Ngày bắt đầu kế hoạch: 02/11/2026 (có thể thay đổi mà không coi ngày trên lịch là tiến độ học).

## Bắt đầu trong 3 bước

1. Đọc [AGENTS.md](AGENTS.md) để agent đóng vai giảng viên; xem [cấu trúc dự án](docs/architecture.md).
2. Xem [giáo án tuần 01](curriculum/semester-01/week-01/README.md) và [kế hoạch Excel](roadmap/README.md).
3. Mở repo trong Codex / Antigravity / Cursor / Copilot, yêu cầu: **“Đọc AGENTS.md và learning/progress.json, bắt đầu buổi chưa đạt đầu tiên; hướng dẫn và giao bài nhưng không giải hộ.”**

## Cấu trúc

| Thư mục / Tệp | Vai trò |
|---|---|
| [AGENTS.md](AGENTS.md) + [.agents/](.agents/) | Hợp đồng giảng viên và kỹ năng dùng chung |
| [curriculum/](curriculum/) | Giáo án **đã biên soạn** (hiện có 3 tuần mẫu) |
| [roadmap/](roadmap/) | [Excel snapshot 104 tuần / 312 buổi](roadmap/PLC_SCADA_IIoT_104_Weeks_3_Days_ESP32.xlsx) |
| [resources/](resources/) | Tài liệu học, phần mềm, nguồn tham khảo |
| [labs/](labs/) | Mã lab mẫu và mô phỏng |
| [submissions/](submissions/) | Bài **thực tế** học viên nộp |
| [projects/](projects/) | Đề tài, milestone, rubric |
| [learning/](learning/) | Tiến độ chuẩn `progress.json`, lịch sử chấm |
| [scripts/](scripts/) + [tests/](tests/) | CLI tiến độ và unit tests |
| [docs/](docs/) + [templates/](templates/) | Quy trình và mẫu bài học/báo cáo |

Các phần trên được mô tả chi tiết ở [architecture](docs/architecture.md) và [báo cáo review](docs/review-report.md).

## Lịch học và giáo án

- Lịch đầy đủ từng buổi: [Google Sheets](https://docs.google.com/spreadsheets/d/1xPHHIHrBS6cPpaPiYvN9yzLG-ZiGUM93roKuzVM6iMw/edit) và [Excel được version hóa](roadmap/PLC_SCADA_IIoT_104_Weeks_3_Days_ESP32.xlsx).
- Giáo án đã viết: [Tuần 01](curriculum/semester-01/week-01/README.md), [Tuần 23 — ESP32](curriculum/semester-01/week-23/README.md), [Tuần 83 — ESP32 IIoT](curriculum/semester-04/week-83/README.md).
- **Các tuần chưa có file giáo án chi tiết**; AI chỉ được tạo dự thảo dựa trên lịch và nguồn được kiểm tra, không khẳng định đã tồn tại 312 bài giảng.

## Lưu tiến độ

`learning/progress.json` là **nguồn chính** cho trạng thái, điểm số và buổi học tiếp theo; `learning/history.jsonl` lưu lịch sử. Google Sheets là bản kế hoạch/theo dõi tùy chọn, **không tự đồng bộ**.

```bash
python scripts/progress.py status
python scripts/progress.py start 1
# Sau khi bạn đã tạo file bài nộp thật:
python scripts/progress.py submit 1 --evidence submissions/semester-01/week-01/session-001/report.md
# Chỉ dùng khi đã có bài và giảng viên đánh giá dựa trên minh chứng:
python scripts/progress.py grade 1 --score 85 --evidence submissions/semester-01/week-01/session-001/report.md --feedback "Đạt yêu cầu"
```

Lệnh ghi dữ liệu **cục bộ**. Để các agent/máy khác đọc được, cần `git add`, `git commit`, `git push` khi bạn đã đồng ý. [Hướng dẫn chi tiết](learning/README.md).

## AI hỗ trợ

- **Codex + Antigravity:** dùng `AGENTS.md`, bốn skill trong `.agents/skills/`.
- **Antigravity:** hai rule có điều kiện trong `.agents/rules/`.
- **Cursor:** `.cursor/rules/technical-instructor.mdc`.
- **GitHub Copilot:** `.github/copilot-instructions.md` và `.github/prompts/`.

[Hướng dẫn từng agent](docs/agent-platforms.md) · [Quy trình giảng dạy](docs/learning-workflows.md) · [Rubric](docs/assessment.md)

> **An toàn:** Mô phỏng trước; không đấu điện lưới/24V trực tiếp vào GPIO ESP32 3.3V; không thay chức năng an toàn máy bằng PLC thường. Repo hiện là **public**, vì vậy không commit thông tin nhạy cảm hoặc dữ liệu thực tế có tính riêng tư.
