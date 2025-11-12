# APACHE WEB SERVER
## Introduction to Apache
### Installing on Debian
- Ban đầu ta chưa tải apache server vì chưa thấy xuất hiện thư mục `/var/www` trong hệ thống

  ![alt text](../images/apache_01.png)

- Sử dụng `apt` để tải về hệ thống ubuntu

  ![alt text](../images/apache_02.png)

- Sau khi cài đặt xong ta kiểm tra `/var/www`

  ![alt text](../images/apache_03.png)

  - Trong đây chứa file `idex.html` trang mặc định bạn thấy khi truy cập `http://localhost` hoặc IP của máy.

- Kiểm tra apache đã cài chưa:

  ![alt text](../images/apache_04.png)

  → tất cả các gói cần thiết của Apache đã được cài đặt thành công (ii nghĩa là installed and ok).


### Installing on RHEL
- Kiểm tra apache có cài chưa:

  ![alt text](../images/apache_05.png)

  - `rpm -q`: query RPM database
  
- Cài đặt apache trên Rocky

  ```bash
  [luongvn@localhost ~]$ sudo yum install httpd
  ```

- Kiểm tra lại:
  
  ![alt text](../images/apache_06.png)

  → Apache đã được cài đặt thành công.

- Thư mục mặc định của apache tren rocky:

  ![alt text](../images/apache_07.png)

### Running apache on Debian

- Cách khởi động apache2 trên ubuntu:

  ![alt text](../images/apache_8.png)

- Để xác nhận rằng đã khởi động apache dùng `service apache2 status` hoặc `ps`

  ![alt text](../images/apache_09.png)

  ![alt text](../images/apache_10.png)

- Hoặc sử dụng `wget` và `file` để xác minh rằng máy chủ web của bạn phục vụ một tài liệu html

  ![alt text](../images/apache_11.png)

### Running apache on Rocky
- Khởi chạy httpd trên Rocky bằng lệnh `service`

  ![alt text](../images/apache_12.png)

- Để xác nhận lại apache đã chạy, dùng `service httpd status` hoặc `ps`

  ![alt text](../images/apache_13.png)

  ![alt text](../images/apache_14.png)

### Index file on Rocky
- Rocky không cung cấp tệp `index.html` hoặc `index.php` chuẩn. Việc sử dụng wget đơn giản sẽ gặp lỗi.

  ![alt text](../images/apache_15.png)

- Bất kỳ tệp `index.html` tùy chỉnh nào trong `/var/www/html` sẽ ngay lập tức được sử dụng làm trang chỉ mục cho máy chủ web này.

  ![alt text](../images/apache_16.png)

### Default website
- Thay đổi trang web mặc định của một máy chủ web Apache vừa cài đặt là rất dễ dàng. Tất cả những gì bạn cần làm là tạo (hoặc thay đổi) một tệp index.html trong thư mục DocumentRoot
- Để xác định vị trí thư mục DocumentRoot trên Debian:

  ![alt text](../images/apache_17.png)

  -> `/var/www/html` là trang web mặc định

- Trên Rocky:

  ![alt text](../images/apche_18.png)


- RHEL không có trang web mặc định. Nhưng một tệp `index.html` được tạo trong `/var/www/html/` sẽ tự động được sử dụng làm trang mặc định

### Apache Configuration

- Tất cả tệp cấu hình trong RHEL được thực hiện trong `/etc/httpd`

  ![alt text](../images/apache_19.png)

- Ở ubuntu nằm ở: `/etc/apache2`

  ![alt text](../images/apache_20.png)

## Port Virtual Hosts on Debian
### Default virtual host
- Debian có một tệp cấu hình virtualhost cho trang web mặc định của nó trong `/etc/apache2/sites-available/default`.

  ![alt text](../images/apache_21.png)

- Nếu muốn chạy nhiều website trên cùng 1 IP nhưng không có tên miền khác nhau, ta có thể gán mỗi website một port riêng.
- Ví dụ:

  | Website       | Port | DocumentRoot         |
  | ------------- | ---- | -------------------- |
  | Choo Choo     | 7000 | /var/www/choochoo    |
  | Chess Club 42 | 8000 | /var/www/chessclub42 |
  | hunter2       | 9000 | /var/www/hunter2     |

- File cấu hình virtualhost:
  - Các file cấu hình virtualhost trên ubuntu cần kết thúc bằng `.conf`

    ```bash
    /etc/apache2/sites-available/choochoo.conf
    /etc/apache2/sites-available/chessclub42.conf
    /etc/apache2/sites-available/hunter2.conf
    ```
  - Ví dụ:

    ![alt text](../images/apache_22.png)

    - `*:7000`: apache lắng nghe port 7000 cho website này
    - `DocumentRoot`: thư mục chứa file web của website đó
    - `ServerAdmin`: email quản trị viên(không bắt buộc)

- Cho phép Apache lắng nghe trên các cổng mới:
  - Apache mặc định chỉ lắng nghe `80/443`, nên bạn cần chỉnh file `/etc/apache2/ports.conf`:
  - Sau đó restart Apache:

    ```bash
    sudo systemctl restart apache2
    ```

- Tạo 3 thư mục DocumentRoot và thêm 1 số trang web đơn giản vào thư mục đó

  ```bash
  mkdir /var/www/choochoo
  mkdir /var/www/chessclub42
  mkdir /var/www/hunter2
  ```

  ![alt text](../images/apache_23.png)

- Sau khi tạo file kích hoạt website bằng lệnh:

  ```bash
  sudo a2ensite choochoo.conf
  sudo a2ensite chessclub42.conf
  sudo a2ensite hunter2.conf
  ```

  - `a2ensite` sẽ tạo đường dẫn trong `sites-enabled`

- Sau đó khởi động lại Apache:

  ```bash
  sudo systemctl restart apache2
  ```

  ![alt text](../images/apache_24.png)

- Kiểm tra lại từng website:

  ![alt text](../images/apache_25.png)

## Named Virtual Hosts on Rocky
### Named Virtual Hosts
- Ta muốn truy cập trang web 1 cách dễ dàng hơn bằng các tên: `choochoo.local`, `chessclub42.local` và `hunter2.local`

- Ta tạo 3 virtualhost mới

  ![alt text](../images/apache_26.png)

### Name resolution
- Ta cần một phương pháp nào đó để phân giải tên. Có thể thực hiện với DNS. Cũng có thể nhanh chóng thêm ba tên vào tệp `/etc/hosts`.

  ![alt text](../images/apache_27.png)


### Reload and Verify

  ![alt text](../images/apache_28.png)

## Password Protected Website on Rocky
- Bạn có thể bảo vệ file và thư mục trong website với 1 file `.htaccess` tham chiếu đến 1 file `.htpasswd`.
- Lệnh `htpasswd` có tạo 1 file `.htpasswd` chứa 1 userid và 1 password

  ![alt text](../images/apache_29.png)

  - Tạo user bim kèm pw

  ![alt text](../images/apache_30.png)

  - user mie cũng muốn truy cập, ta có thể thêm vào tệp

- Sau đó ta tạo tệp `.htaccess` ở DocumentRoot của web mà mình muốn bảo vệ

  ![alt text](../images/apache_31.png)

- Vì `choochoo` nằm trong thư mục gốc mặc định của apache là `/var/www/html` nên khi ta muốn dùng file `.htaccess` Apache phải được cho phép sử dụng file đó.
- Quyền này được điều khiển bời dòng `AllowOverride` trong file cấu hình `/etc/httpd/conf/httpd.conf`

  ![alt text](../images/apache_32.png)

- Restart lại dịch vụ và thử lại:

  ![alt text](../images/apache_33.png)

## Aliases and Redirects
- Apache hỗ trợ aliases cho thư mục

  ```bash
  Alias /choochoo/ "/var/www/html/choochoo/"
  ```

- 1 nội dung có thể được chuyển hướng đến 1 trang web hoặc 1 máy chủ web khác

  ```bash
  Redirect permanent /foo http://www.foo.com/bar
  ```

## Self Signed Cert 
- Chuyển website HTTP sang HTTPs
- Để truy cập website qua giao thức HTTPS (tức là `https://<ip-server>`), cần kích hoạt SSL/TLS trên máy chủ web (Apache hoặc Nginx), cài chứng chỉ số SSL, và cấu hình máy chủ sử dụng chứng chỉ đó.

### Lab trên máy ubuntu 
#### Bước 1: Tạo chứng chỉ SSL self-signed(dùng cho nội bộ, không cần mua)
- Cài đặt module SSL cho apache:

  ![alt text](../images/apache_34.png)

- Kích hoạt module ssl:

  ```bash
  sudo a2enmod ssl
  ```

#### Bước 2: Tạo chứng chỉ SSL tự ký

  ![alt text](../images/apache_35.png)

- `-x509`: Tạo chứng chỉ X.509 (chuẩn SSL).
- `-nodes`: Không mã hóa file key.
- `-days 365`: Chứng chỉ có hiệu lực 1 năm.
- `rsa:2048`: Sử dụng khóa RSA 2048-bit
- `-keyout`: Chỉ định đường dẫn lưu tệp tin khóa riêng.
- `-out`: Chỉ định đường dẫn lưu tệp tin chứng chỉ.
- Trong quá trình tạo, có thể thêm thông tin như quốc gia, tỉnh, tổ chức,... hoặc bỏ trống.

#### Bước 3: Tạo file config VirtualHost cho HTTPs
- Tạo file mới:

  ```bash
  sudo vim /etc/apache2/sites-available/lampsite-ssl.conf
  ```

- Gán nội dung:

  ![alt text](../images/apache_36.png)

#### Bước 4: Kích hoạt site HTTPS và khởi động lại Apache

```bash
sudo a2ensite lampsite-ssl.conf
sudo systemctl restart apache2
```

#### Bước 5: Cho phép cổng HTTPS (443) trên firewall
```bash
sudo ufw allow 443
```

#### Bước 6: Truy cập vào website

  ![alt text](../images/apache_37.png)