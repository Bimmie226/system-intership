# MySQL CHAR Data Type
## Introduction
- `CHAR` là fixed-length(độ dài cố định)
- Khai báo:

  ```sql
  CHAR(n)
  ```
  - MySQL luôn lưu đúng n ký tự bằng cách đệm dấu cách ở cuối (padding).
- Khi truy vấn, MySQL tự động bỏ dấu cách cuối (trừ khi bật chế độ `PAD_CHAR_TO_FULL_LENGTH`).

## Examples
- Tạo bảng:

  ```sql
  CREATE TABLE mysql_char_test (
      status CHAR(3)
  );
  ```

- Thêm dữ liệu:

  ```sql
  INSERT INTO mysql_char_test(status)
  VALUES ('Yes'), ('No');
  ```

## So sánh giá trị CHAR
- MySQL bỏ qua trailing spaces khi so sánh với các toán tử:

  ```bash
  =, <>, >, <, <=, >=
  ```

- Nhưng với LIKE, MySQL không bỏ trailing spaces:

  ```sql
  status LIKE 'Y'   → không match 'Y '
  ```


  