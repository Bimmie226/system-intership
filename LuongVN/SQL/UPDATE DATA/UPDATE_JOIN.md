# MySQL UPDATE JOIN
## Introduction
- Dùng JOIN trong câu lệnh UPDATE để cập nhật dữ liệu của 1 bảng dựa trên giá trị từ bảng khác
- Cú pháp:

  ```sql
  UPDATE T1
  [INNER JOIN | LEFT JOIN] T2 ON T1.C1 = T2.C1
  SET T1.C2 = T2.C2,
      T2.C3 = expr
  WHERE condition;
  ```

- Ta có thể viết UPDATE JOIN theo 2 cách:f
  
  - Cách 1:

    ```sql
    UPDATE T1
    INNER JOIN T2 ON T1.C1 = T2.C1
    SET T1.C2 = T2.C2, 
        T2.C3 = expr
    WHERE T1.C4 = 'something';
    ```

  - Cách 2:

    ```sql
    UPDATE T1, T2
    SET T1.C2 = T2.C2,
        T2.C3 = expr
    WHERE T1.C1 = T2.C1 AND
          T1.C4 = 'something';
    ```