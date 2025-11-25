# MySQL & MariaDB
## Introduction to databases
- Cơ sở dữ liệu là 1 tập hợp dữ liệu có cấu trúc, trong đó các dữ liệu có mối quan hệ với nhau 
- Trong csdl quan hệ (relational database), dữ liệu được mô hình hóa bằng các bảng(tables) gồm cột và hàng, các bảng có thể liên kết với nhau theo nhiều quan hệ(1-1, 1-n, n-n).
- Do dữ liệu lớn, cần công cụ để xử lý -> đó là vai trò của SQL

## SQL - the language of the relational database
- SQL (Structured Query Language) là ngôn ngữ truy vấn có cấu trúc, được tiêu chuẩn hóa và dùng để truy cập, làm việc với cơ sở dữ liệu.
- SQL bao gồm 3 phần:
  - Data Definition Language(DDL) - Dùng để định nghĩa cấu trúc csdl và các đối tượng như bảng
  - Data Manipulation Language(DML) - Dùng để truy vấn và cập nhật dữ liệu
  - Data Control Language(DCL) - Dùng để cấp quyền truy cập dữ liệu cho người dùng

→ Tóm lại, SQL là ngôn ngữ chuẩn giúp định nghĩa, thao tác và kiểm soát dữ liệu trong cơ sở dữ liệu.

## What is MySQL
- MySQL là hệ quản trị cơ sở dữ liệu mạnh mẽ, mã nguồn mở. Người dùng có thể sử dụng miễn phí và chỉnh sửa mã nguồn để phù hợp với nhu cầu riêng.
- Ưu điểm: MySQL dễ đọc, đa nền tảng(UNIX, Linux, Windows), đáng tin cậy, mở rộng tốt và chạy nhanh

## What is MariaDB
- MariaDB là một hệ quản trị cơ sở dữ liệu mã nguồn mở, được phát triển từ MySQL 
- Ưu điểm: MariaDB tương thích cao với MySQL, hỗ trợ JSON, ảo hóa, và cải tiến trong sao lưu/phục hồi dữ liệu.
- MariaDB cũng chạy được trên nhiều nền tảng (UNIX, Linux, Windows) và thường được dùng như thay thế trực tiếp cho MySQL trong các hệ thống web và máy chủ.

## Different of MySQL và MariaDB
| **Tiêu chí**             | **MySQL**                                                                                     | **MariaDB**                                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Nguồn gốc**            | Được phát triển bởi **Oracle** (sau khi mua lại MySQL AB).                                    | Được tạo ra bởi **Monty Widenius**, nhà sáng lập MySQL, để tiếp tục phát triển mã nguồn mở.                       |
| **Giấy phép**            | Có **phiên bản mã nguồn mở** và **phiên bản thương mại** (bản quyền của Oracle).              | **Hoàn toàn mã nguồn mở**, sử dụng giấy phép **GPL**.                                                             |
| **Hiệu năng**            | Ổn định, phù hợp cho doanh nghiệp lớn, nhưng một số tính năng bị giới hạn trong bản miễn phí. | Thường **nhanh hơn và nhẹ hơn**, tối ưu hiệu năng truy vấn và nhân bản dữ liệu.                                   |
| **Khả năng tương thích** | Là tiêu chuẩn gốc, nhiều phần mềm được thiết kế cho MySQL.                                    | **Tương thích cao** với MySQL (có thể thay thế trực tiếp trong nhiều ứng dụng).                                   |
| **Cộng đồng phát triển** | Do Oracle quản lý – mã nguồn không hoàn toàn mở.                                              | Được **cộng đồng mã nguồn mở hỗ trợ mạnh mẽ** và phát triển độc lập.                                              |

