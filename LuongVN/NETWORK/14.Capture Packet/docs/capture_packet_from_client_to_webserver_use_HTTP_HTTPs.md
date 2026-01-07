# Capture gói tin từ Client đến WebServer dùng HTTP/HTTPs
## HTTP
Dùng filter để lọc các gói tin sử dụng HTTP

![alt text](../images/http_01.png)

Nhấp vào gói `28356` để xem chi tiết về gói HTTP request 

![alt text](../images/http_02.png)

Ở đây, ta nhấp vào `Hypertext Transfer Protocol`:

![alt text](../images/http_03.png)

Ta thấy, đây là 1 gói request với method là `GET`, muốn lấy dữ liệu từ `webcatra.com`

Ta quay lại và xem thử gói response với số thứ tự là `28370`

![alt text](../images/http_04.png)

![alt text](../images/http_05.png)

Ta thấy, gói response này có status là `401` cùng với header `www-Authentication` tức là `webcatra.com` yêu cầu nhập user và password theo đúng basic auth

![alt text](../images/http_06.png)

Quay trở lại gói tin http ta thấy với gói `72182` ta nhấp vào để xem chi tiết gói:

![alt text](../images/http_07.png)

Ở đây ta thấy gói `request` có thêm trường `Authorization` ta nhấp vào để xem thử:

![alt text](../images/http_08.png)

Ta thấy ở đây client đã nhập user: `bimmie` với password: `Bimvungoc23@`. Để biết user và pw này là đúng hay sai ta kiểm tra gói response tiếp theo là gói `72193`

![alt text](../images/http_09.png)


![alt text](../images/http_10.png)

Ta thấy, server vẫn trả về status là `401`, vì vậy với user và pw là `bimmie` và `Bimvungoc23@` không hợp lệ

Ta kiểm tra gói tin tiếp theo `104399`:

![alt text](../images/http_11.png)

Ta thấy trong gói request lần này trong trường authorization đã có password mới: `Bimvungoc23@2005`

![alt text](../images/http_12.png)

Ta kiểm tra gói request trả về xem với password mới này có đúng hay không?

![alt text](../images/http_13.png)

![alt text](../images/http_14.png)

Lúc này mã status đã là `200` tức là password đã đúng

## HTTPs

Để lọc các gói tin sử dụng HTTPs ta filter bằng `tls`

![alt text](../images/https_01.png)

Lúc này ta thấy, các gói tin thể hiện quá trình `client hello` và `server hello`

![alt text](../images/https_02.png)

Sau khi bắt tay xong lúc này client gửi gói tin tuy nhiên khác với HTTP, ở đây các gói tin đã được mã hóa và có thông tin là gói tin `Application Data` 

![alt text](../images/https_03.png)

Khi nhấp vào các gói này, ta thấy thông tin đã được mã hóa hoàn toàn và ta không thể xem được client dùng method `GET`, `POST` hay `PUT`, cũng như không thể thấy server trả về gói có status là `200` hay `404`, user và password cũng được che dấu hoàn toàn

