# TẦNG GIAO VẬN
## I. Tổng Quan Về Tầng Giao Vận Trong Internet
- Trong mạng Internet hay mạng TCP/IP có hai giao thức ửo tầng giao vận: `UDP và TCP`.

- **UDP** (User Dâtgram Protocol) cung cấp dịch vụ truyền không tin cậy, không hướng nối và **TCP** (Transmission Control Protocol) cung cấp dịch vụ tin cậy, hướng nối cho ứng dụng.

- Mối quan hệ giữa tầng giao vận và tầng mạng(IP)
  - IP(Internet Protocol) thuộc tầng mạng:
    - Cung cấp dịch vụ truyền dữ liệu giữa các máy tính (host-to-host).
    - Best effort delivery service: cố gắng chuyển dữ liệu nhưng không đảm bảo dữ liệu đến nơi, không đảm bảo đúng thứ tự hay toàn vẹn.
    - Mỗi thiết bị có một địa chỉ IP xác định để định danh.
  - TCP/UDP mở rộng dịch vụ IP:
    - Biến truyền dữ liệu từ mức máy tính (host-to-host) thành mức tiến trình (process-to-process).
    - Thực hiện đơn kênh (multiplexing) và phân kênh (demultiplexing) để nhiều ứng dụng trên cùng một máy tính có thể dùng chung kết nối mạng.
  
## II. Dịch Vụ Dồn Kênh, Phân Kênh