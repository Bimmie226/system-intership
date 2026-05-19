# MySQL ON DELETE CASCADE
- `ON DELETE CASCADE` cho phép xóa tự động các bản ghi ở bảng con khi bản ghi tương ứng ở bảng cha bị xóa
- Đây là cách hiệu quả để quản lý dữ liệu quan hệ 1:N mà không cần xóa thủ công từng bảng con

## Ví dụ
- Bước 1: Tạo bảng building(bảng cha)

  ```sql
  CREATE TABLE buildings (
      building_no INT PRIMARY KEY AUTO_INCREMENT,
      building_name VARCHAR(255) NOT NULL,
      address VARCHAR(255) NOT NULL
  );
  ```

- Bước 2: Tạo bảng rooms (bảng con) với khóa ngoại `ON DELETE CASCADE`

  ```sql
  CREATE TABLE rooms (
      room_no INT PRIMARY KEY AUTO_INCREMENT,
      room_name VARCHAR(255) NOT NULL,
      building_no INT NOT NULL,
      FOREIGN KEY (building_no)
          REFERENCES buildings (building_no)
          ON DELETE CASCADE
  );
  ```

- Bước 3: Thêm dữ liệu vào `buildings`:

  ```sql
  INSERT INTO buildings(building_name,address)
  VALUES 
  ('ACME Headquaters','3950 North 1st Street CA 95134'),
  ('ACME Sales','5000 North 1st Street CA 95134');
  ```

- Bước 4: Thêm dữ liệu vào `rooms`:

  ```sql
  INSERT INTO rooms(room_name,building_no)
  VALUES
  ('Amazon',1),
  ('War Room',1),
  ('Office of CEO',1),
  ('Marketing',2),
  ('Showroom',2);
  ```

- Bước 5: Xóa 1 toà nhà:

  ```sql
  DELETE FROM buildings 
  WHERE building_no = 2;
  ```
  - Tòa nhà số 2 bị xóa
  - Các phòng thuộc tòa nhà số 2 cũng bị xóa
