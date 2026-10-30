# Tiến độ học tập — hướng dẫn đọc

**Nguồn chính xác là [progress.json](progress.json)**, không phải bảng markdown này. Lịch: 104 tuần × 3 buổi × 2 giờ = **312 buổi / 624 giờ** (thứ Hai, Tư, Sáu).

Trạng thái ban đầu chưa có buổi nào hoàn thành và chưa có điểm. Agent phải đọc dữ liệu mới nhất từ `progress.json`, không suy luận theo ngày hiện tại. Nhật ký thay đổi nằm trong [history.jsonl](history.jsonl).

## Lệnh cần dùng

```bash
python scripts/progress.py status
python scripts/progress.py start 1
python scripts/progress.py submit 1 --evidence labs/semester-01/week-01/report.md
python scripts/progress.py grade 1 --score 85 --evidence labs/semester-01/week-01/report.md --feedback "Nhận xét dựa trên bằng chứng"
```

**Chỉ dùng đường dẫn có thật, đúng bài nộp.** Các lệnh thao tác tệp cục bộ; muốn agent khác thấy, cần commit/push thay đổi lên GitHub.

Hướng dẫn đầy đủ: [learning/README.md](README.md). Google Sheet theo dõi tùy chọn: https://docs.google.com/spreadsheets/d/1xPHHIHrBS6cPpaPiYvN9yzLG-ZiGUM93roKuzVM6iMw/edit
