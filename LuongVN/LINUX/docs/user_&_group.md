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
