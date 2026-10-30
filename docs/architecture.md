# Kiến trúc repository — PLC / SCADA / ESP32 / IIoT

## Mục tiêu thiết kế
Đây là **learning workspace**, không phải ứng dụng sản xuất. Tách bạch *giáo trình*, *bài mẫu*, *bài học viên nộp*, *hồ sơ tiến độ*, *quy tắc agent*, và *công cụ/kiểm thử*. Không giả định đã biên soạn đủ 312 giáo án.

```text
/
├── AGENTS.md                         # Hợp đồng agent trung tâm
├── .agents/                          # Skills & conditional rules Codex/Antigravity
├── .cursor/rules/                    # Cursor adapter: tham chiếu AGENTS.md
├── .github/
│   ├── copilot-instructions.md       # Copilot adapter: tham chiếu AGENTS.md
│   ├── prompts/                      # Shortcut để người học chủ động gọi
│   └── workflows/                    # CI validation
├── curriculum/semester-XX/week-XX/  # Giáo án được biên soạn, có thể thiếu tuần
├── labs/semester-XX/week-XX/        # MÃ MẪU, mô phỏng và test tham khảo
├── submissions/                     # BÀI HỌC VIÊN NỘP; chỉ tạo khi có thật
├── projects/                        # Danh mục milestone và project
├── resources/                       # Tài liệu hợp pháp có đường dẫn
├── roadmap/                         # Snapshot Excel được kiểm soát phiên bản
├── learning/
│   ├── progress.json                # NGUỒN CHÍNH của trạng thái học & điểm
│   ├── history.jsonl                # Nhật ký cập nhật tiến độ
│   ├── progress.md                  # Hướng dẫn; KHÔNG phải bản sao điểm
│   └── README.md                    # Quy trình khôi phục/đồng bộ
├── scripts/progress.py               # CLI quản lý tiến độ
├── tests/                            # Unit tests của CLI
└── templates/                        # Mẫu lesson, exercise, grading, lab
```

## Quy tắc nguồn dữ liệu (single source of truth)
| Dữ liệu | Nguồn chuẩn | Chính sách |
|---|---|---|
| Khung thời gian, bài học dự kiến | `roadmap/*.xlsx` (snapshot) + Google Sheets (bản làm việc) | Không tự đồng bộ; cập nhật giáo trình phải phát hành snapshot mới |
| Giáo án chi tiết đã biên soạn | `curriculum/**/README.md` | Nếu không tồn tại, agent phải nói chưa có và có thể tạo *draft* |
| Bài lab tham khảo | `labs/` | Không coi mã mẫu là bài học viên nộp |
| Bài làm/chứng cứ | `submissions/` (hoặc file bài thực tế khác do người học chỉ định) | Cấm dựng bằng chứng giả |
| Trạng thái và điểm | `learning/progress.json` | Không thay bằng Markdown hay Google Sheets |
| Nhật ký thay đổi | `learning/history.jsonl` + Git history | Chỉ ghi sự kiện thực tế |
| Quy tắc giảng viên | `AGENTS.md` | Adapter của mỗi IDE chỉ dẫn về đây |

## Vòng đời một buổi
`not_started → in_progress → submitted → passed | needs_revision → submitted`.

Chỉ thay trạng thái khi có hành động thực tế. `grade` phải có bài nộp và bằng chứng kiểm tra, điểm 0–100 và nhận xét. `passed` đòi hỏi ≥75 điểm và không có lỗi an toàn nghiêm trọng. Bài chưa đạt là đối tượng học tiếp (không bỏ qua do ngày lịch).

## Các quy tắc không phá vỡ dữ liệu
- Không đổi tên đường dẫn đã được giáo án hoặc progress JSON tham chiếu khi chưa có migration.
- Không để agent tự ý commit/push bài nộp, điểm hay thông tin riêng tư.
- Không ghi đè Google Sheet bằng file Excel snapshot cũ.
- Không thay đổi `learning/progress.json` khi đang chỉ review cấu trúc.
- Tạo bài học/lab mới qua PR hoặc commit có tiêu đề rõ và cập nhật index tương ứng.
