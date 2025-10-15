# CÂU HỎI

Khi lên trình duyệt, truy cập `google.com` thì flow chi tiết qua các giao thức là như nào? Có những giao thức nào được sử dụng?

# Flow 

## 1. Thiết bị gửi yêu cầu(PC / lap top / điện thoại) 
- Thiết bị có IP Private `192.168.1.10/24`.
- DNS server: `8.8.8.8`

Khi gõ `google.com`, trình duyệt:
- Kiểm tra DNS cache cục bộ.
- Nếu không có, gửi gói DNS đến DNS server(Source IP: `192.168.1.10`, Dest IP: `8.8.8.8`).

## 2. Router NAT nhận gói tin DNS

Router làm:
- NAT đổi Source IP từ `192.168.1.10` thành IP Public của router(ví dụ `123.45.67.89`).
- Gửi ra ngoài Internet.

-> Gói tin DNS ra Internet với IP nguồn public.

DNS server(8.8.8.8) trả về IP của Google(ví dụ `142.250.66.206`).

Router nhận gói trả lời, nhìn bảng NAT, chuyển Dest IP từ `123.45.67.89` về `192.168.1.10` rồi gửi vào LAN.

## 3. Thiết lập kết nối TCP tới google

Bây giờ PC đã biết IP của Google `142.250.66.206`.

Nó gửi gói TCP SYN đến server của Google:
- Source IP: 192.168.1.10, Source Port: 50234
- Dest IP: 142.250.66.206, Dest Port: 80

Router nhận được:
- NAT đổi Source IP `192.168.1.10:50234` -> `123.45.67.79:40000` (một port random trên IP Public).
- Gửi ra Internet.

Google nhận gói tin:
- Thấy Source IP là `123.45.67.89:40000`.
- Trả SYN-ACK về IP đó.

Router nhận SYN-ACK:
- Nhìn bảng NAT, biết đó là mapping cho `192.168.1.10:50234`.
- Đổi Dest IP về `192.168.1.10`, Dest Port về `50234`.
- Gửi gói SYN-ACK vào LAN.

PC nhận SYN-ACK, gửi ACK -> TCP handshake hoàn tất.

## 4. Gửi yêu cầu HTTP

Bây giờ kênh TCP sẵn sàng.

PC gửi gói HTTP GET:
- Source IP: 192.168.1.10, Source Port: 50234.
- Router NAT đổi thành 123.45.67.89:40000.

Google nhận được, xử lý, trả về nộ dung HTML:
- Dest IP: 123.45.67.89:40000.
- Router nhận được, tra bảng NAT, đổi thành 192.168.1.10:50234.
- PC nhận dữ liệu, giải mã nội dung HTML.

Trình duyệt render trang Google.

# Quá trình data trong TCP/IP

|Tầng|Client|Server|
|---|---|---|
|Application(HTTP)|Trình duyệt gửi HTTP GET / tới `google.com` port 80|Web server Google nhận HTTP /, chuyển cho ứng dụng xử lý trang chủ.|
|Transport(TCP)|Client tạo kết nối TCP tới IP google(Trước khi ra Internet, router NAT sẽ đổi source port và IP thành IP public)|Server google nhận SYN từ IP public, trả SYN-ACK về IP public đó, sau đó nhận ACK và thiết lập kết nối.|
|Internet(IP)|Gắn source IP private(192.168.x.x) và dest IP google(142.250.x.x) -> gửi ra router. Router NAT đổi source IP thành IP public|Nhận IP packet có IP = IP google và source IP = IP public người gửi. Bóc IP header, đưa TCP segment lên Transport.|
|Network Access|Đóng frame: MAC nguồn = MAC PC, MAC đích = MAC router. Router bóc, đổi IP/port, rồi đóng khung mới để gửi ra Internet.|Server Google nhận khung Ethernet (MAC đích = MAC server), bóc MAC header lấy IP packet.|