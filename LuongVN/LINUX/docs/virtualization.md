# TỔNG QUAN VỀ VIRTUALIZATION VÀ HYPERVISOR
## Virtualization là gì?
- Ảo hóa là từ một máy vật lý đơn lẻ có thể tạo thành nhiều máy độc lập
- Mỗi máy ảo có một hệ điều hành riêng và các ứng dụng riêng

## Tại sao nên sử dụng công nghệ ảo hóa?
- Ảo hóa cho phép chia sẻ CPU, RAM, ổ cứng giữa nhiều máy ảo (VM), tăng hiệu quả sử dụng phần cứng. 
- Giảm số lượng máy chủ vật lý -> giảm điện năng và không gian đặt thiết bị
- Cách ly các ứng dụng, hệ điều hành trên các VM khác nhau -> giảm nguy cơ xâm nhập lan sang toàn bộ hệ thống

## Virtual Machine là gì?
- Máy ảo là một môi trường hoạt động độc lập - phần mềm hoạt động cùng nhưng độc lập với hệ điều hành máy chủ

## Hypervisor/VMM là gì?
- `Hypervisor` - phần mềm giám sát máy ảo: 
  - là 1 chương trình phần mềm quản lý 1 hoặc nhiều máy ảo (VM)
  - Sử dụng để tạo, startup, dừng và reset lại các máy ảo
  - Hypervisor cho phép mỗi VM truy cập vào lớp tài nguyên phần cứng vật lý như CPU, RAM
  - Có thể giới hạn số lượng tài nguyên hệ thống mà mỗi VM có thể sử dụng để đảm bảo nhiều máy ảo sử dụng đồng thời trên 1 hệ thống
- Có 2 loại hypervisor là `Native` và `Hosted`

### Native

  ![alt text](../images/hypervisor_native.png)

- Hypervisor loại native chạy trực tiếp trên phần cứng, nằm giữa phần cứng và các guest OS
- Nó được khởi động trước cả hệ điều hành và tương tác trực tiếp với kernel
- Hiệu suất cao vì không có hệ điều hành nào cạnh tranh tài nguyên máy với nó. Tuy nhiên, hệ thống cũng chỉ được sử dụng để chạy các VM vì hypervisor luôn phải chạy ngầm bên dưới.

### Hosted

  ![alt text](../images/hypervisor_hosted.png)

- Hypervisor loại hosted được cài đặt trên 1 máy host, mà trong đó có 1 hệ điều hành đã được cài đặt.
- Nó chạy như 1 ứng dụng trên máy tính, có thể quản lý và chạy nhiều máy ảo cùng lúc.
- Nó có thể được bật hoặc thoát khi cần để giải phóng tài nguyên cho host. Tuy nhiên, vì chạy trên hệ điều hành nên hiệu suất có thể thấp hơn so với native.

## Ring
- Hierarchical Protection Domains(hay Protection Rings) là cơ chế nhằm bảo vệ dữ liệu của 1 chương trình tránh khỏi nguy cơ bị truy cập trái phép bởi các chương trình khác.
- Môt Protection Ring là 1 mức độ truy cập tài nguyên hệ thống
- Các Ring được sắp xếp có thứ bậc, 0 là đặc quyền nhiều nhất(trusted-software), được đánh số cao nhất là ít đặc quyền nhấy(untrusted-software)

  ![alt text](../images/ring.png)

- Các chương trình hoạt động tại Ring 0 có đặc quyền cao nhất, có thể tương tác trực tiếp với phần cứng CPU, RAM, ...
- Các ứng dụng nằm ở Ring cao muốn truy cập tài nguyên được quản lý bởi Ring thấp hơn phải dùng các cổng `gate` đặc biệt. Ví dụ `system call` giữa các Ring

## Phân loại Virtualization

- Người ta có thể ảo hóa:
  - RAM virtualization
  - CPU virtualization
  - Network virtualization
  - Device I/O virtualization

-> Ta tập trung vào CPU virtualization

## CPU virtualization
- Các loại CPU virtualization:
  - Full virtualization
  - Paravirtualization 
  - Container-based Virtualization
  - Hardware Assisted Virtualization
  - OS level Virtualization
  - Hybrid Virtualization: ( Hardware Virtualized with PV Drivers )

-> Ta tập trung vào `Full virtualization`, `Paravirtualization` và `Hardware Assisted Virtualization`

### Full Virtualization
- Vấn đề: Một số lệnh trong guest OS(như truy cạp I/O, điều khiển ngắt, thay đổi page table, ...) không thể thực hiện trực tiếp vì chúng yêu cầu Ring 0.
- Giải pháp:
  - Hypervisor dùng Binary Translation để xử lý.
- Cụ thể:
  - Guest OS chạy nguyên bản, không biết rằng nó đang bị ảo hóa.
  - Khi gặp lệnh đặc quyền, VMM dùng binary translation để:
    - phát hiện lệnh này trong mã này
    - dịch chúng sang các lệnh an toàn tương đương
    - sau đó thực thi chúng trong môi trường được kiểm soát
- Kết quả:
  - Ứng dụng người dùng chạy bình thường, trực tiếp trong Ring 3
  - Guest OS tưởng rằng nó đang ở Ring 0, nhưng thật ra nó đang làm việc với VMM không phải làm việc với phần cứng, các lệnh đặc thù được VMM xử lý.
  - VMM kiểm soát hoàn toàn phần cứng thật ở Ring 0

### Paravirtualization
- Trong paravirtualization, hypervisor sẽ cung cấp hypercall interface.
- Guest OS sẽ được chỉnh sửa kernel code để thay thế non-virtualizable instruction bằng các hypercall này.
- Do kernel code bị đổi -> không sử dụng được với 1 số hệ điều hành mã nguồn đóng như windows
- Guest OS được chỉnh sửa để nằm ở Ring 0 nhưng nó biết rằng nó đang chạy trong môi trường ảo.
- Thay vì thực thi trực tiếp các lệnh đặc quyền, guest OS gọi trực tiếp hypervisor thông qua các hypercall
- Hypervisor nhận các hypercall này, thực thi các tác vụ đặc quyền

### Hardware Assisted Virtualization
