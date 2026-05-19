# MySQL CHECK Constraint 
## Introduction
- CHECK đảm bảo giá trị lưu vào cột phải thỏa mãn 1 biểu thức boolean (TRUE hoặc UNKNOWN). Nếu bthuc là FALSE -> lỗi không cho INSERT/UPDATE
- Cú pháp:

  ```sql
  CONSTRAINT constraint_name 
  CHECK (expression)
  [ENFORCED | NOT ENFORCED]
  ```

## Examples
### Tạo check cấp 1

```sql
CREATE TABLE parts (
    part_no VARCHAR(18) PRIMARY KEY,
    description VARCHAR(40),
    cost DECIMAL(10,2 ) NOT NULL CHECK (cost >= 0),
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0)
);
```

### Tạo check cấp bảng

```sql
CREATE TABLE parts (
    part_no VARCHAR(18) PRIMARY KEY,
    description VARCHAR(40),
    cost DECIMAL(10,2 ) NOT NULL CHECK (cost >= 0),
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    CONSTRAINT parts_chk_price_gt_cost CHECK(price >= cost)
);
```


### Thêm CHECK vào bảng đã có
- tự sinh tên ràng buộc:

  ```sql
  ALTER TABLE parts
  ADD CHECK (part_no <> description);
  ```

- Tự đặt tên ràng buộc:

  ```sql
  ALTER TABLE parts
  ADD CONSTRAINT chk_part_name
  CHECK (part_no <> description);
  ```

### Xóa CHECK Constraint
- Ta phải biết tên constraint:

  ```sql
  ALTER TABLE parts
  DROP CHECK name_check_constraint;
  ```