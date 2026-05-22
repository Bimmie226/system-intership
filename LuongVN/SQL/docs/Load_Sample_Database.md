# Load Sample Database into MySQL server
## Bước 1: Tải classimodels database

- Tải file zip chứa database

  ```bash
  wget https://www.mysqltutorial.org/wp-content/uploads/2023/10/mysqlsampledatabase.zip -O sampledatabase.zip
  ```

  ![alt text](../images/install_db_01.png)

- Giải nén file ZIP:

  ```bash
  unzip sampledatabase.zip -d ~/classimodels
  ``` 

  - `-d ~/classicmodels` sẽ giải nén vào thư mục `classicmodels` trong home.


  ![alt text](../images/install_db_02.png)

## Bước 2: Connect to the MySQL server 
- Sử dụng `mysql`

  ```bash
  mysql -u root -p
  ```

  - `mysql`: câu lệnh để bắt đầu MySQL client
  - `-u root`: chỉ định user root để kết nối với MySQL server
  - `-p`: cờ nhắc rằng nhập mk của root 

  ![alt text](../images/load_db_01.png)

## Bước 3: Tạo Database:

```sql
CREATE DATABASE classicmodels;
USE classicmodels
EXIT;
```

![alt text](../images/load_db_02.png)

## Bước 4: Import dữ liệu vào database

![alt text](../images/load_db_03.png)

## Bước 5: Kiểm tra 

![alt text](../images/load_db_04.png)