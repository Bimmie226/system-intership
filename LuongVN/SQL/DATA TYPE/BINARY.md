# MySQL BINARY Data Type
## Introduction
- `BINARY` là kiểu dữ liệu lưu trữ dữ liệu nhị phân cố định (fixed-length binary data).

- Thường dùng cho: hash, checksum (ví dụ SHA-256) hoặc các dữ liệu nhị phân có độ dài cố định.

- Cú pháp:

  ```sql
  column_name BINARY(size);
  ```
  - `size` = số byte tối đa của dữ liệu nhị phân

## Quy tắc lưu trữ
1. Right-padding với 0x00

   - Nếu dữ liệu nhị phân ngắn hơn `size`, MySQL sẽ tự động thêm byte `0x00` vào bên phải để đủ độ dài.

2. Không xóa byte khi truy xuất

   - Khi `SELECT` dữ liệu, các byte `0x00` thêm lúc chèn vẫn tồn tại.

3. So sánh `byte-by-byte`

   - Khi dùng `WHERE`, `ORDER BY`, `DISTINCT`, mọi byte đều quan trọng.

   - Hai giá trị chỉ bằng nhau khi tất cả byte trùng khớp.

4. `0x00` khác với space (`0x20`)

   - Byte null và khoảng trắng được MySQL phân biệt, ảnh hưởng tới so sánh và sắp xếp.

   - Null bytes được xếp trước space trong ORDER BY.