# MySQL INT Data Type
## Introduction
- `INT` trong MySQL dùng để lưu số nguyên (không có phần thập phân): ví dụ `1`, `100`, `-10`.

- Hỗ trợ cả số âm và số dương.

- MySQL cung cấp nhiều loại số nguyên theo kích thước: `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`/`INTEGER`, `BIGINT`.

  | **Type**    | **Bytes** | **Signed (min → max)**   | **Unsigned (min → max)** |
  | ----------- | --------- | ------------------------ | ------------------------ |
  | TINYINT     | 1         | -128 → 127               | 0 → 255                  |
  | SMALLINT    | 2         | -32768 → 32767           | 0 → 65535                |
  | MEDIUMINT   | 3         | -8388608 → 8388607       | 0 → 16777215             |
  | INT/INTEGER | 4         | -2147483648 → 2147483647 | 0 → 4294967295           |
  | BIGINT      | 8         | -9223372036854775808 → … | 0 → 18446744073709551615 |
- Có thể đặt thuộc tính `SIGNED` hoặc `UNSIGNED`

