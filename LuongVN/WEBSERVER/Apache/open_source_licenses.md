# Các Loại Giấy Phép Mã Nguồn Mở Và Quyền Đi Kèm
## I. Tổng quan về giấy phép mã nguồn mở (Open Source Licenses)
Giấy phép mã nguồn mở là các điều khoản pháp lý cho phép người dùng xem, sửa đổi, phân phối lại mã nguồn của 1 phần mềm.

Tùy từng giấy phép, mức độ tự do có thể khác nhau:
- **Permissive** (tự do, ít hạn chế)
- **Copyleft** (hạn chế mạnh, yêu cầu mã kế thừa phải mở)
- **Weak Copyleft** (mở nhưng chỉ áp dụng cho một phần)

## II. Bố cục của giấy phép
### 1. Tiêu đề (Title)
Tên của giấy phép, phiên bản, năm pháp hành

**Ví dụ:** Apache License Version 2.0, January 2004

### 2. Phần tuyên bố bản quyền (Copyright Notice)
**Bao gồm:**
- Ai là chủ sở hữu bản quyền
- Năm sở hữu
  
**Ví dụ:** `Copyright (c) <year> <owner>`

### 3. Phần cấp quyền (Grant of Permission / Grant of License)
Phần này mô tả rõ người dùng được phép làm gì:
- Sử dụng(use)
- Sao chép(copy)
- Sửa đổi(modify)
- Phân phối(distribute)
- Sử dụng thương mại
- Cấp lại giấy phép(sublicense)

### 4. Điều kiện và giới hạn (Conditions & Limitations)
Gồm các nghĩa vụ khi sử dụng mã nguồn, như: 
- Giữ lại thông báo bản quyền
- Ghi rõ các thay đổi
- Mã dẫn xuất phải mở
- Không được dùng tên tác giả để quảng bá
- Điều kiện đóng góp

### 5. Miễn trừ trách nhiệm (Disclaimer of Warranty)
Luôn có trong OSS license

Thường ghi rằng:

> "Phần mềm được cung cấp **không có bất kỳ bảo đảm nào**, người dùng tự chịu rủi ro."

### 6. Giới hạn trách nhiệm (Limitation of Liability)
Giúp tác giả trách bị kiện

Thường ghi:

> “Tác giả không chịu trách nhiệm cho bất kỳ thiệt hại nào gây ra bởi việc sử dụng phần mềm.”


### 7. Điều khoản bằng sách chế (Patent Clause) (nếu có)
Bao gồm:
- Quyền dùng bằng sáng chế liên quan đến mã

- Điều khoản thu hồi nếu kiện tụng

### 8. Điều khoản phân phối (Redistribution Terms)
Xác định khi nào được phép:
- Đóng gói lại
- Phát hành lại
- Đóng mã hay mở mã

### 9. Điều khoản đóng góp (Contributor License Agreement - CLA)
Một số giấy phép quy định:
- Nếu bạn đóng góp mã, bạn đồng ý cấp quyền bản quyền & quyền sáng chế cho người quản lý dự án. Apache License có phần này.

### 10. Điều khoản chấm dứt hiệu lực (Termination)
Chỉ ra khi nào giấy phép hết hiệu lực:

**Ví dụ:**
- Vi phạm điều khoản → giấy phép tự động chấm dứt
- Apache có điều khoản thu hồi vì kiện bằng sáng chế

## III. Cách áp dụng giấy phép
Thêm đường link tới website chứa giấy phép vào các file thông báo với nội dung:

**Ví dụ:** Apache license 2.0

```
Copyright [yyyy] [owner]

Licensed under the Apache License, Version 2.0 (the “License”);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
```

## IV. Các loại giấy phép trên thị trường
### 1. Apache License 2.0
Phiên bản 2.0 của Apache license, được ASF phê duyệt vào năm 2004

**Quyền sử dụng:**
- Được phép dùng, sao chép, sửa đổi, phân phối
- Được đóng gói vào phần mềm đóng
- Được nhận quyền bằng sách chế

**Giới hạn:**
- Phải giữ lại LICENSE + NOTICE
- Phải thông báo rõ ràng khi thay đổi mã
- Không được dùng tên tác giả dưới dạng thương mại
- Không có bảo hành
- Không kiện về bằng sáng chế (nếu kiện -> mất quyền)
- Nếu bạn bán bản phân phối kèm: hỗ trợ kỹ thuật, bảo hành, cam kết chịu trách nhiệm. Bạn phải tự chịu toàn bộ trách nhiệm, không được đổ lên Contributor

### 2. MIT License
MIT là một trong những giấy phép tự do nhất, không ràng buộc nhiều

**Quyền sử dụng:**

MIT License cho phép người dùng gần như mọi quyền, bao gồm:
- Được dùng phần mềm cho mọi mục đích
- Được sao chép lại nguyên bản
- Được sửa đổi, bổ sung, viết lại mã nguồn
- Được gộp vào phần mềm khác (kể cả phần mềm thương mại, đóng nguồn)
- Được phân phối lại bản gốc hoặc bản sửa đổi
- Được bán phần mềm hoặc cung cấp dịch vụ dựa trên phần mềm
- Được cấp lại giấy phép (sublicense) nếu muốn

**Giới hạn:**

- Phải giữ nguyên dòng copyright và thông báo permission notice trong tất cả các bản phân phối (gốc hoặc đã sửa). Đây là điều kiện **DUY NHẤT** bắt buộc.

### 3. GPL (GNU General Public License)
Hiện có 2 phiên bản được sử dụng phổ biến là `GPL-2.0` và `GPL-3.0`

**Quyền sử dụng:**
- Được sao chép và phân phối chương trình, được yêu cầu trả phí cho việc phân phối đó
- Được thay đổi chương trình để sử dụng cho mục đích cá nhân
- Được phân phối bản đã được thay đổi 

**Giới hạn:**
- Khi sao chép và phân phối chương trình, phải đính kèm các thông báo về bản quyền gốc và không bảo hành
- Khi phân phối bản đã được thay đổi bởi bản thân, phải chú thích rõ đó là bản đã được thay đổi, các thành phần được thay đổi, và áp dụng giấy phép GNU cho bản đã được thay đổi đó.
- Khi phát hành chương trình phải công khai mã nguồn của chương trình, đồng thời phải công bố mã nguồn của chương trình trong tối thiểu 3 năm mà không được đòi một khoản phí nào từ những người yêu cầu mã nguồn trừ chi phí vận chuyển hay tương đương.

### 4. LGPL (Lesser GPL) 
LGPL thường được áp dụng cho thư viện, để chúng có thể được dùng trong phần mềm đóng nguồn mà không buộc toàn bộ phần mềm phải mở mã nguồn.

**Quyền sử dụng:**

LGPL cho phép:
- Dùng thư viện trong phần mềm mở hoặc đóng
- Sao chép, phân phối bản gốc hoặc bản sửa đổi
- Sửa đổi mã nguồn của thư viện
- Phân phối bản sửa đổi của thư viện dưới LGPL
- Kết hợp thư viện LGPL với mã nguồn khác, kể cả mã nguồn đóng, miễn là vẫn giữ LGPL
- Tính phí cho bản phân phối hoặc dịch vụ hỗ trợ 

**Giới hạn:**
- Bạn chỉ cần mở nguồn những phần thuộc về thư viện LGPL, không phải mở toàn bộ chương trình.
- Cho phép người dùng thay thế hoặc sửa đổi thư viện
- Khi phân phối lại thư viện đã sửa đổi: Phải mở toàn bộ mã nguồn thay đổi, Phải giữ lại license gốc, Phải chú thích rõ phần đã chỉnh sửa
- Không có bảo hành

### 5. BSD License(2-Clause / 3-Clause)
**Quyền sử dụng:**

BSD (cả 2 và 3 điều khoản) cho phép:

- Dùng phần mềm cho mục đích cá nhân hoặc thương mại

- Sao chép và phân phối lại

- Sửa đổi mã nguồn

- Dùng trong phần mềm đóng nguồn

- Tạo bản quyền sở hữu (proprietary) từ bản sửa đổi

- Bán lại hoặc phân phối lại

> Bạn có thể làm bất kỳ điều gì, miễn là giữ lại thông báo bản quyền.


**Giới hạn(BSD 2-Clause):**

BSD 2-Clause chỉ có hai yêu cầu:

1. Phải giữ nguyên thông báo bản quyền trong source code

2. Phải giữ nguyên disclaimer “NO WARRANTY” khi phân phối binary hoặc source

Không cần phải mở mã nguồn.

Không cần công khai thay đổi.

Không cấm sử dụng thương mại.

Không yêu cầu NOTICE.

**Giới hạn (BSD 3-Clause) – thêm 1 hạn chế so với 2-Clause**

BSD 3-Clause có thêm điều khoản thứ ba:

3. Không được dùng tên tác giả hoặc tổ chức để quảng cáo cho sản phẩm (no endorsement clause)

### 6. Mozilla Public License 2.0
Là một giấy phép phần mềm tự do của Quỹ Mozilla.

Nó ra đời để giúp phân phối trình duyệt web Mozilla. MPL yêu cầu việc công bố mã nguồn của mọi thay đổi được đưa ra công chúng. Thời gian yêu cầu để công bố được giới hạn trong vòng khoảng 6 tháng đến 1 năm tuỳ theo từng trường hợp

### BẢNG: YÊU CẦU CÔNG KHAI MÃ NGUỒN KHI SỬ DỤNG / SỬA ĐỔI

| Giấy phép          | Khi **sử dụng** (chỉ dùng hoặc liên kết)                                           | Khi **sửa đổi** (thay đổi mã nguồn)                                                         |
| ------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **MIT**            | **Không** cần công khai mã nguồn                                                   | **Không** cần công khai mã nguồn (chỉ cần giữ copyright + license)                          |
| **BSD 2-Clause**   | **Không** cần công khai                                                            | **Không** cần công khai                                                                     |
| **BSD 3-Clause**   | **Không** cần công khai                                                            | **Không** cần công khai                                                                     |
| **Apache 2.0**     | **Không** cần công khai                                                            | **Không** cần công khai (nhưng **phải** giữ LICENSE + NOTICE và ghi rõ thay đổi)            |
| **LGPL 2.1 / 3.0** | **Không** cần công khai toàn bộ mã                                                 | **PHẢI** công khai mã nguồn của **thư viện đã sửa** (**không** bắt buộc công khai ứng dụng) |  |
| **GPL 2.0 / 3.0**  | **Phải** công khai **nếu phân phối sản phẩm có bao gồm mã GPL** (vì copyleft mạnh) | **Phải** công khai toàn bộ mã nguồn của phần mềm dẫn xuất                                   |
| **MPL 2.0**        | **Không** cần công khai khi chỉ sử dụng                                            | **Phải** công khai **chỉ những file đã sửa** (copyleft file-level)                          |
