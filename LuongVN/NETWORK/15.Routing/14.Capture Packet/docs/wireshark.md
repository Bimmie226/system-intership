# WIRESHARK
## Wireshark là gì?
Wireshark là một ứng dụng để bắt (capture), phân tích và xác định các vấn đề liên quan đến network như: gói tin, kết nối chậm, hoặc các truy cập bất thường. Phần mềm này cho phép quản trị viên hiểu sâu hơn các Network Packets đang chạy trên hệ thống để có thể xác định được cácc nguyên nhân chính xác gây ra lỗi.

## Cách sử dụng wireshark
Kích đúp vào 1 giao diện nào đó để xem chi tiết lưu lượng các gói tin trên giao diện đó. 

Ví dụ: ta xem lưu lượng trên giao diện `ens3`:

![alt text](../images/wireshark_01.png)

Sau đó lưu lượng các gói tin qua `ens3` sẽ hiển thị như sau:

![alt text](../images/wireshark_02.png)

Ta thấy giao diện wireshark được hiển thị với 3 phần chính:

**1. Packet list:** Hiển thị các gói tin bắt được trên 1 card mạng, Ở phần này mỗi gói tin là 1 dòng. Các gói tin được đánh số theo thứ tự

![alt text](../images/ws_01.png)

**2. Packet details:** Hiển thị thông tin chi tiết của 1 gói tin được chọn:

![alt text](../images/ws_02.png)

**3. Packet bytes:** Hiện thị dữ liệu thô của gói tin dưới dạng hex hoặc ASCII, giúp xem chi tiết nội dung thực tế, tìm kiếm thông tin nhạy cảm như (mật khẩu) trong các giao thức không mã hóa như (HTTP) 

- Ví dụ trong 1 gói tin HTTP response:

    ![alt text](../images/ws_03.png)

- Ta có thể thấy thông tin về status trả về: `200`, các header, và dữ liệu trả về `hello`

Ta có thể lưu lại lưu lượng hiện tại bằng cách nhấp vào nút đỏ trên thanh công cụ:

![alt text](../images/wireshark_03.png)

Sau đó để lưu, ta chọn vào `file -> save`. Lưu lượng những gói tin này sẽ lưu dưới dạng file `.pcap`

![alt text](../images/wireshark_04.png)

Để xem 1 file có sẵn ta chọn `file -> open` và chọn file `.pcap` 

![alt text](../images/wireshark_05.png)

Ở đây, ta chọn xem file `capture.pcap` đã có sẵn trên máy

![alt text](../images/wireshark_06.png)

## Ý nghĩa về màu của các gói tin trong wireshark

![alt text](../images/color_ws_01.png)

Muốn xem ý nghĩa màu của các gói tin ta làm như sau: `chọn view -> Coloring Rules`

![alt text](../images/color_ws_02.png)

![alt text](../images/color_ws_03.png)


- **Nền đỏ, chữ vàng** - TCP RST / SCTP ABORT

    ![alt text](../images/color_ws_04.png)


    - Kết nối bị đóng cưỡng bức 
- **Nền đen, chữ đỏ cam** - Bad TCP

    ![alt text](../images/color_ws_05.png)

    - `tcp.analysis.flags`: cờ này được bật khi gói TCP thuộc nhóm bất thường

        | Tên nhóm bất thường | Ý nghĩa                                                   |
        | ------------------- | --------------------------------------------------------- |
        | Retransmission      | Gửi lại 1 segment TCP vì không nhận được ACK hoặc timeout |
        | Out of order        | Segmment đến không đúng thứ tự                            |
        | Zero Window         | Server hết buffer, yêu cầu không gửi nữa                  |

    - `!tcp.analysis.window_update`: không phải là window update
    - `!tcp.analysis.keep_alive`: Không phải là tcp keep alive
    - `!tcp.analysis.keep_alive_ack`: không phải là các gói trả lời cho tcp keep alive

    - **Tóm lại:** Chỉ tô màu những gói tin TCP mà wireshark đánh giá là có vấn đề nhưng KHÔNG tô: `window update`, `keep-alive`, `ACK của keep alive`
- **Nền đen, chữ xanh** - ICMP errors

    ![alt text](../images/color_ws_06.png)

    - Destination Unreachable, Time Exceeded
- **Nền đỏ, chữ trắng** - TTL/hop limit thấp

    ![alt text](../images/color_ws_07.png)
    
- **Nền màu da nhạt, chữ đen** - ARP

    ![alt text](../images/color_ws_08.png)

- **Nền màu da đậm, chữ đen** - Routing

    ![alt text](../images/color_ws_09.png)

- **Nền hồng nhạt, chữ đen** - ICMP

    ![alt text](../images/color_ws_10.png)

- **Nền xanh lá nhạt, chữ đen** - HTTP

    ![alt text](../images/color_ws_11.png)

- **Nền tím nhạt, chữ đen** - TCP

    ![alt text](../images/color_ws_12.png)

- **Nền xanh dương nhạt, chữ đen** - UDP

    ![alt text](../images/color_ws_13.png)

- **Không màu** - broadcast

    ![alt text](../images/color_ws_14.png)

- **Nền xám, chữ đen** - TCP SYN/FIN

    ![alt text](../images/color_ws_15.png)


## Sử dụng filter để lọc các gói tin
### Chỉ bắt các gói có IP trùng khớp 
- Bắt các gói tin có source ip là `192.168.70.93`

    ![alt text](../images/wireshark_07.png)

- Bắt các gói tin có dest ip là `192.168.70.93`

    ![alt text](../images/wireshark_08.png)

- Bắt các gói tin có cả source ip là `192.168.70.93` và dest ip là `192.168.0.117`

    ![alt text](../images/wireshark_09.png)

### Chỉ bắt các gói tin có IP khác với 1 IP nào đó
- Bắt các gói tin có source ip khác ip `192.168.70.93`

    ![alt text](../images/wireshark_10.png)


### Chỉ bắt các gói có port hoặc giao thức trùng khớp
- Bắt các gói tin có TCP port là `80` 

    ![alt text](../images/wireshark_11.png)

- Bắt các gói tin dùng `ssh` 

    ![alt text](../images/wireshark_12.png)

- Bắt các gói tin có source port là `80`

    ![alt text](../images/wireshark_13.png)

- Bắt các gói tin có dest port là `80`

    ![alt text](../images/wireshark_14.png)