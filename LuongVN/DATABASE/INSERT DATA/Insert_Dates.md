# MySQL INSERT DATE
- Kiểu dữ liệu DATE dùng để lưu trữ ngày. 
- Cú pháp khai báo cột:

  ```sql
  column_name DATE
  ```

- Định dạng:

  ```sql
  'YYYY-MM-DD'
  ```

## Chèn giá trị ngày cố định

```sql
INSERT INTO events(event_name, event_date)
VALUES('MySQL Conference', '2023-10-29');
```
- Lưu ý định dạng đúng
- Nếu giá trị ngày sai -> báo lỗi

## Chèn ngày hiện tại
- `CURRENT_DATE()`

  ```sql
  INSERT INTO events(event_name, event_date)
  VALUES('MySQL Replication Workshop', CURRENT_DATE);
  ```

## Chèn từ chuỗi ngày khác định dạng chuẩn

- Dùng `STR_TO_DATE()`:

  ```sql
  INSERT INTO events(event_name, event_date)
  VALUES('MySQL Innovate', STR_TO_DATE('10/29/2023', '%m/%d/%Y'));
  ```