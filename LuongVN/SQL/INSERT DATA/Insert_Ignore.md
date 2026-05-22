# MySQL INSERT IGNORE
## Introduction
- Chèn dữ liệu và bỏ qua lỗi — không làm gián đoạn lệnh INSERT

- Khi dùng INSERT bình thường, nếu bất kỳ hàng nào gây lỗi:

  - Toàn bộ câu lệnh bị hủy

  - Không hàng nào được thêm vào

  - MySQL trả về lỗi

- INSERT IGNORE giúp ta tránh điều đó.

- INSERT IGNORE sẽ:
  - Bỏ qua những hàng gây lỗi (duplicate key, data too long, invalid data…)

  - Chỉ chèn những hàng hợp lệ
  - MySQL không trả lỗi → chỉ tạo WARNING
- Cú pháp:

  ```sql
  INSERT IGNORE INTO table_name (column_list)
  VALUES (value_list1),
         (value_list2),
         ...;
  ```