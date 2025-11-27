# MySQL DATE Data Type
## Introduction
- `DATE` là 1 trong 5 kiểu thời gian của MySQL
- Định dạng:

  ```css
  YYYY-MM-DD
  ```
- Phạm vi:

  ```yaml
  1000-01-01 → 9999-12-31
  ```

## Các hàm xử lý trong DATE
- Lấy ngày giờ hiện tại:

  ```sql
  SELECT NOW();
  ```

- Lấy phần ngày của DATETIME:

  ```sql
  SELECT DATE(NOW());
  ```

- Lấy hệ thống ngày hiện tại:

  ```sql
  SELECT CURDATE();
  ```

### DATE_FORMAT() - Định dạng ngày

```sql
SELECT DATE_FORMAT(CURDATE(), '%m/%d/%Y');
```

-> `01/30/2024`

### DATEDIFF() - Tính số ngày chênh lệch giữa 2 ngày

```sql
SELECT DATEDIFF('2015-11-04','2014-11-04');  -- 365
```

### DATE_ADD() - Cộng ngày, tuần, tháng, năm
```sql
SELECT DATE_ADD('2015-01-01', INTERVAL 1 MONTH);
```

### DATE_SUB() - Trừ ngày 
```sql
SELECT DATE_SUB('2015-01-01', INTERVAL 1 YEAR);
```

### Lấy thành phần ngày
```sql
SELECT
  DAY('2000-12-31'),
  MONTH('2000-12-31'),
  QUARTER('2000-12-31'),
  YEAR('2000-12-31');
```

### Các hàm liên quan đến tuần
```sql
SELECT
  WEEKDAY('2000-12-31'),   -- Thứ (0 = Monday)
  WEEK('2000-12-31'),      -- Tuần theo kiểu mặc định
  WEEKOFYEAR('2000-12-31');
```
