# Lab các command Chapter 1
## `pwd` - print working directory
### `pwd` -> In ra thư mục hiện tại

![alt text](../images/lpic_1_06.png)


## `cd` - change directory
### `cd ~`, `cd`, `cd $HOME` -> Quay về thư mục home của user hiện tại

![alt text](../images/lpic_1_01.png)

### `cd -` -> Quay lại thư mục trước đó

![alt text](../images/lpic_1_02.png)

Ta thấy khi `cd /var` tức là ta đã đến thư mục `var`, sau đó dùng `cd -` thì đã quay lại được `etc`.

### `cd .` -> Thư mục hiện tại

![alt text](../images/lpic_1_03.png)

Ta thấy ban đầu khi `pwd` ta đang ở `/home/luongvn` dùng lệnh `cd` sau đó kiểm tra đang ở đâu bằng `pwd` thấy vẫn ở `/home/luongvn`

### `cd ..` -> Di chuyển lên thư mục cha

![alt text](../images/lpic_1_04.png)

Ta thấy ban đầu khi `pwd` ta đang ở `/home/luongvn` dùng `cd ..` đã quay trở lại `/home`

### `cd ../..` -> Di chuyển lên 2 cấp thư mục

![alt text](../images/lpic_1_05.png)

Ta thấy ban đầu khi `pwd` ta đang ở `/home/luongvn` dùng `cd ../..` đã về `/`

### `cd + đường dẫn tuyệt đối` -> Di chuyển đến thư mục bằng đường dẫn tuyệt đối

![alt text](../images/lpic_1_07.png)

Ta thấy ở đây ta đã di chuyển được đến `dir1` nhờ đường dẫn tuyệt đối `/home/luongvn/dir1`

### `cd + đường dẫn tương đối` -> Di chuyển đến thư mục bằng đường dẫn tương đối

![alt text](../images/lpic_1_08.png)

Lưu ý: thư mục muốn đến phải nằm trong thư mục đang ở hiện tại nếu không sẽ bị lỗi `No such file or directory`

## `history`
### `history` -> Hiển thị toàn bộ lịch sử lệnh hiện tại

![alt text](../images/lpic_1_09.png)

### `history -c` -> Xóa toàn bộ lịch sử trong phiên hiện tại

![alt text](../images/lpic_1_10.png)

Sau khi xóa ta kiểm tra lại `history` chỉ thấy 1 lệnh duy nhất

### `history -d STT` -> Xóa history với đúng STT đó

![alt text](../images/lpic_1_11.png)

Ta thấy trước khi xóa STT 10 là `cd .` sau khi xóa đã mất `cd .`

### `history N` -> hiển thị N dòng cuối của history

![alt text](../images/lpic_1_12.png)

### Thêm định dạng thời gian vào lịch sử lệnh
- Mặc định không có thời gian cụ thể, để tự động thêm định dạng thời gian vào, cần chỉnh sửa biến `$HISTTIMEFORMAT` trong tệp cấu hình `~/.bashrc` của user.
- Biến `$HISTTIMEFORMAT` xác định định dạng thời gian được sử dụng để hiển thị lịch sử lệnh.

```bash
echo 'export HISTTIMEFORMAT="%F %T | "' >> ~/.bashrc
source ~/.bashrc
```

- `%F` -> Ngày(YYYY-MM-DD)
- `%T` -> Giờ(HH:MM:SS)

![alt text](../images/lpic_1_13.png)

-> Ta đã thấy xuất hiện thời gian 

### `history !!` -> hiển thị câu lệnh gần nhất

![alt text](../images/lpic_1_14.png)

### `history !STT` -> hiển thị câu lệnh theo STT

![alt text](../images/lpic_1_15.png)

### Bỏ qua các lệnh cụ thể
- Có thể chỉ định 1 hoặc nhiều lệnh không bao giờ được ghi vào tệp lịch sử với biến `$HISTIGNORE`

```bash
echo 'export HISTIGNORE="cd *:cd"' >> ~/.bashrc
source ~/.bashrc
```
- `cd` -> khớp với lệnh `cd` trống
- `cd *` -> khớp với mọi lệnh bắt đầu bằng `cd`

![alt text](../images/lpic_1_16.png)

