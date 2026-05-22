# MySQL TEXT Data Type
## Introduction
- `TEXT` là kiểu dữ liệu dùng để lưu chuỗi văn bản dài, từ vài byte tới vài GB.

- Không cần khai báo chiều dài như `CHAR/VARCHAR`.

- MySQL không pad hoặc trim khoảng trắng khi chèn hoặc truy vấn.

- Dữ liệu TEXT lưu trên đĩa, không nằm trong bộ nhớ → truy vấn chậm hơn `CHAR/VARCHAR`.

  | TEXT type      | Kích thước tối đa           | Overhead | Khi nào dùng                                               |
  | -------------- | --------------------------- | -------- | ---------------------------------------------------------- |
  | **TINYTEXT**   | 255 bytes (~255 ký tự)      | 1 byte   | Văn bản ngắn, không yêu cầu sắp xếp, ví dụ: trích dẫn blog |
  | **TEXT**       | 64 KB (~65,535 ký tự)       | 2 bytes  | Nội dung bài viết, mô tả sản phẩm                          |
  | **MEDIUMTEXT** | 16 MB (~16,777,215 ký tự)   | 3 bytes  | Văn bản lớn, sách, whitepaper                              |
  | **LONGTEXT**   | 4 GB (~4,294,967,295 ký tự) | 4 bytes  | Văn bản cực lớn, lưu trữ dữ liệu cực dài                   |
