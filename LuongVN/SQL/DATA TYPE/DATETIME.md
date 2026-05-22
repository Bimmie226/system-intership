# MySQL DATETIME Data Type
## Introduction
- DATETIME lưu ngày + giờ theo định dạng: 

  ```bash
  'YYYY-MM-DD HH:MM:SS'
  ```

## Chèn giá trị vào DATETIME
- Đúng định dạng: 

  ```sql
  INSERT INTO table_name(dt) VALUES ('2023-12-31 15:30:45');
  ```

- Giá trị mặc định:

  ```sql
  NOW()              -- trả về datetime hiện tại
  CURRENT_TIMESTAMP  -- tương tự NOW()
  ```

- Ví dụ:

  ```sql
  started_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
  ```

## DATETIME và TIMESTAMP
- `TIMESTAMP` thay đổi khi đổi `timezone`, `DATETIME` thì không.
- Ví dụ:
  - Khi bạn đổi timezone (`SET time_zone = '+03:00'`):

    - `TIMESTAMP` tự điều chỉnh lại giờ

    - `DATETIME` giữ nguyên

## Các hàm làm việc với DATETIME
### NOW()
- Lấy thời gian hiện tại: 

  ```sql
  SET @dt = NOW();
  SELECT @dt;
  ```

### DATE()
- Lấy phần ngày:

  ```sql
  WHERE DATE(create_at) = '2025-11-27'
  ```

### TIME()
- Lấy phần giờ:

  ```sql
  WHERE TIME(create_at) = '09:23:30'
  ```

### Tách từng thành phần thời gian

```sql
SELECT 
  YEAR(@dt),
  QUARTER(@dt),
  MONTH(@dt),
  WEEK(@dt),
  DAY(@dt),
  HOUR(@dt),
  MINUTE(@dt),
  SECOND(@dt);
```

### DATE_FORMAT() - định dạng datetime
```sql
SELECT DATE_FORMAT(@dt, '%H:%i:%s - %W %M %Y');
```

- Ví dụ kết quả: `14:22:30 - Thursday December 2023`

### DATE_ADD() - cộng thêm thời gian

```sql
SELECT @dt start, 
      DATE_ADD(@dt, INTERVAL 1 SECOND) '1 second later',
      DATE_ADD(@dt, INTERVAL 1 MINUTE) '1 minute later',
      DATE_ADD(@dt, INTERVAL 1 HOUR) '1 hour later',
      DATE_ADD(@dt, INTERVAL 1 DAY) '1 day later',
      DATE_ADD(@dt, INTERVAL 1 WEEK) '1 week later',
      DATE_ADD(@dt, INTERVAL 1 MONTH) '1 month later',
      DATE_ADD(@dt, INTERVAL 1 YEAR) '1 year later';
```

### DATE_SUB() - trừ đi thời gian

```sql
DATE_SUB(@dt, INTERVAL 1 WEEK)
```

### DATEDIFF() - tính số ngày
- Chỉ tính ngày, bỏ qua giờ phút giây

  ```sql
  SELECT dt, DATEDIFF(NOW(), dt)
  FROM datediff_test;
  ```