# MySQL ADD COLUMN
## Introduction
- Cú pháp:

  ```sql
  ALTER TABLE table_name
  ADD COLUMN new_column_name data_type 
  [FIRST | AFTER existing_column];
  ```

- Tên bảng: Sau từ khóa ALTER TABLE, bạn ghi tên bảng mà bạn muốn thêm cột mới.

- Cột mới và thuộc tính: Sau ADD COLUMN, bạn định nghĩa tên cột mới và kiểu dữ liệu của nó. Lưu ý rằng từ COLUMN là tùy chọn, bạn có thể bỏ qua.

- Vị trí cột: Bạn có thể chỉ định vị trí của cột mới trong bảng:

  - `FIRST`: đặt cột mới làm cột đầu tiên.

  - `AFTER existing_column`: đặt cột mới ngay sau cột đã tồn tại.

- Thêm nhiều cột cùng lúc:

  ```sql
  ALTER TABLE table_name
  ADD [COLUMN] column1 data_type [FIRST|AFTER existing_column],
  ADD [COLUMN] column2 data_type [FIRST|AFTER existing_column],
  ...;
  ```

## Examples
- Tạo bảng `vendors` với 2 cột `id` và `name`:

  ```sql
  CREATE TABLE vendors (
    id INT PRIMARY KEY,
    name VARCHAR(25)
  );
  ```

- Thêm cột `phone` sau `name`:

  ```sql
  ALTER TABLE vendors
  ADD phone VARCHAR(10) AFTER name;
  ```