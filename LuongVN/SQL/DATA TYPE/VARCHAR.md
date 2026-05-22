# MySQL VARCHAR Data Type
## Introduction
- VARCHAR là kiểu chuỗi độ dài biến đổi (`variable-length`)
- Chiều dài tối đa có thể khai báo:

  ```sql
  VARCHAR(65535)
  ```

- Dữ liệu vượt quá độ dài VARCHAR -> báo lỗi
- VARCHAR và khoảng trắng:

  - Không tự động padding như CHAR. MySQL giữ nguyên khoảng trắng khi lưu và khi truy vấn.

    ```sql
    INSERT INTO items(title) VALUES ('AB ');
    SELECT title, LENGTH(title) FROM items;
    ```

    - Kết quả:

      ```sql
      title = 'AB ', LENGTH = 3
      ```

- Truncation khi có trailing spaces làm vượt chiều dài:

  - Ví dụ:

    ```sql
    INSERT INTO items(title) VALUES ('ABC ');
    ```

    - Chuỗi thực tế dài 4 nhưng VARCHAR(3):
      - MySQL cắt bỏ trailing space để còn 'ABC'
      - Chèn thành công nhưng báo warning: