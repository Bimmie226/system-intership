# MySQL UNIQUE Constraint
## Introduction
- UNIQUE constraint dùng để đảm bảo rằng giá trị trong 1 cột hoặc 1 nhóm cột không bị trùng lặp
- Cú pháp:

  ```sql
  CREATE TABLE table_name (
    column1 datatype UNIQUE
  );
  ```

  - Ví dụ:

    ```sql
    phone VARCHAR(15) UNIQUE
    ```

    -> Cột `phone` không được có giá trị trùng

- UNIQUE cho nhiều cột:

  ```sql
  UNIQUE(column1, column2)
  ```

- UNIQUE có tên rõ ràng (đặt tên constraint):

  ```sql
  CONSTRAINT constraint_name
  UNIQUE(column_list)
  ```

  - Ví dụ: 

    ```sql
    CONSTRAINT uc_name_address UNIQUE(name, address)
    ```

