# MySQL Foreign Key
## Introduction
- Khóa ngoại là cột(hoặc nhóm cột) trong bảng con tham chiếu đến cột(thường là khóa chính) trong bảng cha.
- Nó giúp đảm bảo tính toàn vẹn dữ liệu: các giá trị trong bảng con phải tồn tại trong bảng cha hoặc là NULL.
  - Bảng cha = bảng được tham chiếu
  - Bảng con = bảng tham chiếu
  - Có thể tự tham chiếu(recursive), ví dụ: `employees.reportsTo -> employees.employeeNumber`
- Cú pháp:

  ```sql
  [CONSTRAINT ten_rangbuoc] 
  FOREIGN KEY (cot_con, ...)
  REFERENCES bang_cha(cot_cha, ...)
  [ON DELETE thao_tac]
  [ON UPDATE thao_tac]
  ```
  - `thao_tac` có thể:
    - `CASCADE`: tự động cập nhật/xóa các hàng con khi hàng cha thay đổi
    - `SET NULL`: Đặt giá trị cột con thành `NULL` khi hàng cha thay đổi
    - `RESTRICT / NO ACTION`: không cho phép thay đổi nếu có hàng con tồn tại
    - `SET DEFAULT`: 
  - Mặc định: `RESTRICT` 

## Examples
### RESTRICT / NO ACTION

```sql
CREATE TABLE categories (
  categoryId INT AUTO_INCREMENT PRIMARY KEY, 
  categoryName VARCHAR(100) NOT NULL
) ENGINE=INNODB;

CREATE TABLE products (
  productId INT AUTO_INCREMENT PRIMARY KEY, 
  productName VARCHAR(100) NOT NULL, 
  categoryId INT, 
  CONSTRAINT fk_category FOREIGN KEY (catogoryId)
    REFERENCES categories(categoryId)
) ENGINE=INNODB;
```

- Thêm `categoryId` không có trong `categories` -> báo lỗi
- Cập nhật / xóa `categoryId` đang được tham chiếu -> báo lỗi

### CASCADE

```sql
CREATE TABLE products (
  productId INT AUTO_INCREMENT PRIMARY KEY,
  productName VARCHAR(100) NOT NULL, 
  categoryId INT, 
  CONSTRAINT fk_category FOREIGN KEY (categoryId) 
    REFERENCES categories(categoryId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE=INNODB;
```

- Cập nhật `categoryId` ở bảng cha -> các hàng con tự động cập nhật
- Xóa `categoryId` ở bảng cha -> các hàng con tự động xóa

### SET NULL

```sql
CREATE TABLE products (
  productId INT AUTO_INCREMENT PRIMARY KEY,
  productName VARCHAR(100) NOT NULL,
  categoryId INT,
  CONSTRAINT fk_category FOREIGN KEY (categoryId)
    REFERENCES categories(categoryId)
    ON UPDATE SET NULL
    ON DELETE SET NULL
) ENGINE=INNODB;
```
- Cập nhật `categoryId` ở bảng cha → các hàng con tự động thành `NULL`.
- Xóa `categoryId` ở bảng cha → các hàng con tự động thành `NULL`.

### Xóa khóa ngoại

```sql
ALTER TABLE products 
DROP FOREIGN KEY fk_category;
```
- Xem tên ràng buộc của khóa ngoại:

  ```sql
  SHOW CREATE TABLE products;
  ```

### Tạm tắt kiểm tra khóa ngoại
- Dùng khi import dữ liệu:

  ```sql
  SET foreign_key_checks = 0; -- tắt
  SET foreign_key_checks = 1; -- bật lại
  ```