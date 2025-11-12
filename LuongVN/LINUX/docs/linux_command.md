# Linux command
## 1. Lệnh `man`(manual - hướng dẫn sử dụng)
### 1.1 `man $command`
- Xem thông tin của 1 lệnh nào đó: công dụng, options, ...

  ![images/image.png](../images/image.png)

### 1.2. `man $config_file`
- Xem hướng dẫn các file config. VD: `man sshd_config`

  ![alt text](../images/man_01.png)

### 1.3. `man $daemon`
- Xem thông tin các tiến trình chạy nền. VD: `man sshd`

  ![alt text](../images/man_02.png)

### 1.4. `man -k`
- Hiển thị mô tả ngắn các trang hướng dẫn của từ khóa trong tiêu đề 

  ![alt text](../images/man_03.png)

### 1.5. `whatis`

Xem mô tả trang hướng dẫn của từ sau nó

Ví dụ:

- `whatis mkdir`

  ![images/image copy.png](<../images/image copy.png>)

- `whatis echo`

  ![images/image-1.png](../images/image-1.png)

### 1.6. `whereis`
- Tìm kiếm các file liên quan đến 1 lệnh gồm:
  - File thực thi(binary)
  - file source code
  - file man page

- Ví Dụ: 

  ![alt text](../images/whereis_01.png)

  - `/usr/sbin/sshd` → file thực thi

  - `/usr/share/man/man8/sshd.8.gz` → man page
  
- OPTION:
  - `-b` -> chỉ tìm file binary
  - `-m` -> chỉ tìm file man
  - `-s` -> chỉ tìm source code

## 2. Lệnh `pwd` (Print Working Directory)

- Lệnh `pwd` dùng để hiển thị đường dẫn dến thư mục đang làm việc hiện tại:

  ![alt text](../images/pwd.png)

## 3. Lệnh `cd`(Change Directory)

- Chuyển đổi thư mục làm việc.

  - `cd /home/luongvn/Documents/foder1`: chuyển tới thư mục folder1.
  - `cd`: chuyển về thư mục chính của người dùng.
  - `cd A && ls`: chuyển tới thư mục A và hiện danh sách các file của nó.
  - `cd -`: chuyển về thư mục đang làm việc trước đó.
  - `cd ..`: chuyển về thư mục cha.
  - `cd ~`: Thay đổi thư mục hiện tại về thư mục chính.

## 4. Lệnh `ls`(List)
### 4.1. `ls`

- Hiển thị các tệp tin và thư mục trong thư mục.

  ![alt text](../images/ls.png)

### 4.2. `ls -t`

- Hiển thị các thư mục và file theo thời gian chỉnh sửa.

  ![alt text](../images/ls-t.png)

- Để show ra các file cuối cùng được chỉnh sửa. Thêm `head -(số_file)`

  ![alt text](../images/ls-t_them_head.png)

### 4.3. `ls -1`

- Hiển thị mỗi mục trên 1 dòng

  ![alt text](../images/ls-1.png)

### 4.4. `ls -l`

- Hiển thị tất cả thông tin các mục

  ![alt text](../images/ls-l.png)

- Trong đó:
  - Kí tự đầu tiên: định dạng
    - `-`: file bình thường
    - `d`: thư mục
    - `s`: file socket
    - `l`: link file
  - Trường 1: File permission
  - Trường 2: Số lượng liên kết đến tệp hay thư mục đó
  - Trường 3: Chủ sở hữu của tệp, thư mục
  - Trường 4: Nhóm của tệp, thư mục
  - Trường 5: Kích thước của tệp, thư mục đó(đơn vị: byte)
  - Trường 6: Thời gian sửa đổi cuối cùng
  - Trường 7: Tên của tệp, thư mục

### 4.5. `ls -lh`

- Giống `ls -l` nhưng hiển thị trường 5(kích thước) ở dạng dễ đọc. M là MB, K là KB, G là GB.

  ![alt text](../images/ls-lh.png)

### 4.6. `ls -a`

- Như lệnh `ls` nhưng hiển thị cả những file ẩn. Trong linux, các file có tên bắt đầu bằng dấu chấm được gọi là file ẩn và nó không hiển thị cùng các file bình thường.

  ![alt text](../images/ls-a.png)

### 4.7. `ls -ld`

- Hiển thị thông tin thư mục

  ![alt text](../images/ls-ld.png)

### 4.8. `ls -r`

- Giống `ls` nhưng sắp xếp ngược lại. Có thể kết hợp với option `-l` và `-t` để được kết quả như sau:

  ![alt text](../images/ls-ltr.png)

### 4.9. `ls -F`

- Nếu chỉ cần biết các mục là file hay thư mục ta sử dụng `ls -F`:

  ![alt text](../images/ls-F.png)

- Trong đó: 
  - `/`: Thư mục
  - Nothing: tệp bình thường
  - `*`: Tập tin thực thi
  - `@`: link file

### 4.10. `ls -S`

- Hiển thị danh sách nội dung theo kích thước giảm dần.

  ![alt text](../images/ls-S.png)

## 5. Lệnh `mkdir` (make directory - tạo thư mục)
### 5.1. Một số thông tin
- `mkdir --version`: Hiển thị thông tin phiên bản, giấy phép, tác giả.

  ![alt text](../images/mkdir_01.png)

- `mkdir --help`: các option của `mkdir`

  ![alt text](../images/mkdir_02.png)

### 5.2. `mkdir <tên_thư_mục>`
- Tạo thư mục mới tại thư mục hiên tại
- Có thể tạo nhiều thư mục cùng lúc

  ```bash
  luongvn@dev-server:~$ mkdir folder_1 folder_2 folder_3 ...
  ```

### 5.3. `mkdir -v <tên_thư_mục>`
- Tạo thư mục với hiển thị thông báo

  ![alt text](../images/mkdir_03.png)

### 5.4. `mkdir -p`
- Tạo thư mục kèm thư mục cha khi cần thiết

  ![alt text](../images/mkdir_04.png)

### 5.5. `mkdir -m`
- Tạo thư mục đi kèm với cấp permission 

  ![alt text](../images/mkdir_05.png)

## 6. Lệnh `rmdir`(remove directory - xóa thư mục)
### 6.1. `rmdir + <tên_thư_mục>`
- Xóa thư mục rỗng

  ![alt text](../images/rmdir_06.png)

- Khi dùng lệnh này với thư mục không rỗng sẽ tạo ra lỗi

  ![alt text](../images/rmdir_01.png)

### 6.2. `rmdir -p <ten_thu_muc>`
- Xóa đệ quy cho tới khi gặp thư mục không rỗng

  ![alt text](../images/rmdir_02.png)

  ![alt text](../images/rmdir_03.png)

  ![alt text](../images/rmdir_07.png)

### 6.3. `rmdir -v <ten_thu_muc>`
- Hiển thị thông báo khi xóa lên màn hình

  ![alt text](../images/rmdir_08.png)

## 7. Lệnh `file`

- Cú pháp:

  ```bash
  file [OPTION] [file_name]
  ```

- Lệnh `file` được sừ dụng để xác định loại tệp

  ![alt text](../images/file_01.png)

- Lệnh `file` sử dụng tệp `magic` nằm ở `/usr/share/file/magic` chứa các mẫu để nhận dạng các loại tệp. 

### 7.1. `file -b: brief` - tóm tắt
- Hiển thị kiểu file 1 cách ngắn gọn dễ hiểu

  ![alt text](../images/file_02.png)

### 7.2. `file *`
- Hiển thị tất cả các file trong thư mục đang đứng

  ![alt text](../images/file_03.png)

- Hiển thị tất cả các loại file trong thư mục nào đó

  ![alt text](../images/file_04.png)

### 7.3. `file [range]*`
- Hiển thị kiểu file của các file trong khoảng nào đó

  ![alt text](../images/file_05.png)

### 7.4. `file -s`
- Hiển thị các loại tệp của tệp đặc biệt như các tệp trong `/dev`

  ![alt text](../images/file_06.png)

### 7.5. `file -f -`
- Kiểm tra kiểu file của nhiều file. Mỗi file gõ trên 1 dòng

  ![alt text](../images/file_07.png)

### 7.6. `file <file_name_1> <file_name_2> ...`
- Hiển thị loại tệp của nhiều tệp

  ![alt text](../images/file_08.png)

### 7.7. `file -z <file_nén>`

- Lệnh này sẽ cố gắng nhìn vào bên trong file nén

  ![alt text](../images/file_09.png)

## 8. Lệnh `touch`
- Là 1 cách đơn giản để tạo 1 file trống hoặc thay đổi thời gian (timestamps) của file
- timestamps của file:
  - accesstime
  - modifytime
  - changetime

### 8.1. Tạo file trống
- Tạo 1 file:
  
  ```bash
  touch <filename>
  ```

  ![alt text](../images/touch_01.png)

- Tạo nhiều file:

  ```bash
  touch <filename_1> <filename_2> ...
  ```

  ![alt text](../images/touch_02.png)

### 8.2. `touch -a <file_name>`
- Thay đổi thời gian lần cuối truy cập vào file bằng thời gian hiện tại

  ![alt text](../images/touch_03.png)

- `touch -m`: thay đổi thời gian sửa đổi(modifytime)

### 8.3. `touch -c <file_name>`
- Khi dùng option này với 1 file chưa có sẵn -> không tạo file mới 
- Dùng để thay đổi tất cả timestamps thành thời gian hiện tại

  ![alt text](../images/touch_04.png)

### 8.4. `touch -t YYYYMMDDHHMM <file_name>`

- Tạo 1 tệp tin với thời gian được chỉ định sẵn
- Có thể dùng để thay đổi thời gian của 1 tệp có sẵn

  ![alt text](../images/touch_05.png)

## 9. Lệnh `rm` - remove
- Dùng để xóa file hoặc thư mục

### 9.1. `rm <file_name>`

  ![alt text](../images/rm_01.png)

- Xóa nhiều file cùng lúc:

  ```bash
  rm <filename_1> <filename_2> ...
  ```

### 9.2. `rm -i`
- Xóa file hiện xác nhận trước khi xóa

  ![alt text](../images/rm_02.png)

### 9.3. `rm -f`
- Xóa file không xác nhận

  ![alt text](../images/rm_03.png)

### 9.4. `rm -I file*`
- Xóa hàng loạt file có tên gần giống nhau

  ![alt text](../images/rm_04.png)

### 9.5. `rm -d <folder_name>`
- Xóa thư mục rỗng
- Nếu thư mục không rỗng ta không thể xóa!!

  ![alt text](../images/rm_05.png)

### 9.6. `rm -r <folder_name>`
- Nếu gặp thư mục, sẽ xóa tất cả file và thư mục con bên trong nó, rồi xóa luôn chính thư mục đó.

  ![alt text](../images/rm_06.png)

### 9.7. `rm -v`
- Hiển thị thông báo khi xóa

  ![alt text](../images/rm_07.png)

## 10. Lệnh `cp`
- Dùng để sao chép file hoặc thư mục

### 10.1. Copy nội dung 1 file vào 1 file khác

- Sao chép nội dung 1 file vào 1 file khác. Nếu file đích đó chưa tồn tại thì sẽ tạo ra file đó với nội dung giống hệt file nguồn.

  ```bash
  $ cp <file_nguồn> <file_đích>
  ```

  ![alt text](../images/cp_01.png)

### 10.2. Copy file vào thư mục khác

  ```bash
  $ cp <file_1> <file_2> ... <thư mục đích>
  ```

  ![alt text](../images/cp_02.png)

### 10.3. `cp -r/-R <thư_mục_nguồn> <thư_mục_đích>`
- Copy 1 thư mục vào thư mục khác, `-r: recursion`

  ![alt text](../images/cp_03.png)

### 10.4. `cp -i`
- `-i: interactive`

- Hỏi người dùng có muốn ghi đè không khi mà có 1 file có tên trùng với file đích 

  ![alt text](../images/cp_04.png)

### 10.5. `cp -b`
- `-b: backup`
- Tạo bản sao lưu cho 1 file trong cùng thư mục, nếu tên của bản sao lưu trùng với tên 1 file nào đó nó sẽ tự động thêm `~` vào cuối tên file

  ![alt text](../images/cp_05.png)

### 10.6. `cp -f`
- `-f: force`: ép buộc
- Khi hệ thống không thể mở tệp đích để thực hiện thao tác ghi vì người dùng không có quyền ghi cho tệp này thì ta sử dụng tùy chọn `-f`. Khi này, tệp đích sẽ bị xóa trước rồi sau đó copy nội dung từ tệp nguồn tới tệp đích. Nó thay đổi luôn cả quyền của tệp đích.

  ![alt text](../images/cp_06.png)

### 10.7. `cp -p`
- `-p: preserve`: bảo quản
- Khi sử dụng `-p`, lệnh cp sẽ bảo toàn các đặc điểm sau của tệp nguồn: timestamp, quyền sở hữu (owner, chỉ khi nó có quyền) và permission.

  ![alt text](../images/cp_07.png)

### 10.8. `cp -n`
- `-n: no clobber`: 
- không ghi đè lên tệp đã có sẵn

  ![alt text](../images/cp_08.png)

### 10.9. `cp -v`
- `-v: verbose`
- Hiển thị thông báo quá trình

  ![alt text](../images/cp_09.png)

## 11. Lệnh `mv`
- `mv - move(rename) file`: được sử dụng để di chuyển 1 hoặc nhiều tệp hoặc thư mục từ nơi này sang nơi khác
- Nó có 2 chức năng riêng biệt:
  - Đổi tên file hoặc thư mục
  - Di chuyển 1 nhóm các tệp tin vào thư mục khác.

### 11.1. Đổi tên file, thư mục

```bash
$ mv <old_name> <new_name> 
```

![alt text](../images/mv_01.png)

### 11.2. `mv -i`
- `-i: interactive`: tương tác
- Xác nhận di chuyển và ghi đè lên 1 tệp tin có sẵn

  ![alt text](../images/mv_02.png)

### 11.3. `mv -f`
- `-f: force`: ép buộc
- Khi dùng lệnh này để ghi đè với các file không có quyền ghi lên. `-f` sẽ cho ta ghi đè lên tệp mới và xóa tệp ban đầu

  ![alt text](../images/mv_03.png)


### 11.4 `mv -n`
- `-n: no clobber`: không cho ghi đè lên 1 tệp có sẵn

  ![alt text](../images/mv_04.png)


### 11.5. `mv -b`
- `-b: backup`: tạo 1 bản sao lưu tệp tin sẽ bị ghi đè

  ![alt text](../images/mv_05.png)

### 11.6. Di chuyển tệp tin, thư mục
- Chuyển tệp tin tới 1 thư mục khác

  ![alt text](../images/mv_06.png)

- Chuyển thư mục tới thư mục khác

  ![alt text](../images/mv_07.png)

## 12. Lệnh `rename`

- Thường dùng để đổi tên hàng loạt các file có tên cấu trúc gần giống nhau.

  ```bash
  $ rename [OPTION] expression replacement file...
  ```

### 12.1. Đổi tên nhiều file 

- Đổi đuôi tệp:

  ![alt text](../images/rename_01.png)

- Đổi chữ hoa/thường:

  ![alt text](../images/rename_02.png)

### 12.2. `rename -v`
- `-v: verbose`: hiển thị quá trình

  ![alt text](../images/rename_03.png)

## 13. Lệnh `head`
- Dùng để in phần đầu của tệp tin 

### 13.1. `head <file_name>`
- Mặc định in ra 10 dòng đầu file

  ![alt text](../images/head_01.png)

- Có thể dùng cho nhiều file 

  ![alt text](../images/head_02.png)

### 13.2. `head -n number`
- `-n: number`: in ra số dòng theo yêu cầu!!

  ![alt text](../images/head_03.png)

### 13.3. `head -c number`
- In ra `number` byte đầu tiên!!
- Mỗi kí tự = 1 byte, dòng mới = 1 byte

  ![alt text](../images/head_04.png)

### 13.4. `head -q`
- `-q: quiet --silent`: Khi in ra nhiều tệp cùng lúc không có dòng tên tệp hiện ra

  ![alt text](../images/head_05.png)

### 13.5. `head -v`
- `-v: verbose`: luôn in ra tên tệp khi in ra

  ![alt text](../images/head_06.png)

### 13.6. Ứng dụng của `head`
- Khi ta muốn in ra những dòng giữa của file. Ví dụ từ `k -> o` của file `list.txt`

  ![alt text](../images/head_07.png)

- Khi ta sử dụng các lệnh có thông tin in ra màn hình ta có thể dùng `|` sau đó kết hợp `head` hoặc 1 số lệnh khác để in ra thông tin mình muốn!!

  ![alt text](../images/head_08.png)

## 14. Lệnh `tail`
- In những dòng cuối cùng của file

### 14.1. `tail <file_name>`
- Mặc định in 10 dòng cuối của file

  ![alt text](../images/tail_01.png)

- Áp dụng với nhiều file

  ![alt text](../images/tail_02.png)

### 14.2. `tail -n number`
- In ra số dòng xác định cuối cùng của file

  ![alt text](../images/tail_03.png)

- Có thể không cần kí tự `n`:

  ![alt text](../images/tail_04.png)

- Hoặc dùng `+` để in từ dòng `number` đến cuối file:

  ![alt text](../images/tail_05.png)

### 14.3. `tail -c number`
- In ra số byte cuối cùng của tệp

  ![alt text](../images/tail_06.png)

- Dùng `+` để bỏ qua `number` byte đầu tiên:

  ![alt text](../images/tail_07.png)

### 14.4. `tail -q`

- Không in kèm theo tên file. Sử dụng khi áp dụng với nhiều file

  ![alt text](../images/tail_08.png)

### 14.5. `tail -f`
- `-f: follow`: dùng để theo dõi sự thay đổi của file(thường là file log)
- Tùy chọn này sẽ in ra 10 dòng cuối cùng của tệp và cập nhật liên tục

  ![alt text](../images/tail_09.png)

### 14.6. `tail -v`
- In ra luôn đi kèm tên file

  ![alt text](../images/tail_10.png)

## 15. Lệnh `cat`
- `cat: concatenate`: nối tiếp
- Lệnh này dùng để tạo, xem, nối nội dung cac file với nhau

  ![alt text](../images/cat_01.png)

### 15.1. `cat file_name_1 file_name_2 ...`
- Xem nội dung của 1 tệp:

  ![alt text](../images/cat_02.png)

- Nối nội dung của nhiều tệp và in ra màn hình:

  ![alt text](../images/cat_03.png)

### 15.2. `cat -n file_name`
- `-n: number`
- Xem nội dung của file và đánh số dòng

  ![alt text](../images/cat_04.png)

- Nhiều file:

  ![alt text](../images/cat_05.png)

### 15.3. `cat > new_file`
- Tạo file:

  ![alt text](../images/cat_06.png)

### 15.4. `cat file_nguồn > file_đích`
- Sao chép file:

  ![alt text](../images/cat_07.png)

### 15.5. `cat -s`
- `-s: squeeze-blank`: bỏ những dòng trôgns ở đầu file

  ![alt text](../images/cat_08.png)

### 15.6. `cat file1 >> file2`
- Nối nội dung `file1` vào cuối `file2`

  ![alt text](../images/cat_09.png)

### 15.7. `cat -E file`
- `-E: show ends`: Thêm kí tự `$` vào cuối mỗi dòng

  ![alt text](../images/cat_10.png)

## 16. Lệnh `tac`
- Dùng để nối và in nội dung file ngược lại. Ngược với lệnh `cat`

  ![alt text](../images/tac_01.png)

### 16.1. `tac file1 file2`
- Nối ngược nhiều tệp rồi in ra

  ![alt text](../images/tac_02.png)

### 16.2. `tac -b file_name`
- `-b: before`: Tạo dòng trắng để ngăn cách trước mỗi file

  ![alt text](../images/tac_03.png)

### 16.3. `tac -r`
- `-r: regex`: Lệnh này cho phép sử dụng regex

  ![alt text](../images/tac_04.png)

### 16.4. `tac -s string`
- `-s: seperator`: cho phép chỉ định ký tự hoặc chuỗi phân tách giữa các bản ghi thay vì theo từng dòng mặc định

- Ví dụ:
  - Đảo ngược theo dấu `.`:

    ![alt text](../images/tac_05.png)

  - Đảo ngược theo chuỗi dài hơn:

    ![alt text](../images/tac_06.png)

## 17. Lệnh `more` và `less`
### 17.1. Lệnh `more`
- Dùng để xem các tệp lớn trong 1 màn hình, có thể cuộn chuột để xem
- Dùng phím Enter để xem tiếp các dòng.
- Ở đây ta xem file `data.log`

  ```bash
  $ more /var/log/syslog
  ```

  ![alt text](../images/more_01.png)

- `-p`: Xóa màn hình rồi hiển thị nội dung của file
- `+/<string>`: Tìm kiếm trong file và hiển thị ra

  ![alt text](../images/more_02.png)

- `+number`: hiển thị từ dòng `number` của file

  ![alt text](../images/more_03.png)

- Dùng để đọc đầu ra với nội dung dài:

  ```bash
  $ cat filename | more
  ```

### 17.2. Lệnh `less`
- Truy cập từng trang của file tài liệu dài:
  - `less -N`: đánh số dòng

    ![alt text](../images/less_01.png)

  - `less -p "string"`: Tìm vị trí có `string`

    ```bash
    $ dmesg | less -p "disable"
    ```

    ![alt text](../images/less_02.png)

## 18. Lệnh `strings`
- In ra các chuỗi kí tự có thể in trong tệp. Hiển thị các chuỗi ASCII có thể đọc được trong file nhị phân.

- Ví dụ xem file nhị phân của lệnh ls:

  ![alt text](../images/strings_01.png)

### 18.1. `strings -f`
- Hiển thị tên file trước mỗi dòng

  ![alt text](../images/strings_02.png)

## 19. Lệnh `echo`
- Dùng để hiện thị dòng văn bản được truyền vào. Nó được sử dụng chủ yếu trong các tập lệnh shell hay xuất văn bản ra màn hình hoặc tạo file.

### 19.1. `echo <string>`
- In ra màn hình chuỗi `string`

  ![alt text](../images/echo_01.png)

### 19.2. `echo -e \(mini_option)`
- `-e: escape` cho phép ta xác định sự liên tục của văn bản đầu vào

#### 19.2.1. `\b`
- `b: backspace`: Xóa 1 kí tự trước nó

  ![alt text](../images/echo_02.png)

#### 19.2.2. `\c`
- Ngắt văn bản và không xuống dòng

  ![alt text](../images/echo_03.png)

#### 19.2.3. `\n`
- `n: new line`: Xuống dòng

  ![alt text](../images/echo_04.png)

#### 19.2.4. `\t`
- `t: tab`: Tạo khoảng dấu tab

  ![alt text](../images/echo_05.png)

#### 19.2.5. `\r`
- Trả về văn bản sau nó

  ![alt text](../images/echo_06.png)

#### 19.2.6. `\v`
- `v: vertical tab`: tab đầu dòng

  ![alt text](../images/echo_07.png)

### 19.3. `echo *`
- Giống như lệnh `ls`

  ![alt text](../images/echo_08.png)

### 19.4. `echo -n`
- Ngăn không xuống dòng. Con trỏ sẽ ở vị trí cuối văn bản.

  ![alt text](../images/echo_09.png)