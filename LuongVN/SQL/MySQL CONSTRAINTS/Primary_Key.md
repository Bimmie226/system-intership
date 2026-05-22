# MySQL Primary Key
## Introduction
- Primary key là cột hoặc tập hợp cột dùng để định danh duy nhất mỗi hàng trong bảng.

- Các cột của primary key phải unique và không được NULL.

- Mỗi bảng chỉ có thể có một primary key (hoặc không có).
- Cú pháp:

  - Single column primary key:

    ```sql
    CREATE TABLE table_name(
      column1 datatype PRIMARY KEY, 
      column2 datatype
    );
    ```

    Hoặc đặt cuối ds cột:

    ```sql
    CREATE TABLE table_name(
      column1 datatype, 
      column2 datatype,
      PRIMARY KEY(column1)
    );
    ```

  - Multi-column primary key:

    ```sql
    CREATE TABLE table_name(
      column1 datatype,
      column2 datatype,
      column3 datatype,
      PRIMARY KEY(column1, column2)
    );
    ```

- Thêm PRIMARY KEY vào bảng đã tồn tại:

  ```sql
  ALTER TABLE table_name
  ADD PRIMARY KEY(column1, column2, ...);
  ```

- Xóa PRIMARY KEY:

  ```sql
  ALTER TABLE table_name
  DROP PRIMARY KEY;
  ```

  