# Tuần 01 — Giới hạn & Đạo hàm

**Mục tiêu:** Hiểu giới hạn của hàm số, đạo hàm và cách xác minh bằng tính toán số. **Không cần thiết bị vật lý**.

## Ngày 01 — Giới hạn: khái niệm
- **20'** Ôn biến số, phân thức và giá trị hàm.
- **45'** Đọc [MIT OCW – Calculus](https://ocw.mit.edu/search/?q=calculus), tìm bài giới hạn (limits).
- **45'** Tính lim (x²−1)/(x−1), x→1 bằng phân tích nhân tử; so kết quả tại x=0.9, 0.99, 1.01, 1.001.
- **10'** Viết vì sao giá trị tại x=1 khác với giới hạn.
- **Nộp:** `day-01/solution.md`; tiêu chí: giới hạn 2, giải thích được điểm khuyết.

## Ngày 02 — Giới hạn: bài tập
- **15'** Ôn lý thuyết.
- **75'** Giải 3 bài: (1) lim (x²−4)/(x−2), x→2; (2) lim sin(x)/x, x→0; (3) lim (3x+1), x→2.
- **20'** Kiểm tra bằng bảng số gần điểm xét; nêu sai số do làm tròn.
- **10'** Ghi nhật ký.
- **Nộp:** `day-02/solution.md`; đáp án để tự đối chiếu: **4; 1; 7**.

## Ngày 03 — Đạo hàm: định nghĩa và quy tắc
- **20'** Ôn ý nghĩa độ dốc.
- **45'** Đọc mục đạo hàm trong MIT OCW Calculus.
- **45'** Tìm đạo hàm của f(x)=x³−4x²+2x; tính f'(2).
- **10'** Viết ý nghĩa đạo hàm trong kỹ thuật đo/điều khiển.
- **Nộp:** `day-03/solution.md`; đáp án f'(x)=3x²−8x+2, f'(2)=−2.

## Ngày 04 — Python lab: đạo hàm số
- **15'** Thiết lập Python.
- **70'** Hoàn thành [bài lab numerical derivative](../../../labs/semester-01/week-01/numerical_derivative.py) và chạy cho h = 0.1, 0.01, 0.001.
- **25'** So sánh sai số của forward difference và central difference, thử x=2 và x=0.
- **10'** Lưu kết quả.
- **Nộp:** output và nhận xét.

## Ngày 05 — Mini-project và kiểm tra
- **20'** Ôn giới hạn và đạo hàm.
- **60'** Hoàn thành bảng 8 điểm gần x=1 cho f(x)=(x²−1)/(x−1), và bảng sai số đạo hàm tại x=2.
- **30'** Trả lời: giới hạn là gì; tại sao thay trực tiếp có thể thất bại; đạo hàm có ý nghĩa gì; forward/central khác nhau thế nào; mô phỏng sai số đến từ đâu?
- **10'** Commit và ghi đánh giá.
- **Đạt:** ≥4/5 câu đúng; file code chạy; kết quả tái lập.
