# MySQL TIME Data Type
## Introduction
- Đùng để lưu thời gian trong ngày hoặc khoảng thời gian
- Định dạng:

  ```yaml
  HH:MM:SS
  ```

- Khai báo:

  ```sql
  column_name TIME;
  column_name TIME(N);   -- N = 0 đến 6 (microseconds)
  ```

## Các hàm xử lý TIME
### Lấy thời gian hiện tại

```sql
SELECT CURRENT_TIME();    -- dạng string
SELECT CURRENT_TIME() + 0; -- dạng số HHMMSS
```

### Cộng/Trừ thời gian
- `ADDTIME()`

  ```sql
  SELECT ADDTIME(CURRENT_TIME(), 023000);
  ```

- `SUBTIME()`

  ```sql
  SELECT SUBTIME(CURRENT_TIME(), 023000);
  ```

- `TIMEDIFF()` - Lấy hiện 2 thời điểm

  ```sql
  SELECT TIMEDIFF(end_at, start_at) FROM tests;
  ```

- `TIME_FORMAT()` - định dạng thời gian

  ```sql
  SELECT TIME_FORMAT(start_at, '%h:%i %p');
  ```

  - `%h` – giờ 2 chữ số (1–12)

  - `%i` – phút

  - `%p` – AM/PM
  
### Lấy thành phần thời gian

```sql
SELECT
  HOUR(start_at),
  MINUTE(start_at),
  SECOND(start_at)
FROM tests;
```