# Quy trình giảng dạy, thực hành và đánh giá

## 1. PREPARE
- Đọc `learning/progress.json` qua `python scripts/progress.py status` nếu có thể. Không dựa vào ngày hiện tại.
- Dựa trên session ID, tính tuần `(id-1)//3+1`, buổi trong tuần `(id-1)%3+1`.
- Mở giáo án của tuần nếu có. Nếu chưa có, xem roadmap, tra tài liệu chính thức và tạo **bản nháp có nhãn draft**.
- Kiểm tra tiên quyết, công cụ/mô phỏng và 1–3 nguồn tham khảo. Phân biệt trang danh mục và link bài cụ thể.

## 2. TEACH (120 phút)
Mặc định: 15 phút nhắc lại → 35 phút khái niệm → 20 phút ví dụ hướng dẫn → 40 phút luyện tập độc lập → 10 phút tự kiểm. Nếu giáo án ngày cung cấp phân bổ khác nhưng tổng 120 phút, ưu tiên giáo án. Dạy theo từng phần; không giả vờ đã trôi qua 120 phút.

## 3. PRACTICE
Đề bài phải rõ đầu vào/đầu ra, đơn vị, phần mềm, hướng dẫn tái lập, case normal/boundary/fault khi phù hợp, đường dẫn nộp trong `submissions/` (không chấm `labs/` mẫu). Gợi ý dần, không đưa full solution trừ khi yêu cầu.

## 4. ASSESS
Đọc bài nộp thật. Thực thi test nếu có quyền và môi trường; nếu không ghi **chưa chạy**. Chấm theo `docs/assessment.md`, cung cấp bằng chứng, điểm /100, lỗi, cách cải thiện. Đạt khi ≥75 và không có lỗi an toàn nghiêm trọng.

## 5. PERSIST
Sau khi người học cho phép:
1. `python scripts/progress.py start <id>` khi bắt đầu.
2. `python scripts/progress.py submit <id> --evidence <file-da-ton-tai>` khi có bài nộp thực.
3. `python scripts/progress.py grade <id> --score N --evidence <same-file> --feedback "..."` sau khi chấm thật.
4. Nếu được phép rõ ràng, `git add` / `git commit` / `git push` để các thiết bị/agent khác nhận dữ liệu.
5. Google Sheets chỉ cập nhật theo yêu cầu và khi có kết nối. Nếu xung đột với JSON, báo rõ, không ghi đè âm thầm.

## 6. REVIEW / ÔN TẬP
Nhận xét sai sót, đưa 1–3 câu ôn tăng cường và xác định buổi chưa passed tiếp theo. Chỉ đổi lộ trình khi người học chấp thuận.

## 7. QUY TẮC BỔ SUNG
- Không tạo bài nộp/chứng cứ hoặc điểm số giả.
- Không sửa hoặc xóa `learning/progress.json` trong tác vụ review hoặc tái cấu trúc repository.
- Không đưa secrets, API keys, nhật ký sản xuất hoặc dữ liệu riêng tư lên GitHub.
- Không tự suy đoán tài liệu 312 buổi đã hoàn chỉnh: chỉ số tuần trong roadmap không đảm bảo tồn tại giáo án.
