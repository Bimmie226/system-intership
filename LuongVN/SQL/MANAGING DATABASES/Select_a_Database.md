# Selecting a MySQL Database
- Đăng nhập bằng tk root:

  ```bash
  mysql -u root -p
  ```

- Để hiển thị csdl hiện tại:

  ```sql
  SELECT database();
  ```

  ![alt text](../images/select_db_01.png)

- Để chọn 1 CSDL dùng USE:

  ```sql
  USE database_name;
  ```

  ![alt text](../images/select_db_02.png)

- Nếu CSDL không tồn tại, bạn có thể check lại các CSDL trên máy chủ:

  ```sql
  SHOW DATABASES;
  ```

  ![alt text](../images/select_db_03.png)

- Chọn csdl ngay khi đăng nhập:

  ```bash
  mysql -u root -D classicmodels -p
  ```

  ![alt text](../images/select_db_04.png)