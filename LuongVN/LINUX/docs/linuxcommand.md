# Linux command
## 1. Lệnh `man`(manual - hướng dẫn sử dụng)
### 1.1 `man $command`
- Xem thông tin của 1 lệnh nào đó: công dụng, options, ...

  ![images/image.png](../images/image.png)

### 1.2. `man $config_file`
- Xem hướng dẫn các file config. VD: `man sshd_config`

  ![alt text](../images/man_01.png)

### 1.3. `man $daemon`
- Xem thông tin các tiến trình chạy nền. VD: `man sshd`

  ![alt text](../images/man_02.png)

### 1.4. `man -k`
- Hiển thị mô tả ngắn các trang hướng dẫn của từ khóa trong tiêu đề 

  ![alt text](../images/man_03.png)

### 1.5. `whatis`

Xem mô tả trang hướng dẫn của từ sau nó

Ví dụ:

- `whatis mkdir`

  ![images/image copy.png](<../images/image copy.png>)

- `whatis echo`

  ![images/image-1.png](../images/image-1.png)

### 1.6. `whereis`
- Tìm kiếm các file liên quan đến 1 lệnh gồm:
  - File thực thi(binary)
  - file source code
  - file man page

- Ví Dụ: 

  ![alt text](../images/whereis_01.png)

  - `/usr/sbin/sshd` → file thực thi

  - `/usr/share/man/man8/sshd.8.gz` → man page
  
- OPTION:
  - `-b` -> chỉ tìm file binary
  - `-m` -> chỉ tìm file man
  - `-s` -> chỉ tìm source code

## 2. Lệnh `pwd` (Print Working Directory)

- Lệnh `pwd` dùng để hiển thị đường dẫn dến thư mục đang làm việc hiện tại:

  ![alt text](../images/pwd.png)

## 3. Lệnh `cd`(Change Directory)

- Chuyển đổi thư mục làm việc.

  - `cd /home/luongvn/Documents/foder1`: chuyển tới thư mục folder1.
  - `cd`: chuyển về thư mục chính của người dùng.
  - `cd A && ls`: chuyển tới thư mục A và hiện danh sách các file của nó.
  - `cd -`: chuyển về thư mục đang làm việc trước đó.
  - `cd ..`: chuyển về thư mục cha.
  - `cd ~`: Thay đổi thư mục hiện tại về thư mục chính.

## 4. Lệnh `ls`(List)
### 4.1. `ls`

- Hiển thị các tệp tin và thư mục trong thư mục.

  ![alt text](../images/ls.png)

### 4.2. `ls -t`

- Hiển thị các thư mục và file theo thời gian chỉnh sửa.

  ![alt text](../images/ls-t.png)

- Để show ra các file cuối cùng được chỉnh sửa. Thêm `head -(số_file)`

  ![alt text](../images/ls-t_them_head.png)

### 4.3. `ls -1`

- Hiển thị mỗi mục trên 1 dòng

  ![alt text](../images/ls-1.png)

### 4.4. `ls -l`

- Hiển thị tất cả thông tin các mục

  ![alt text](../images/ls-l.png)

- Trong đó:
  - Kí tự đầu tiên: định dạng
    - `-`: file bình thường
    - `d`: thư mục
    - `s`: file socket
    - `l`: link file
  - Trường 1: File permission
  - Trường 2: Số lượng liên kết đến tệp hay thư mục đó
  - Trường 3: Chủ sở hữu của tệp, thư mục
  - Trường 4: Nhóm của tệp, thư mục
  - Trường 5: Kích thước của tệp, thư mục đó(đơn vị: byte)
  - Trường 6: Thời gian sửa đổi cuối cùng
  - Trường 7: Tên của tệp, thư mục

### 4.5. `ls -lh`

- Giống `ls -l` nhưng hiển thị trường 5(kích thước) ở dạng dễ đọc. M là MB, K là KB, G là GB.

  ![alt text](../images/ls-lh.png)

### 4.6. `ls -a`

- Như lệnh `ls` nhưng hiển thị cả những file ẩn. Trong linux, các file có tên bắt đầu bằng dấu chấm được gọi là file ẩn và nó không hiển thị cùng các file bình thường.

  ![alt text](../images/ls-a.png)

### 4.7. `ls -ld`

- Hiển thị thông tin thư mục

  ![alt text](../images/ls-ld.png)

### 4.8. `ls -r`

- Giống `ls` nhưng sắp xếp ngược lại. Có thể kết hợp với option `-l` và `-t` để được kết quả như sau:

  ![alt text](../images/ls-ltr.png)

### 4.9. `ls -F`

- Nếu chỉ cần biết các mục là file hay thư mục ta sử dụng `ls -F`:

  ![alt text](../images/ls-F.png)

- Trong đó: 
  - `/`: Thư mục
  - Nothing: tệp bình thường
  - `*`: Tập tin thực thi
  - `@`: link file

### 4.10. `ls -S`

- Hiển thị danh sách nội dung theo kích thước giảm dần.

  ![alt text](../images/ls-S.png)

