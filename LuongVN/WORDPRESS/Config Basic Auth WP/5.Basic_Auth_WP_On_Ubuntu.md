# Cấu Hình Basic Auth WordPress Ubuntu
- Ta có thể bảo vệ website với 1 file `.htaccess` tham chiếu đến 1 file `.htpasswd`
- Lệnh `htpasswd` có tạo 1 file `.htpasswd` chứa 1 userid và 1 password

  ```bash
  sudo apt update
  sudo apt install apache2-utils
  sudo htpasswd -c /etc/apache2/.htpasswd bim
  ```

  ![alt text](../images/auth_01.png)

  - Tạo user `bim` đi kèm pw

  ![alt text](../images/auth_02.png)

  - Tạo thêm user `mie` mới
- Sau đó ta tạo tệp `.htaccess` ở DocumentRoot của WP:

  - Mở file site config (mặc định là `000-default.conf` hoặc file riêng nếu bạn đã tạo site mới):

    ```bash
    vi /etc/apache2/sites-available/000-default.conf
    ```

    ![alt text](../images/auth_03.png)

    - `AllowOverride All` → để WordPress .htaccess vẫn hoạt động.

    - `AuthType Basic` + `AuthName` + `AuthUserFile` + `Require valid-user` → bật Basic Auth.
- Bật module Apache và site config:

  ```bash
  sudo a2enmod auth_basic
  sudo a2ensite 000-default
  sudo systemctl restart apache2
  ```

  ![alt text](../images/auth_04.png)

- Kiểm tra lại: Truy cập: `http://ip_address`

  ![alt text](../images/auth_05.png)

  - Nhập `user`: bim, `pw`: 123456 

  ![alt text](../images/auth_06.png)

  - Truy cập thành công