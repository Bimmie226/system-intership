# WEB SERVER
## Webserver là gì?
- Webserver là một hệ thống phần mềm hoặc phần cứng có nhiệm vụ lưu trữ, xử lý và phân phối các nội dung web(như trang HTML, hình ảnh, video, file, ...) đến browser của người dùng thông qua HTTP/HTTPS

## Chức năng của Webserver
- Lưu trữ nội dung web: Tài liệu HTML, CSS, JavaScript, hình ảnh, video, ...
- Phản hồi yêu cầu HTTP/HTTPs: Giao tiếp với trình duyệt người dùng
- Xử lý tập lệnh động(Dynamic Content): Kết hợp với các ngôn ngữ lập trình(PHP, python, java, ...) để xử lý nội dung động
  
## Cách hoạt động của Webserver

  ![alt text](../images/webserver_01.png)

1) Người dùng nhập URL vào trình duyệt. Ví dụ: `https://example.com/index.html`
2) Trình duyệt gửi yêu cầu đến DNS để phân giải tên miền thành địa chỉ IP
3) Trình duyệt sử dụng địa chỉ IP để gửi yêu cầu đến Webserver:
  - Trình duyệt thiết lập kết nối với Webserver qua giao thức HTTP (port 80) hoặc HTTPS (port 443).
  - Yêu cầu gửi đi sẽ chứa các thông tin chính như:

    ```bash
    GET /index.html HTTP/1.1
    Host: example.com
    ```

4) Webserver xử lý yêu cầu:
- Nếu là nội dung tĩnh (HTML, CSS, JS, hình ảnh): Webserver tìm kiếm file và gửi phản hồi.
- Nếu là nội dung động (PHP, Python, Node.js…): Webserver gọi trình thông dịch hoặc chương trình phụ trợ để xử lý.

5) Webserver gửi phản hồi (Response) về trình duyệt:
- Nếu thành công: Trả về mã `200 OK` cùng nội dung trang web.
- Nếu lỗi: Trả về các mã lỗi như `404 Not Found`, `500 Internal Server Error`, ...

6) Trình duyệt hiển thị nội dung cho người dùng

## Phân loại Webserver
1) Static webserver(Máy chủ tĩnh):
- Phục vụ các nội dung cố định (HTML, CSS, JS, hình ảnh).
- Ví dụ: Nginx, Apache.

2) Dynamic webserver(Máy chủ động):
- Kết hợp máy chủ HTTP với phần mềm ứng dụng (PHP, Python, Node.js, ...).
- Ví dụ: Apache + PHP.

## Một số tính năng mở rộng của Webserver
- `Caching`: Tăng tốc bằng cách lưu trữ nội dung tĩnh.
- `Load Balancing`: Cân bằng tải giữa nhiều máy chủ.
- `Virtual Hosting`: Lưu trữ nhiều trang web trên cùng một máy chủ.