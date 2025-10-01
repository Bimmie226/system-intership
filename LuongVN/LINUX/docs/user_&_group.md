# USER
Có 2 loại User:

- User hệ thống(thực thi các module, script cần thiết phục vụ cho HĐH).
- User người dùng(login để sử dụng HĐH, gồm `super user` và `regular user`).

## Đặc điểm của user:
- Tên mỗi user là duy nhất, chỉ có thể đặt tên chữ thường, chữ hoa.
- User có username và password.
- Mỗi user có một mã định danh duy nhấy(uid).
- Mỗi user có thể thuộc về nhiều nhóm(gid).
- Tài khoản superuser có uid = gid = 0.

## File /etc/passwd

- Là file chứa thông tin người dùng.

![LINUX/images/user_01.png](../images/user_01.png)

|Cột  |Nội dung|
|---  |---  |
|Cột 1|Tên người sủ dụng|
|Cột 2|Mã liên quan đến mật khẩu cho Unix và `x` đối với Linux. 
||Linux lưu mã này trong một tập tin khác `/etc/shadow` mà chỉ có root mới có quyền đọc|
|Cột 3|user ID|
|Cột 4|group ID|
|Cột 5|Tên mô tả người sử dụng(Comment)|
|Cột 6|Thư mục home của user. Thướng sẽ nằm trong `/home/"tên_tài_khoản"`|
|Cột 7|Shell sẽ hoạt động sau khi user login, thường là `/bin/bash`|

## File /etc/shadow

- File để chứa thông tin về mật khẩu, chỉ có `root` mới đọc được file này.

![LINUX/images/user_01.png](../images/user_02.png)

|Cột  |Nội dung|
|---  |---  |
|Cột 1|tên người dùng|
|Cột 2|mật khẩu đã được mã hóa. Để trống - không có mk, Dấu "*" - tài khoản bị tạm ngưng|
|Cột 3|số ngày kể từ lần cuối đổi mật khẩu(tính từ 1/1/1970)|
|Cột 4|số ngày trước khi có thể thay đổi mật khẩu, giá trị 0 có nghĩa là thay đổi bất cứ lúc nào|
|Cột 5|số ngày mật khẩu có giá trị. 99999 có ý nghĩa mật khẩu có giá trị vô thời hạn|
|Cột 6|số ngày cảnh báo user trước khi mật khẩu hết hạn|
|Cột 7|số ngày sau khi mật khẩu hết hạn và sẽ bị xóa. Thường có giá trị 7(1 tuần)|
|Cột 8|Số ngày kể từ khi tài khoản bị khóa(tính từ 1/1/1970)|

# GROUP
- Nhóm là tập hợp nhiều user. Mỗi nhóm có tên duy nhất, và có một mã định danh duy nhất(gid).
- Khi tạo 1 user (không dùng -g: không chỉ định nhóm user ở) thì mặc định tạo 1 group mới có tên giống với user được tạo ra.

## File /etc/group
- Là file chứa thông tin các group. File này tất cả user đều có thể đọc nhưng chỉ có `root` mới có quyền thay đổi.

![LINUX/images/user_01.png](../images/group_01.png)

|Cột  |Nội dung|
|---  |---  |
|Cột 1|tên nhóm|
|Cột 2|mật khẩu đã được mã hóa. Để trống - không có mk, dấu "*" - tạm ngưng, dấu "x" đc lưu trong file /etc/gshadow|
|Cột 3|mã nhóm(gid)|
|Cột 4|danh sách các user thuộc nhóm|

# Mối quan hệ giữa User và Group trong quản lý quyền
- Quyền sở hữu tệp và thư mục: Mỗi tệp và thư mục trong Linux đều có thông tin về owner(chủ sở hữu) (là một user) và group owner(nhóm sở hữu) (là một group).
- Quyền truy cập: Hệ thống Linux sử dụng ba loại quyền truy cập cơ bản cho mỗi tệp và thư mục, áp dụng cho ba đối tượng:
  - Owner: User sở hữu tệp/thư mục.
  - Group: Group sở hữu tệp/thư mục.
  - Others: Tất cả các user khác không phải là owner và không thuộc group sở hữu.
- Các loại quyền:
  - Read(r): Cho phép xem nội dung của tệp hoặc nội dung của thư mục.
  - Write(w): Cho phép sửa đổi nội dung của tệp hoặc tạo, xóa, đổi tên tệp trong thư mục.
  - Execute(x): Cho phép chạy tệp (nếu là một chương trình) hoặc truy cập vào thư mục (để truy cập các tệp bên trong).

- Lệnh `chmod`: Được sử dụng để thay đổi quyền truy cập của tệp và thư mục.

- Lệnh `chown`: Được sử dụng để thay đổi owner của tệp và thư mục.

- Lệnh `chgrp`: Được sử dụng để thay đổi group owner của tệp và thư mục.

# Các lệnh thực thi
