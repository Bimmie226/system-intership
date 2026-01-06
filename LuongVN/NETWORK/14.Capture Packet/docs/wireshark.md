# WIRESHARK
## Wireshark là gì?
Wireshark là một ứng dụng để bắt (capture), phân tích và xác định các vấn đề liên quan đến network như: gói tin, kết nối chậm, hoặc các truy cập bất thường. Phần mềm này cho phép quản trị viên hiểu sâu hơn các Network Packets đang chạy trên hệ thống để có thể xác định được cácc nguyên nhân chính xác gây ra lỗi.

## Cách sử dụng wireshark
Kích đúp vào 1 giao diện nào đó để xem chi tiết lưu lượng các gói tin trên giao diện đó. 

Ví dụ: ta xem lưu lượng trên giao diện `ens3`:

![alt text](../images/wireshark_01.png)

Sau đó lưu lượng các gói tin qua `ens3` sẽ hiển thị như sau:

![alt text](../images/wireshark_02.png)

Ta có thể lưu lại lưu lượng hiện tại bằng cách nhấp vào nút đỏ trên thanh công cụ:

![alt text](../images/wireshark_03.png)

Sau đó để lưu, ta chọn vào `file -> save`. Lưu lượng những gói tin này sẽ lưu dưới dạng file `.pcap`

![alt text](../images/wireshark_04.png)

Để xem 1 file có sẵn ta chọn `file -> open` và chọn file `.pcap` 

![alt text](../images/wireshark_05.png)

Ở đây, ta chọn xem file `capture.pcap` đã có sẵn trên máy

![alt text](../images/wireshark_06.png)

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