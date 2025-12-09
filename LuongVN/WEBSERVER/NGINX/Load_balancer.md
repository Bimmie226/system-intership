# Load Balancer
## Cân bằng tải là gì?
Cân bằng tải là cơ chế phân phối đều lưu lượng truy cập đến nhiều máy chủ để ứng dụng hoạt động nhanh, ổn định và phục vụ được số lượng lớn người dùng cùng lúc. Bộ cân bằng tải đứng giữa người dùng và các máy chủ, điều phối yêu cầu sao cho không máy nào bị quá tải và toàn hệ thống vận hành hiệu quả.

## Cần bằng tải có lợi ích gì?
Cân bằng tải giúp điều phối lưu lượng mạng giữa nhiều máy chủ để ứng dụng hoạt động ổn định, mở rộng tốt và an toàn hơn. Các lợi ích chính gồm:

1. Tăng mức độ sẵn sàng:

   - Tự động phát hiện máy chủ gặp lỗi và chuyển lưu lượng sang máy chủ khác.
   - Giúp bảo trì hoặc nâng cấp hệ thống mà không gây gián đoạn cho người dùng.
   - Hỗ trợ chuyển sang máy chủ / địa điểm dự phòng khi xảy ra sự cố lớn

2. Cải thiện khả năng mở rộng 

    - Phân phối yêu cầu hợp lý, tránh tình trạng một máy chủ bị quá tải
    - Cho phép thêm hoặc bớt máy chủ theo nhu cầu thực tế của lưu lượng
    - Tăng tính dự phòng 

3. Tăng cường bảo mật

    - Bảo vệ trước tấn công DDoS bằng cách phân tán hoặc lọc lưu lượng bất thường.
    - Giám sát và chặn lưu lượng độc hại trước khi đến máy chủ ứng dụng.
    - Kết hợp với tường lửa để tạo thêm một lớp bảo vệ.

4. Cải thiện hiệu năng ứng dụng

    - Phân phối tải đều giúp máy chủ xử lý nhanh hơn và ổn định hơn.
    - Chuyển yêu cầu của người dùng đến máy chủ gần nhất nhằm giảm độ trễ.

## Cân bằng tải hoạt động như thế nào
Các công ty thường để ứng dụng chạy trên nhiều máy chủ. Việc sắp xếp máy chủ như vậy được gọi là cụm máy chủ. Trước tiên, yêu cầu của người dùng gửi tới ứng dụng sẽ đi đến bộ cân bằng tải. Sau đó, bộ cân bằng tải định tuyến từng yêu cầu tới một máy chủ duy nhất, phù hợp nhất trong cụm máy chủ để xử lý yêu cầu.

![alt text](../images/lb_01.png)

## Thuật toán cân bằng tải là gì?
Thuật toán cân bằng tải là một tập hợp các quy tắc mà bộ cân bằng tải tuân theo để xác định máy chủ phù hợp nhất cho từng yêu cầu của máy khách khác nhau. Các thuật toán cân bằng tải gồm có hai loại chính.

### Cân bằng tải tĩnh
Các thuật toán cân bằng tải tĩnh tuân theo những **quy tắc cố định** và **độc lập với trạng thái** máy chủ hiện tại.

#### Phương thức round-robin (luân chuyển vòng)
DNS trả về IP của các máy chủ theo vòng lặp. Mỗi khi có yêu cầu mới, client sẽ nhận một IP khác trong cụm máy chủ, nhờ đó lưu lượng được phân bố luân phiên mà không cần thiết bị cân bằng tải chuyện dụng 

#### Weighted Round Robin
Giống Round Robin nhưng mỗi máy chủ được gán một trọng số. Máy chủ có trọng số cao hơn sẽ nhận nhiều lưu lượng hơn, phù hợp với các máy mạnh hoặc ưu tiên cao.

#### IP Hashing
Bộ cân bằng tải tính hàm băm từ địa chỉ IP của client, rồi ánh xạ kết quả đến một máy chủ cụ thể. Điều này giúp mỗi client luôn được chuyển đến cùng một máy chủ, hữu ích cho các phiên (session) cố định.

### Cân bằng tải động
Thuật toán cân bằng tải động xem xét trạng thái hiện tại của từng máy chủ trước khi phân phối lưu lượng, giúp hệ thống phản ứng linh hoạt hơn với tải thực tế.

#### Least Connection
Gửi yêu cầu đến máy chủ có ít kết nối đang hoạt động nhất. Phù hợp khi số lượng kết nối phản ánh mức tải của máy chủ.

#### Weighted Least Connection
Tương tự Least Connection nhưng mỗi máy chủ được gán trọng số. Máy chủ mạnh có thể xử lý nhiều kết nối hơn và sẽ nhận nhiều yêu cầu tương ứng.

#### Least Response Time
Cân nhắc cả thời gian phản hồi và số kết nối. Máy chủ phản hồi nhanh hơn và ít tải hơn sẽ được ưu tiên, giúp tăng tốc độ phục vụ người dùng.

#### Resource-based Methods
Tác nhân (agent) trên mỗi máy chủ theo dõi tài nguyên như CPU, RAM,… Bộ cân bằng tải sẽ gửi yêu cầu đến máy chủ còn nhiều tài nguyên trống nhất, đảm bảo phân bổ tối ưu theo hiệu năng thực tế.

## Các loại bộ cân bằng tải
Bộ cân bằng tải có thể được phân loại dựa trên yếu tố mà nó kiểm tra trong yêu cầu của khách hàng khi điều hướng lưu lượng. Các loại chính gồm:

### Application Load Balancing
Cân bằng tải ở tầng ứng dụng, dựa vào nội dung yêu cầu (HTTP header, URL, SSL session ID…).
- Dùng cho ứng dụng phức tạp có nhiều cụm máy chủ cho từng chức năng.
- Ví dụ: yêu cầu xem sản phẩm được gửi đến cụm chứa hình ảnh/video; yêu cầu giỏ hàng được gửi đến cụm cần giữ kết nối lâu hơn.

### Network Load Balancing
Cân bằng tải ở tầng mạng, dựa trên IP và thông tin kết nối.
- Có thể gán 1 IP tĩnh cho nhiều máy chủ
- Sử dụng các thuật toán cân bằng tải tĩnh và động để phân phối yêu cầu

### Global Server Load Balancing (GSLB)
Cân bằng tải giữa nhiều cụm máy chủ đặt ở các vị trí địa lý khác nhau.
- Định tuyến yêu cầu đến máy chủ gần người dùng nhất để giảm độ trễ.

- Nếu một khu vực gặp sự cố, lưu lượng được chuyển sang khu vực khác.

### DNS Load Balancing
Cân bằng tải bằng cách cấu hình DNS để trả về nhiều IP khác nhau cho một tên miền.

