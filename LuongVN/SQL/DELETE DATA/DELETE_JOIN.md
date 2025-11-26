# MySQL DELETE JOIN
- MySQL cho phép xóa dữ liệu từ một hoặc nhiều bảng dựa trên mối quan hệ giữa các bảng bằng INNER JOIN hoặc LEFT JOIN trong câu lệnh DELETE. 

## DELETE JOIN với INNER JOIN
- Cú pháp:

  ```sql
  DELETE T1, T2
  FROM T1
  INNER JOIN T2 ON T1.key = T2.key
  WHERE condition;
  ```
  - Chỉ xóa các hàng có khớp giữa T1 và T2 theo điều kiện JOIN.

  - Có thể xóa một bảng hoặc cả hai bảng cùng lúc.

## DELETE JOIN với LEFT JOIN
- Cú pháp:

  ```sql
  DELETE T1
  FROM T1
  LEFT JOIN T2 ON T1.key = T2.key 
  WHERE T2.key IS NULL;
  ```

  - Xóa các hàng trong bảng trái (T1) mà không có bản ghi tương ứng trong bảng phải (T2).

  - Chỉ liệt kê bảng cần xóa sau DELETE, không xóa cả hai bảng như INNER JOIN.
- Ví dụ:
  - Xóa những khách hàng chưa đặt đơn hàng nào:

    ```sql
    DELETE * 
    FROM customers
    LEFT JOIN orders ON customers.customerNumber = orders.customerNumber
    WHERE orderNumber IS NULL
    ```