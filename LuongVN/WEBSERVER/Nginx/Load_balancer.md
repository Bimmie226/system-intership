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

### Application Load Balancing (ALB)
Aplication Load Balancer(ALB) là một loại load balancer thuộc layer 7 trong mô hình OSI. Nó được thiết kế để phân phối lưu lượng HTTP/HTTPS thông minh hơn. ALB hiểu và phân tích nội dung request(URL, header, cookie, host, ...) rồi phân phối đến server phù hợp.

ALB có thể đọc được:

- Đường dẫn(path-based routing)
- Domain/host(host-based routing)
- Header, query string, cookie

Từ đó nó phân tích và điều hướng request tới backend khác nhau, ví dụ:

| URL                | Backend       |
| ------------------ | ------------- |
| `/api/*`           | API servers   |
| `/images/*`        | Image servers |
| `shop.example.com` | Shop service  |
| `blog.example.com` | Blog service  |

ALB cũng có cơ chế **Health Check** thông minh, ALB gửi request đến backend (ví dụ `/health`) để kiểm tra server nào còn sống, từ đó khi gửi request đến server nó sẽ loại bỏ các server lỗi.

Ngoài ra ALB còn có thể phân tích HTTPs, giải mã SSL ở load balancer để có thể giảm tải công việc cho server backend

### Network Load Balancing (NLB)
Network Load Balancer là loại load balancer layer 4 theo mô hình OSI - tức là hoạt động ở tầng Transport (TCP/UDP). Khác với ALB (layer 7), NLB không đọc nội dung HTTP/HTTPs, chỉ xử lý kết nối mạng thuần túy như: TCP hoặc UDP. 

Như vậy, ta có thể hiểu NLB có nhiệm vụ là proxy TCP/UDP

**Đặc điểm chính của NLB:**

- `Hiệu năng cao`: Vì hoạt động ở Layer thấp hơn, NLB nhanh, nhẹ, latency cực thấp, có thể xử lý hàng triệu connections / second 
- `non-HTTP aware`: NLB không đọc header HTTP, URL, Cookies. Nó chỉ thấy: Source IP/Port, Dest IP/Port, TCP/UDP. Do đó NLB hỗ trợ các service sử dụng TCP/UDP như là: Database (MySQL, MongoDB, ...), SSH, DNS, ...
- `health check`: NLB cũng có health check ở layer 4 thông qua kiểm tra TCP handshake. Nếu server chết -> tự loại bỏ ra khỏi pool
- `SSL Passthrough hoặc Offloading`: NLB xử lý 2 kiểu Passthrough và Offloading. Với Passthrough thì NLB không giải mã SSL còn Offloading thì ngược lại. Default của NLB là passthrough.

- **NOTE:** Đối với các dịch vụ UDP, có thể sử dụng bất kỳ loại health check nào khả dụng (`TCP`, `HTTP` hoặc `HTTPs`), và bất kỳ cổng nào trên target để xác minh tính khả dụng của dịch vụ. Nếu dịch vụ nhận health check thất bại, target sẽ được coi là không khả dụng.

### DNS Load Balancing
DNS Load Balancer là cơ chế cân bằng tải dựa trên DNS, tức là phân tán lưu lượng bằng cách trả về nhiều IP khác nhau cho cùng 1 tên miền

**Ví dụ:**

Khi truy cập: 

```css
api.example.com → có thể trả về IP A, hoặc IP B, hoặc IP C
```

DNS LB hoạt động trước cả Network LB (L4) hay Aplication LB (L7).

DNS LB dùng để phân phối tải giữa nhiều `data center`

```
us.example.com → DC ở Mỹ  
sg.example.com → DC ở Singapore  
jp.example.com → DC ở Nhật
```

Client sẽ được điều hướng về nơi gần nhất. 

**Sơ đồ mô tả DNS Load Balancer:**

```mathematica
                Client
                   |
          DNS Load Balancer
       (Route53 / Cloudflare DNS)
     /        |        |       \
   Region 1 Region 2 Region 3 Region 4
     |         |        |         |
 ALB/NLB    ALB/NLB  ALB/NLB  ALB/NLB
```

**DNS LB** -> chọn region

**NLB/ALB** -> chọn server trong region

Như vậy, DNS Load Balancer là layer đầu tiên trong hệ thống phân phối tải toàn cầu. Nó giúp phân tải theo địa lý, latency, điều hướng user đến data center phù hợp nhất.



## Nguồn tham khảo 

https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html

https://vietnix.vn/load-balancing-la-gi/?utm_source=ggads&utm_medium=pmax&p=&gad_source=1&gad_campaignid=23385187609&gbraid=0AAAAABwedNIQgcgeef3phRxchKazM4EPE&gclid=Cj0KCQiAvOjKBhC9ARIsAFvz5ljl-CdrbVRLbXFRf-jdWe7wK2_kvcFAkBffAjjRVi_SkKA0W36sfKsaArPJEALw_wcB#cac-loai-load-balancer-l4-l7-gslb