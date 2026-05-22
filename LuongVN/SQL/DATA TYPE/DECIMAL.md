# MySQL DECIMAL Data Type
## Introduction
- `DECIMAL` dùng để lưu giá trị số chính xác (exact numeric), đặc biệt là dữ liệu tiền tệ.

- Không giống như `FLOAT/DOUBLE`, `DECIMAL` không gây lỗi làm tròn do dùng lưu trữ dạng `decimal` chứ không phải `floating point`.
- Cú pháp:
  - DECIMAL(P, D)
    - `P (precision)`: tổng số chữ số (1–65)
    - `D (scale)`: số chữ số sau dấu thập phân (0–30), và `D ≤ P`
  - Ví dụ:

    ```sql
    amount DECIMAL(6, 2);
    ```

  - Biến thể:
    - `DECIMAL(P)` = `DECIMAL(P,0)`
    - `DECIMAL` = `DECIMAL(10,0)`

