# Lưu tiến độ học tập

## Nguồn dữ liệu
- **`learning/progress.json`**: dữ liệu chuẩn (machine-readable, lưu trong Git) của tối đa 312 buổi.
- **`learning/history.jsonl`**: nhật ký thay đổi (append-only trên máy khi dùng CLI).
- **`learning/progress.md`**: hướng dẫn và tóm tắt, không tự động chỉnh bằng tay khi JSON đã có dữ liệu.
- Google Sheets: kế hoạch và bảng theo dõi tùy chọn. **Không có đồng bộ hai chiều tự động.**

Mỗi buổi định danh bằng `session_id` 1–312; tuần `ceil(session_id/3)`, buổi trong tuần `(session_id-1)%3+1`. Học 120 phút/buổi, chọn bất kỳ 3 ngày trong tuần, không có thứ/ngày lịch cố định. Nếu bỏ lỡ, tiếp tục buổi chưa passed. Dữ liệu ban đầu trống: **chưa học / chưa có điểm**.

## Dùng công cụ (Python 3.9+; không cài thư viện ngoài)

Tại thư mục gốc của repo:

```bash
python scripts/progress.py status
python scripts/progress.py start 1
python scripts/progress.py submit 1 --evidence labs/semester-01/week-01/report.md --note "Đã nộp bài"
python scripts/progress.py grade 1 --score 84 --evidence labs/semester-01/week-01/report.md --feedback "Đạt, bổ sung giải thích sai số"
python scripts/progress.py status
python -m unittest discover -s tests -v
```

Các lệnh `start`, `submit`, `grade` thay đổi **tệp cục bộ ngay** và thêm nhật ký (atomic replace progress.json). Điểm `grade` chỉ hợp lệ khi có bài đã `submit`, đường dẫn bằng chứng, kết quả chấm thật và quyền chấm. Lệnh không tự chạy kiểm thử. Đừng dùng `--score` nếu giảng viên chưa đánh giá bài thật.

## Lưu bền vững lên GitHub
```bash
git add learning/progress.json learning/history.jsonl
git commit -m "Record learning progress"
git push origin main
```
Điều này là bước **bắt buộc để thiết bị/agent khác nhìn thấy tiến độ mới**. Nếu dùng Codex, Cursor hoặc Antigravity, chỉ yêu cầu agent commit/push khi bạn cho phép; tuyệt đối không ghi điểm thiếu minh chứng. Sau khi clone ở máy khác, `git pull` trước khi cập nhật để tránh xung đột.

## Quy tắc trạng thái
`not_started` (mặc định, không lưu record), `in_progress`, `submitted`, `needs_revision`, `passed`.

- Chỉ `passed` nếu score ≥75, có bằng chứng bài nộp và không có lỗi an toàn nghiêm trọng.
- Lần chấm mới được lưu vào `assessments[]` (không ghi đè điểm cũ).
- `status` tìm buổi **chưa passed đầu tiên**; không dựa vào ngày hiện tại hoặc số tuần lịch.
- Tệp JSON không ghi mật khẩu, token, thông tin cá nhân nhạy cảm hay dữ liệu hệ thống sản xuất.
- Không tự động đồng bộ lên Google Sheets; nếu cần, thực hiện riêng khi có quyền kết nối và xác nhận.
