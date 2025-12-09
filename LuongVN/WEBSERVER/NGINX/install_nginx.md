# NGINX 
## Nginx là gì?
Nginx là 1 phần mềm mã nguồn mở để phục vụ web. Nó sử dụng kiến trúc đơn luồng và được thiết kế để có hiệu suất và độ ổn định tối đa, vì thế nó hiệu quả hơn Apache nếu được cấu hình chính xác. Ngoài khả năng làm web server, nó cũng có thể hoạt động như trình cân bằng tải hay 1 reverse proxy cho các máy chủ HTTP, TCP và UDP

### Chức năng chính
**Máy chủ web (Web server):**
- Nginx có khả năng phục vụ các trang web tĩnh (HTML, CSS, JavaScript, hình ảnh,...) và động (PHP, Python,...) một cách hiệu quả.
- Nó nổi tiếng với khả năng xử lý số lượng lớn kết nối đồng thời mà vẫn duy trì hiệu suất cao.

**Reverse Proxy:**
- Nginx có thể hoạt động như một reverse proxy, nhận các yêu cầu từ máy khách và chuyển tiếp chúng đến các máy chủ ứng dụng (backend servers).
- Điều này giúp cải thiện hiệu suất, bảo mật và khả năng mở rộng của ứng dụng web.

**Load Balancer:**
- Nginx có thể phân phối lưu lượng truy cập đến nhiều máy chủ ứng dụng, giúp cân bằng tải và đảm bảo tính sẵn sàng cao của ứng dụng.

**HTTP cache:**
- Nginx có thể lưu trữ các nội dung web tĩnh trong bộ nhớ cache, giúp giảm tải cho máy chủ ứng dụng và tăng tốc độ tải trang.

### Đặc điểm nổi bật
**Hiệu suất cao:**
- Nginx được thiết kế để xử lý số lượng lớn kết nối đồng thời một cách hiệu quả, đặc biệt là trong các môi trường có lưu lượng truy cập cao.

**Tiêu thụ tài nguyên thấp:**
- Nginx sử dụng ít tài nguyên hệ thống (CPU, RAM) hơn so với một số máy chủ web khác, giúp tiết kiệm chi phí phần cứng.

**Tính ổn định:**
- Nginx được biết đến với tính ổn định và khả năng hoạt động liên tục trong thời gian dài.

**Cấu hình linh hoạt:**
- Nginx cung cấp một hệ thống cấu hình linh hoạt, cho phép người dùng tùy chỉnh để phù hợp với nhu cầu của mình.



## Cài đặt Nginx
