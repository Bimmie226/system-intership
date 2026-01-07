# Capture gói tin TCP và UDP
## TCP
Ở đây ta sẽ tạo 1 gói tin TCP với port là `9999` để lab

![alt text](../images/tcp_01.png)

Ta để ý 3 gói tin đầu tiên có phần info lần lượt là 3 gói tin `SYN`, `SYN-ACK`, `ACK` 

![alt text](../images/tcp_02.png)

Ta chọn gói tin số `19829` để xem kỹ gói tin `SYN`:

![alt text](../images/tcp_03.png)

Ta thấy:
- số `sequence number (raw) = 2034908235` là số mà bên client chọn cho gói `SYN` gửi tới server. 

- Vì là gói SYN nên phần `Acknowledgment Number` sẽ bằng 0 do chưa Ack cái gì

- Trong trường `Flags` chỉ có cờ `SYN` thể hiện đây là gói SYN đầu tiên trong quá trình bắt tay 3 bước 


Tiếp theo ta sẽ xem chi tiết gói tin số `19830` ngay sau gói tin trên:

![alt text](../images/tcp_04.png)

Ta thấy:

- Trường flags lúc này đã bao gồm 2 cờ `SYN, ACK` thể hiện đây là gói SYN, ACK trong quá trình bắt tay 3 bước
- số `Sequence number` server chọn sẽ là: `492230714`
- Số ACK xác nhận gói SYN từ client gửi về là: `2034908236` đúng bằng `2034908235 + 1` tức là bằng số Sequence của client trong gói SYN đã gửi trước đó cộng thêm 1 

Ta quan sát nốt gói tin tiếp theo số `19832`:

![alt text](../images/tcp_05.png)

Ta thấy:

- Trường flags lúc này là cờ `ACK` thể hiện đây là gói ACK trong quá tình bắt tay 3 bước
- Số `Sequence number` lúc này thể hiện byte tiếp theo mà client gửi đi sẽ là `2034908236` đúng bằng `2034908235 + 1` tức là byte trước đó client gửi cho server cộng thêm 1 vì SYN đã chiếm 1 sequence number
- Số ACK xác nhận gói SYN-ACK từ server gửi về là: `492230715` đúng bằng với số sequence của gói SYN-ACK mà server đã gửi trước đó cộng thêm 1. Xác nhận đã nhận được gói SYN-ACK từ client

Từ đó, ta thấy quá trình bắt tay 3 bước đã diễn ra thành công 

## UDP
Ta sẽ tạo 1 gói tin UDP với port `9999` để lab:

![alt text](../images/udp_01.png)

![alt text](../images/udp_02.png)


Ta thấy chỉ có 1 gói tin duy nhất trong quá trình giao tiếp giữa client và server. UDP không tạo handshake, không ACK, gửi là xong -> chỉ 1 gói

