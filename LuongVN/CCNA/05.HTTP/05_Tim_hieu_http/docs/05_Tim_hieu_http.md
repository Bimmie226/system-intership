- [HTTP(HyperText Transfer Protocol)](#httphypertext-transfer-protocol)
  - [1. Tổng Quan Về HTTP](#1-tổng-quan-về-http)
  - [2. Kết nối liên tục và không liên tục(persistent/nonpersistent)](#2-kết-nối-liên-tục-và-không-liên-tụcpersistentnonpersistent)
    - [2.1. Kết nối không liên tục(nonpersistent)](#21-kết-nối-không-liên-tụcnonpersistent)
    - [2.2. Kết nối liên tục(Persistent Connection)](#22-kết-nối-liên-tụcpersistent-connection)
    - [2.3. Khuôn dạng thông điệp HTTP](#23-khuôn-dạng-thông-điệp-http)
      - [Thông điệp yêu cầu HTTP(HTTTP request message)](#thông-điệp-yêu-cầu-httphtttp-request-message)


# HTTP(HyperText Transfer Protocol)

![alt text](../images/HTTP.png)

## 1. Tổng Quan Về HTTP
- HTTP - giao thức tầng ứng dụng của Web - là trái tim của Web. 
- HTTP được triển khai trên cả hai phía client và server. Các tiến trình client và server trên các hệ thống đầu cuối khác nhau giao tiếp với nhau thông qua việc trao đổi các thông điệp HTTP. 
- HTTP quy định cấu trúc thông điệp cũng như cách thức trao đổi thông điệp giữa client và server.

`Trang Web` (webpage - hay còn gọi là một tập tin) chứa các dối tượng(Object). Đơn giản đối tượng chỉ là một file như HTML, file ảnh,.... Đối tượng được xác định qua địa chỉ URL
- Trang web chứa một file HTML cơ sở và tham chiếu đến các đối tượng khác.
- Ví dụ: 
  - Một trang web chứa 1 file HTML văn bản và 5 đối tượng ảnh JPEG, khi đó trang Web có 6 đối tượng: 1 file văn bản HTML và 5 file ảnh. 
  - File HTML cơ sở này tham chiếu đến các đối tượng khác thông qua địa chỉ URL.
  - Mỗi địa chỉ URL có hai thành phần: tên của máy chủ và vị trí của đối tượng trên máy chủ.
  > URL : www.someschool.edu/somedepartment/picture.gif

  - www.someschool.edu là tên máy chủ và somedepartment/picture.gif là đường dẫn đối tượng.

## 2. Kết nối liên tục và không liên tục(persistent/nonpersistent)
### 2.1. Kết nối không liên tục(nonpersistent)
- Cách hoạt động:
  - Với HTTP/1.0 mặc định, mỗi yêu cầu/response dùng một kết nối TCP riêng.
  - Trình duyệt gửi yêu cầu đến server -> server trả về phản hồi -> TCP connection bị đóng.
  - Nếu trang web có nhiều thành phần(HTML, ảnh, ...) thì trình dueyetj phải tạo một TCP connection mới cho từng thành phần.
- Đặc điểm:
  - Mỗi request/response = 1 connection.
  - Tốn thời gian vì phải thực hiện TCP handshake nhiều lần.
  - Hiệu suất thấp khi tải trang có nhiều tài nguyên.
  - Ít tốn tài nguyên server hơn, vì server không phải giữ kết nối lâu.
- Ví dụ:
  - Một trang web có 5 ảnh -> cần 1 kết nối cho file HTML + 5 kết nối cho ảnh = 6 TCP connections.

### 2.2. Kết nối liên tục(Persistent Connection)
- Cách hoạt động:
  - Được giới thiệu trong HTTP/1.1(và có thể dùng với HTTP/1.0 kèm header `Connection: keep-alive`).
  - Một TCP connection được mở và dùng cho nhiều request/response liên tiếp.
  - Sau khi gửi response, server không đóng kết nối ngay mà giữ nó mở trong một khoảng thời gian(timeout).
- Đặc điểm:
  - Một connection có thể truyền nhiều request/response.
  - Giảm chi phí thiết lập kết nối(TCP handshake và TLS handshake nếu có HTTPS).
  - Tăng tốc độ tải trang web vì có thể tái sử dụng kết nối cho nhiều tài nguyên.
  - Tốn thêm bộ nhớ và tài nguyên server để giữ các kết nối mở.
- Ví dụ:
  - Với trang web có 5 ảnh: chỉ cần 1 TCP connection để tải HTML và 5 ảnh.

### 2.3. Khuôn dạng thông điệp HTTP
Có hai kiểu khuôn dạng HTTP: thông điệp yêu cầu và thông điệp trả lời.

#### Thông điệp yêu cầu HTTP(HTTTP request message)
- Một thông điệp yêu cầu thường có dạng sau:
```pgsql
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
Connection: close
User-agent: Mozilla/4.0
Accept-language: Fr

(extra carry return line feed)
```
Thông điệp gồm các thành phần chính:

a. Dòng yêu cầu(Request line)
- Đây là dòng đầu tiên,, có 3 thành phần:
  1. Method: `GET` -> phương thức truy vấn (có thể là GET, POST, HEAD, PUT, ...).
  2. URL: `somedir/page.html` -> tài nguyên mà client muốn truy cập.
  3. HTTP version: `HTTP/1.1` -> phiên bản giao thức đang dùng.

> Trình duyệt yêu cầu server gửi lại nội dung file `page.html` trong thư mục `somedir`.

b. Các tiêu đề(Header lines)

Các dòng tiếp theo mô tả thêm thông tin cho server:
- Host: www.someschool.edu
  
  -> server nào sẽ xử lý yêu cầu này(bắt buộc trong HTTP/1.1 để phân biết các website chạy chung 1 IP).
- Connection: close

  -> Yêu cầu server đóng kết nối TCP sau khi trả xong phản hồi(tức là non-persistent connection).

- User-Agent: Mozilla/4.0

  -> Trình duyệt/người dùng đang sử dụng loại phần mềm nào(ở đây là Mozilla 4.0).

  Server có thể dựa vào đây để điều chỉnh phản hồi cho phù hợp.

- Accept-Language: Fr

  -> Trình duyệt chấp nhận nội dung phản hồi bằng ngôn ngữ tiếng Pháp.

c. Kết thúc thông điệp
- Thông điệp kết thúc bằng một dòng trống(CRLF - Carriage Return + Line Feed).
- Dòng trống này báo hiệu rằng `headers đã hết`; nếu có phần `message body`(ví dụ khi dùng POST) thì nội dung sẽ nằm sau dòng trống này.

