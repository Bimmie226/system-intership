# PERMISSION
## 1. Tổng quan nhanh
- Mỗi file/ thư mục trên Linux có chủ sở hữu (owner), nhóm (group) và others (người khác).
- Quyền được biểu diễn ở dạng rwx (read, write, execute) cho từng nhóm: owner | group | others.
- Có hai cách thể hiện quyền: ký tự (ví dụ `-rwxr-xr--`) và số bát phân (octal) (ví dụ `754`).

## 2. Ý nghĩa quyền `r`, `w`, `x`
- File:
  - `r`(read): đọc nội dung file.
  - `w`(write): sửa/ghi nội dung file.
  - `x`(execute): thực thi file.
- Directory:
  - `r`: liệt kê tên file (`ls`) trong thư mục (cần `x` để nhìn nội dung file?).
  - `w`: tạo/xóa file trong thư mục.
  - `x`: cho phép "vào" thư mục (search/enter) — cần để truy cập các entry bên trong.

## 3. Hiển thị quyền & thông tin cơ bản
- `ls -l` - hiển thị dạng ký tự:
```bash
$ ls -l file.txt
-rw-r--r-- 1 alice dev 1234 Aug  1 12:00 file.txt
# cột đầu: loại + quyền; sau đó owner, group, kích thước, ngày, tên
```

- `id` - xem user hiện tại và nhóm:
```bash
id bim
# uid=1000(bim) gid=1000(bim) groups=1000(bim),4(adm),1001(dev)
```

## 4. Biểu diễn số (octal) và cách chuyển
- Quy ước: `r=4`, `w=2`, `x=1`. Mỗi nhóm có 1 số bằng tổng:
  - `7 = 4+2+1 = rwx`
  - `6 = 4+2 = rw-`
  - `5 = 4+1 = r-x`
  - `4 = r--`
  - `0 = ---`
- Ví dụ:
  - `-rwxr-xr--` → owner `7`, group `5`, others `4` → octal `754`.
  - `-rw-r--r--` → `644`.

## `chmod` - thay đổi quyền
- Dạng số(octal):
```bash
chmod 755 script.sh   # owner rwx, group r-x, others r-x
chmod 644 file.txt    # owner rw-, group r--, others r--
```

- Dạng ký hiệu(symbolic):
```bash
chmod u+rwx,g+rx,o-rwx file   # u=owner, g=group, o=others, a=all
chmod a+x script.sh          # thêm quyền thực thi cho tất cả
chmod g-w file.txt           # bỏ quyền ghi cho group
```

## `chown`  - thay đổi owner 
```bash
sudo chown bim file.txt          # đổi owner thành bim
sudo chown bim:dev file.txt     # owner = bim, group = dev
sudo chown :dev file.txt           # chỉ đổi group
```