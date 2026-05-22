# MySQL DROP TABLE
- DROP TABLE dùng để xóa hoàn toàn một hoặc nhiều bảng và dữ liệu bên trong khỏi cơ sở dữ liệu.

- Không ảnh hưởng đến quyền truy cập đã gán cho bảng.

- Cú pháp:
  ```sql
  DROP [TEMPORARY] TABLE [IF EXISTS] table_name [, table_name ...] [RESTRICT | CASCADE];
  ```

- Ví dụ:
  - Xóa 1 bảng:

    ```sql
    DROP TABLE insurances;
    ```

  - Xóa nhiều bảng cùng lúc:

    ```sql
    DROP TABLE CarAccessories, CarGadgets;
    ```

  - Xóa bảng ko tồn tại với IF EXISTS:

    ```sql
    DROP TABLE IF EXISTS aliens;
    SHOW WARNINGS;
    ```