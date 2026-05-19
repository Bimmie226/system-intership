# MySQL NOT NULL Constraint
## Introduction
- NOT NULL dùng để đảm bảo giá trị của một cột không được phép là NULL
- Cú pháp:

  ```sql
  column_name datatype NOT NULL
  ``` 

## Examples
- Tạo bảng có NOT NULL:

  ```sql
  CREATE TABLE tasks (
      id INT AUTO_INCREMENT PRIMARY KEY,
      title VARCHAR(255) NOT NULL,
      start_date DATE NOT NULL,
      end_date DATE
  );
  ```

- Thêm NOT NULL cho cột trong bảng đã tồn tại:
  - Giả sử bảng `tasks` đã có dữ liệu:


    ```sql
    INSERT INTO tasks(title, start_date, end_date)
    VALUES ('Learn MySQL NOT NULL constraint', '2017-02-01', '2017-02-02'),
           ('Check and update NOT NULL constraint to your database', '2017-02-01', NULL);
    ```

    ĐỔI `end_date` thành NOT NULL

  - Bước 1: Cập nhật NULL -> giá trị hợp lệ:

    ```sql
    UPDATE tasks
    SET end_date = start_date + 7
    WHERE end_date IS NULL;
    ```

  - Bước 2: Thêm ràng buộc `NOT NULL`:

    ```sql
    ALTER TABLE tasks 
    CHANGE end_date end_date DATE NOT NULL;
    ```

    - **NOTE**: `CHANGE old_col new_col new_definition`
- Xóa ràng buộc `NOT NULL`:

  ```sql
  ALTER TABLE tasks 
  MODIFY end_date DATE;
  ```