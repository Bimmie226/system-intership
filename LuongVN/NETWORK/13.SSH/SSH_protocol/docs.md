# SSH - SECURE SHELL 
## I. SSH là gì?
- SSH là 1 giao thức mạng cho phép người dùng thực hiện kết nối giữa máy chủ và máy client 1 cách an toàn và bảo mật

## II. SSH key là gì?
- Là cặp khóa dùng để xác thực khi kết nối SSH giữa client và server, thay cho mật khẩu
- 1 cặp khóa gồm:
  - Private key - giữ trên client, không chia sẻ
  - Public ket - gửi lên server

## III. SSH để làm gì?
- Truy cập và điều khiển máy chủ từ xa: `ssh user@host`
- Truyền file an toàn: SSH cung cấp công cụ để sao chép hoặc đồng bộ file qua mạng 1 cách mã hóa:
  - `scp`(scure copy)
    ```bash
    scp file.txt user@server:/home/user/
    ```
  - `sftp`(secure ftp): giao thức truyền file an toàn bằng ssh

## IV. Cách thức hoạt động của SSH
1) Giai đoạn 1: TCP handshake
- Thiết lập kết nối tcp giữa client và server

2) Giai đoạn 2: Protocol Version Exchange 
- Client và server bắt đầu thương lượng về phiên bản giao thức SSH mà họ sẽ sử dụng và các thuật toán mã hóa, xác thực được hỗ trợ

3) Giai đoạn 3: Key Change
- Tạo ra được `session key`
- Thường dùng các thuật toán trao đổi khóa như Diffie-Hellman(DH)
- Các bước cơ bản (ví dụ sử dụng Diffie-Hellman (DH)):
  - Cả hai bên chọn một cặp số chung: `g` (generator), `p` (số nguyên tố lớn).
  - Mỗi bên chọn một số bí mật: client chọn `a`, server chọn `b`.
  - Tính public value: Client tính `A = g^a mod p`, Server tính `B = g^b mod p`.
  - Client gửi `A` cho server, và server gửi `B` cho client.
  - Client tính `K = B^a mod p`; Server tính `K = A^b mod p`.
  - `Session key = K + random + session ID`.
- Ví dụ:
  - Giả sử `g = 5`, `p = 23`
  - Client chọn `a = 6` → `A = 5^6 mod 23 = 8`
  - Server chọn `b = 15` → `B = 5^15 mod 23 = 2`
  - Client nhận `B = 2` → tính `K = 2^6 mod 23 = 18`
  - Server nhận `A = 8` → tính `K = 8^15 mod 23 = 18`
  - Kết quả: cùng shared secret `K = 18` 

1) Giai đoạn 4: Authentication
- qua trình xác thực giữa client và server nhờ password hoặc cặp khóa SSH key
- Xác thực đúng -> kết nối client và server thành công

## VI. Cách thực hoạt động của SSH key
### 1. Quy trình tạo và sử dụng SSH key
(1) Tạo cặp khóa trên máy client
```bash
ssh-keygen -t rsa -b 4096 -C
```

Kết quả:
- `~/.ssh/id_rsa` -> private key
- `~/.ssh/id_rsa.pub` -> public key

(2) Gửi public key lên server
Chạy lệnh:
```bash
ssh-copy-id user@remote-server
```
- Sao chép nội dung của `~/.ssh/id_rsa.pub`
- Thêm vào file `~/.ssh/authorized_keys` của user trên server.

(3) Khi SSH vào server
```bash
ssh user@host
```

Quy trình xác thực sẽ diễn ra

### 2. Cơ chế xác thực bằng SSH key
- Bước 1: Server gửi challenge
  - Server đọc public key trong `~/.ssh/authorized_keys` 
  - Server tạo một chuỗi ngẫu nhiên (challenge) rồi mã hóa chuỗi này bằng public key.
- Bước 2: Client giải mã challenge
  - Client dùng private key để giải mã chuỗi nhận được
  - Nếu private key hợp lệ -> client có thể giải mã thành công.
- Bước 3: Client gửi lại kết quả cho server
  - Client gửi lại chuỗi đã giải mã cho server
- Bước 4: Server xác minh 
  - Server kiểm tra kết quả có đúng không
  - Nếu đúng -> xác thực thành công
  - Nếu sai -> bị từ chối.