# MySQL INSERT DATETIME
## Introduction
- DATETIME lưu trữ cả ngày và giờ
- Cú pháp:

  ```sql
  column_name DATETIME
  ```

- Định dạng:

  ```bash
  'YYYY-MM-DD HH:MM:SS'
  ```

## Examples
- Chèn DATETIME cụ thể:

  ```sql
  INSERT INTO events(event_name, event_time)
  VALUES('MySQL tutorial livestream', '2023-10-28 19:30:35');
  ```

- Chèn thời gian hiện tại:

  - Sử dụng hàm `NOW()`:

    ```sql
    INSERT INTO events(event_name, event_time)
    VALUES('MySQL Workshop', NOW());
    ```

- Chèn từ chuỗi thời gian khác định dạng:

  - Dùng `STR_TO_DATE()`:

    ```sql
    INSERT INTO events(event_name, event_time)
    VALUES('MySQL Party', STR_TO_DATE('10/28/2023 20:00:00', '%m/%d/%Y %H:%i:%s'));
    ```