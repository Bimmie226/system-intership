# Cài đặt SSH server trên máy ảo Rocky
## 1. Cài đặt ssh server trên máy ảo
- Cấu hình mạng và ghi lại địa chỉ IP, đảm bảo có thể truy cập Internet từ máy ảo

![alt text](./images/lab_ssh_rocky_01.png)

Ta thấy khi dùng lệnh: `ifconfig` IP của máy ảo là: `192.168.174.135`

Thực hiện ping để kiểm tra kết nối Internet

![alt text](./images/lab_ssh_rocky_02.png)

-> Kết nối Internet thành công

- Cài đặt OpenSSH:
```bash
$sudo yum install openssh-server -y
```

![alt text](./images/lab_ssh_rocky_03.png)

- Khởi động và cho phép SSH tự động thực thi khi khởi động hệ điều hành
```bash
$sudo systemctl start sshd
$sudo systemctl enable sshd
```

- Kiểm tra xem ssh server có đang thực thi hay chưa
```bash
$sudo systemctl status sshd
```

![alt text](./images/lab_ssh_rocky_04.png)

-> Thực thi thành công

## 2. Đăng nhập vào máy ảo Ubuntu và kiểm tra xem có thể kết nối tới ssh server Rocky không?

- Đăng nhập vào máy ảo Ubuntu

![alt text](./images/lab_ssh_rocky_05.png)

- Kết nối tới ssh server Rocky
```bash
ssh luongvn@192.168.174.135
```

![alt text](./images/lab_ssh_rocky_06.png)

- Kiểm tra kết nối của ssh server trên internet

![alt text](./images/lab_ssh_rocky_07.png)