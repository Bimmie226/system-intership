- [TẦNG ỨNG DỤNG](#tầng-ứng-dụng)
  - [I. Giao Thức Tầng Ứng Dụng](#i-giao-thức-tầng-ứng-dụng)
    - [Mô hình Khách hàng/Người phục vụ(Client/Sever)](#mô-hình-khách-hàngngười-phục-vụclientsever)
    - [Truyền thông giữa các tiến trình](#truyền-thông-giữa-các-tiến-trình)
  - [II. Các Yêu Cầu Của Ứng Dụng](#ii-các-yêu-cầu-của-ứng-dụng)
    - [1. Mất mát dữ liệu(Data loss)](#1-mất-mát-dữ-liệudata-loss)
    - [2. Băng Thông(bandwith)](#2-băng-thôngbandwith)
    - [3. Thời Gian(timming)](#3-thời-giantimming)
    - [Các yêu cầu cho một số ứng dụng](#các-yêu-cầu-cho-một-số-ứng-dụng)
  - [III. Dịch Vụ Và Các Giao Thức Giao Vận Internet](#iii-dịch-vụ-và-các-giao-thức-giao-vận-internet)
    - [TCP](#tcp)
      - [Dịch vụ giao vận tin cậy:](#dịch-vụ-giao-vận-tin-cậy)
    - [UDP](#udp)


# TẦNG ỨNG DỤNG
## I. Giao Thức Tầng Ứng Dụng
- Cần phân biệt ứng dụng mạng và giao thức tầng ứng dụng. Giao thức tầng ứng dụng chỉ là một phần(cho dù là phần quan trọng) của ứng dụng mạng.
- Ví dụ:
  - Web - ứng dụng mạng cho phép người dùng lấy các đối tượng từ Web sever bao gồm nhiều thành phần, như tiêu chuẩn định dạng văn bản(HTML), trình duyệt Web(Explorer, chrome), Web sever(Microsoft, google), và giao thức tầng ứng dụng.
  - Giao thức tầng ứng dụng của Web-HTTP(HyperText Transfer Protocol), định nghĩa cách thức chuyển thông điệp giữa Web client và Web sever.
  
- Giao thức tầng ứng dụng định nghĩa cách thức truyền thông điệp giữa các tiến trình ứng dụng chạy trên các thiết bị khác nhau. Xác định:
  - Kiểu thông điệp trao đổi, ví dụ như thông điệp yêu cầu hay thông điệp trả lời.
  - Cú pháp của thông điệp, ví dụ các trường trong thông điệp cũng như cách xác định của chúng.
  - Ý nghĩa của các trường.
  - Quy tắc xác định khi nào và như thế nào tiến trình gửi và trả lời thông điệp.

- Nhiều giao thức tầng ứng dụng được đặc tả trong các RFC. Ví dụ: đặc tả của HTTP là HTTP RFC. Nếu người thiết kế trình duyệt tuân theo các quy tắc của HTTP RFC, trình duyệt sẽ có thể lấy được trang Web từ bất kỳ Web sever nào tuân theo các quy tắc HTTP RFC.

### Mô hình Khách hàng/Người phục vụ(Client/Sever)
- Giao thức ứng dụng mạng chia ra hai phía CLient và Sever.
- Phía client trong thiết bị này liên lạc với phía sever trong thiết bị khác.
  - Ví dụ: 
    - trình duyệt Web là phía client, và Web server là phía sever của HTTP. 
    - Trong ứng dụng thư điện tử, mail sever gửi thư là phía client và mail sever nhận thư là phía sever của SMTP.

### Truyền thông giữa các tiến trình
- Ứng dụng bao gồm hai tiến trình trên hai thiết bị khác nhau và liên lạc với nhau qua mạng.
- Hai tiến trình liên lạc với nhau bằng cách gửi và nhận thông điệp qua `socket` của chúng.
- Socket có thể xem như "cửa" của tiến trình vì tiến trình nhận và gửi thông điệp qua "cửa". 

## II. Các Yêu Cầu Của Ứng Dụng
### 1. Mất mát dữ liệu(Data loss)
- Một số ứng dụng như thư điện tử, truyền file, truy cập từ xa, truyển các đối tượng web, và ứng dụng tài chính đòi hỏi dữ liệu phải được truyền chính xác và đầy đủ, tức là không được mất dữ liệu.
- Tuy nhiên một số ứng dụng như real-time audio/video chấp nhận mất mát dữ liệu. Trong các ứng dụng kiểu này, mất mát dữ liệu có thể gây nên một số nhiễu trong dữ liệu đa phương tiện - nhưng điều này có thể chấp nhận được trong giới hạn nào đó.

### 2. Băng Thông(bandwith)
- Để hoạt động hiệu quả, một số ứng dụng phải truyền dữ liệu với một tốc độ nhất định. Nếu không đủ băng thông cần thiết, ứng dụng cần phải mã hóa âm thanh với tốc độ khác hay phải kết thúc.

### 3. Thời Gian(timming)

### Các yêu cầu cho một số ứng dụng

|Ứng dụng|Mất mát dữ liệu|Băng thông|Thời gian|
|---|---|---|---|
|File transfer|Không|Elastic|không|
|Email|không|Elastic|không|
|Web Documents|Không|Elastic|không|
|Real-time Audio/Video|Chấp nhận mất mát|Audio:Few Kbps - 1 Mb, Video: 10Kb-5Mb|Có: 100s of msec|
|Interactive games|Chấp nhận mất mát|Few kbps-10Kb|Có:100s of msec|

## III. Dịch Vụ Và Các Giao Thức Giao Vận Internet
- Hai giao thức giao vận cho tầng ứng dụng: UDP và TCP.

### TCP
- Đặc trưng của giao thức TCP là hướng kết nối và cung cấp dịch vụ truyền dữ liệu tin cậy.

#### Dịch vụ giao vận tin cậy:
- Tiến trình gửi có thể sử dụng TCP dể truyền dữ liệu chính xác và đúng thứ tự. 
- TCP có cơ chế kiểm soát tắc nghẽn, cơ chế này đáp ứng cho cả Interntet chứ khôngphair cho hai tiến trình truyền thông với nhau.
- Giới hạn tốc độ truyền có thể không thỏa mãn với các ứng dụng audio và video theo thời gian thực, những ứng dụng đòi hỏi phải có một băng thông tối thiểu.
- 1 số dịch vụ mà TCP không cung cấp:
  - TCP không đảm bảo một tốc độ truyền tối thiểu.
  - TCP không đưa ra bất kỳ sự đảm bảo về độ trễ.

### UDP
- UDP là giao thức giao vận khá đơn giản với mô hình phục vụ tối thiểu.
- UDP không có cơ chế kiểm soát tắc nghẽn, vì gậy tiến trình gửi có thể đẩy dữ liệu ra cổng UDP với tốc độ bất kỳ.

|Ứng dụng|Giao thức ứng dụng|Giao thức giao vận|
|---|---|---|
|Thư điện tử|SMTP|TCP|
|Truy cập từ xa|Telnet|TCP|
|Web|HTTP|TCP|
|Truyền file|FTP|TCP|
|Remote File Server|NFS|UDP hoặc TCP|
|Điện thoại Internet|Giao thức riêng|Thường là UDP|
