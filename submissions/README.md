# Bài học viên nộp (submissions)

Chỉ thêm nội dung khi **học viên thực sự thực hiện bài tập**. Thư mục này được theo dõi bởi Git để lưu minh chứng, nhưng không chứa thông tin riêng tư, khóa API, token hay dữ liệu vận hành sản xuất.

Cấu trúc đề xuất:

```text
submissions/
  semester-01/
    week-01/
      session-001/
        report.md
        solution.py
        evidence/          # hình/log đã ẩn thông tin nhạy cảm
```

Mỗi bài nộp phải nêu đề bài, tài liệu tham khảo, cách chạy, expected/actual, tình huống biên/lỗi và đánh giá của người học.

Sau khi tạo file thật:
```bash
python scripts/progress.py start 1
python scripts/progress.py submit 1 --evidence submissions/semester-01/week-01/session-001/report.md
```

Chỉ chạy lệnh `grade` sau khi AI/giảng viên đã đọc và đánh giá bài thực tế. Đừng đưa sẵn bài giải vào thư mục này.
