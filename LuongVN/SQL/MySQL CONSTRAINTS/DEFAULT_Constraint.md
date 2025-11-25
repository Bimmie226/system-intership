# MySQL DEFAULT
## Introduction
- Dùng để gán 1 giá trị mặc định cho một cột trong MySQL
- Cú pháp:

  ```sql
  column_name datatype DEFAULT default_value
  ```

## Examples

```sql
CREATE TABLE cart_items 
(
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DEC(5,2) NOT NULL,
    sales_tax DEC(5,2) NOT NULL DEFAULT 0.1,
    CHECK(quantity > 0),
    CHECK(sales_tax >= 0) 
);
```

- `sales_tax` có DEFAULT = 0.1 (10%)
- Nếu bạn không nhập giá trị cho `sales_tax` → MySQL tự dùng 0.1.

### Thêm DEFAULT vào 1 cột của bảng đã tồn tại

- Cú pháp:
  ```sql
  ALTER TABLE table_name
  ALTER COLUMN column_name SET DEFAULT default_value;
  ```

- Ví dụ:

  ```sql
  ALTER TABLE card_items
  ALTER COLUMN quantity SET DEFAULT 1
  ```

### Xóa DEFAULT khỏi cột
- Cú pháp:

  ```sql
  ALTER TABLE table_name
  ALTER COLUMN column_name DROP DEFAULT;
  ```

- Ví dụ:

  ```sql
  ALTER TABLE cart_items
  ALTER COLUMN quantity DROP DEFAULT;
  ```