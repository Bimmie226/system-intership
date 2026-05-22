# MySQL BOOLEAN Data Type
## Introduction
- MySQL không có kiểu BOOLEAN thật sự.
- Giá trị:
  - 0 -> FALSE
  - Non-zero -> TRUE
- BOOLEAN Literals:
  - Có thể dùng: `true`, `false`, `TRUE`, `FALSE`, `True`, `False`
    
    → MySQL chuyển thành 1 và 0.  

## Examples
- Tạo bảng: 

  ```sql
  CREATE TABLE tasks (
      id INT AUTO_INCREMENT PRIMARY KEY,
      title VARCHAR(255) NOT NULL,
      completed BOOLEAN
  );
  ```

- Chèn dữ liệu:

  ```sql
  INSERT INTO tasks(title, completed)
  VALUES ('Master MySQL Boolean type', true),
        ('Design database table', false);
  ```

### BOOLEAN OPERATOR
- Dùng `IS TRUE` thay vì `=`

  ```sql
  WHERE completed IS TRUE;
  ```

- Lấy task chưa hoàn thành:

  ```sql
  WHERE completed IS FALSE;
  ```

- Lấy task không phải TRUE:

  ```sql
  WHERE completed IS NOT TRUE;
  ```

  - Bao gồm `0` và `NULL`