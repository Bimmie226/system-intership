# MySQL TIMESTAMP Data Type
## Introduction
- TIMESTAMP lưu ngày + giờ theo định dạng cố định:

  ```bash
  YYYY-MM-DD HH:MM:SS
  ```

- Phạm vi:
  ```sql
  1970-01-01 00:00:01 UTC → 2038-01-19 03:14:07 UTC
  ```

## TIMESTAMP phụ thuộc Time Zone
- Đây là điểm khác biệt lớn nhất so với `DATETIME`.

  - Khi `INSERT`, MySQL chuyển giá trị từ `timezone` kết nối → `UTC` để lưu.

  - Khi `SELECT`, MySQL chuyển giá trị từ `UTC` → `timezone` kết nối để hiển thị.

  - `DATETIME` không bao giờ đổi giá trị khi chuyển `timezone`.

  - `TIMESTAMP` luôn thay đổi nếu `timezone` thay đổi.
- Ví dụ:
  - Set timezone:

    ```sql
    SET time_zone = '+00:00';
    ```

  - Insert:

    ```sql
    INSERT INTO t VALUES ('2008-01-01 00:00:01');
    ```
  
  - Đọc lại -> ra đúng giá trị:

    ```yaml
    2008-01-01 00:00:01
    ```

  - Đổi timezone:

    ```sql
    SET time_zone = '+03:00';
    ```

  - SELECT lại:

    ```powershell
    2008-01-01 03:00:01   ← tự động +3 giờ
    ```

## Tính năng tự động khởi tạo và cập nhật (Automatic Initialization & Updating)
- TIMESTAMP có thể:

  - Tự động lưu timestamp khi dòng được tạo

  - Tự động cập nhật timestamp khi dòng được chỉnh sửa

### Automatic Initialization
  ```sql
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  ```
  - Khi INSERT không truyền giá trị, MySQL tự chèn thời điểm hiện tại.

### Automatic Updating
```sql
updated_at TIMESTAMP 
  DEFAULT CURRENT_TIMESTAMP 
  ON UPDATE CURRENT_TIMESTAMP
```
- Khi INSERT → MySQL tự gán giờ hiện tại.

- Khi UPDATE bất kỳ cột nào (thay đổi giá trị) → MySQL cập nhật lại giờ.