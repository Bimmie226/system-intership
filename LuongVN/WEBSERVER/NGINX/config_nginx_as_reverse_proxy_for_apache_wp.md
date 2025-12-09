# Cấu hình Nginx làm reverse proxy cho Apache WordPress
## Mục tiêu
Ta có:
- IP của máy Apache WordPress là: `192.168.70.101`
- IP của máy Nginx là: `192.168.70.93`

Ta sẽ cấu hình máy nginx làm reverse proxy cho máy apache wordpress

## Thực hiện
### Bước 1: Backup file cấu hình
Vì quá trình thực hiện có thể có lỗi dẫn đến bị mất file cấu hình nginx ban đầu, để an toàn ta sẽ backup lại file cấu hình này

```bash
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup
```

Khởi động lại dịch vụ nginx:

```bash
sudo systemctl restart nginx
```

### Bước 2: Tạo file config cho reverse proxy
Khai báo file config nằm trong thư mục `/etc/nginx/sites-available`. 

Ta sẽ tạo file với domain là: `bimmie.com`

```bash
vi /etc/nginx/sites-available/bimmie.com.conf
```

