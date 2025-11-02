# CÀI ĐẠT ROCKY SERVER
## Chuẩn bị:
- Tải file ISO của Rocky Linux 9 từ trang chủ: https://rockylinux.org/download
- Cài đặt VMware trên máy tính

## Tiến hành cài đặt
`CTRL + n` để tạo 1 máy ảo mới

![alt text](../images/rocky_01.png)

Chọn typical và nhấn next

![alt text](../images/rocky_02.png)

Chọn Installer disc image file(iso) và chọn đường dẫn của file iso đã tải trong máy

![alt text](../images/rocky_03.png)

Đặt tên máy ảo và chọn nơi lưu trữ trong máy

![alt text](../images/rocky_04.png)

Đặt dung lượng ổ địa và chọn option `store virtual disk as a single file` - lựa chọn nơi chứa là 1 file duy nhất

Nhấn Customize Hardware... để điều chỉnh cấu hình trước khi tạo.

![alt text](../images/rocky_05.png)

- `Memory`: Tăng bộ nhớ RAM (Ví dụ: 4096 MB hoặc hơn).
- `Processors`: Tăng số lượng nhân CPU (Ví dụ: 2).
- `Network Adapter`: Đảm bảo chọn NAT (để truy cập Internet) hoặc Bridged (tùy vào nhu cầu mạng của bạn).

![alt text](../images/rocky_06.png)

Chọn ngôn ngữ, ví dụ: English

![alt text](../images/rocky_07.png)

Chọn root password để cài mk cho root

Nhấp vào Time & Date.

![alt text](../images/rocky_09.png)

- Chọn khu vực thời gian (ví dụ: Asia/Ho_Chi_Minh).

- Nhấp vào Done (góc trên bên trái).

Nhấp vào Installation Destination để chọn vị trí cài đặt

![alt text](../images/rocky_08.png)

- Chọn custom để cấp phân vùng thủ công

![alt text](../images/rocky_10.png)

- `/boot`: 2GB - Lưu trữ file cấu hình hệ thống

![alt text](../images/rocky_11.png)

- `swap`: 16GB - bộ nhớ ra mạng

![alt text](../images/rocky_12.png)

- `/home`: 30GB

![alt text](../images/rocky_13.png)

- `/`: còn lại 

![alt text](../images/rocky_14.png)

- Nhấn done và chọn Accept change

![alt text](../images/rocky_15.png)

- User Creation: Nhấp vào User Creation, điền Full name và Username, nhập mật khẩu và xác nhận. Tùy chọn đánh dấu Make this user administrator để cấp quyền sudo.

Chọn `Begin installation` để cài đặt

Kiểm tra:

![alt text](../images/rocky_16.png)

