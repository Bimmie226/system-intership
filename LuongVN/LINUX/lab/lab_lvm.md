# Lab LVM
## 1. Chuẩn bị
- Add thêm 1 số ổ cứng vào máy ảo

  ![alt text](../images/lab_lvm_01.png)

## 2. Tạo Logical Volume trên LVM

`B1`: Kiểm tra các Hard Drives có trên hệ thống

- Bạn có thể kiểm tra xem có những Hard Drives nào trên hệ thống bằng cách sử dụng câu lệnh `lsblk`

  ![alt text](../images/lab_lvm_02.png)

- Trong đó sdb, sdc, sdd, sde là các Hard Drives mà mình mới thêm vào

`B2`: Tạo Partition

- Từ các Hard Drives trên hệ thống, tạo các partition. Ở đây, từ sdb ta tạo các partition bằng cách sử dụng lệnh `gdisk /dev/sdb`

  ![alt text](../images/lab_lvm_03.png)

- Trong đó:
  - `n` : bắt đầu tạo partition
  - `1` : tạo partition 1
  - `first sector(34-20971486, default = 2048)` : mặc định
  - `Last sector(2048-20971486, default = 20971486)` : 1G để partition tạo ra có dung lượng 1G
  - `Hex code = 8e00` : đổi thành LVM
  - `w`: lưu và thoát
- Tương tự ta tạo thêm các partition từ `sdb`

  ![alt text](../images/lab_lvm_04.png)


- Tạo các partition từ `sdc` bằng lệnh `gdisk /dev/sdc`

  ![alt text](../images/lab_lvm_05.png)

`B3`: Tạo Physical Volume

- Tạo các Physical Volume là `/dev/sdb1` và `/dev/sdc` bằng các lệnh sau:

  - `# pvcreate /dev/sdb1`
  - `# pvcreate /dev/sdc1`
- Có thể kiểm tra các Physical Volume bằng lệnh `pvs: Physical Volumes Show` hoặc `pvdisplay`

  ![alt text](../images/lab_lvm_06.png)


`B4`: Tạo Volume Group

- Nhóm các Physical Volume thành 1 Volume Group bằng câu lệnh:

  ```bash
  $ vgcreate vg-demo1 /dev/sdb1 /dev/sdc1
  ```

- Trong đó: `vg-demo1` là tên của Volume Group

- Có thể dùng `vgs: Volume Group Show` hoặc `vgdisplay` để kiểm tra các Volume Group đã tạo

  ![alt text](../images/lab_lvm_07.png)

`B5`: Tạo Logical Volume

- Từ 1 Volume Group, ta có thể tạo các Logical Volume bằng lệnh:

  ```bash
  $ lvcreate -L 1G -n lv-demo1 vg-demo1
  ```

- Trong đó:
  - `-L`: (--size) - chỉ ra dung lượng của Logical Volume
  - `-n`: (--name) - chỉ ra tên của Logical Volume
  - `lv-demo1` là tên của Logical Volume
  - `vg-demo` là Volume Group mình vừa tạo
- **NOTE**: ta có thể tạo nhiều Logical Volume từ 1 Volume Group
- Ta có thể dùng `lvs:Logical Volume Show` hoặc `lvdisplay` để kiểm tra lại các Logical Volume đã tạo

  ![alt text](../images/lab_lvm_08.png)

`B6`: Định dạng Logical Volume

- Để format các Logical Volume thành các định dạng như ext2, ext3, ext4, ta có thể làm như sau:
  ```bash
  $ mkfs -t ext4 /dev/vg-demo1/lv-demo1
  ```

  ![alt text](../images/lab_lvm_09.png)


`B7`: Mount và sử dụng

- Ta tạo 1 thư mục để mount Logical Volume đã tạo vào thư mục đó:

  ```bash
  $ mkdir demo1
  ```

- Tiến hành mount Logical Volume `lv-demo1` vào thư mục `demo1`:

  ```bash
  $ mount /dev/vg-demo1/lv-demo1 demo1
  ```

- Kiểm tra lại dung lượng của thư mục đã được mount: 

  ```bash
  $ df -h 

  # df: disk free, -h: human-readable
  ```

  ![alt text](../images/lab_lvm_10.png)


## 3. Thay đổi dung lượng Logical Volume trên LVM

- Trước khi thay đổi dung lượng, ta cần kiểm tra các thông tin hiện có:

  ```bash
  $ vgs
  $ lvs
  $ pvs
  ```

  ![alt text](../images/lab_lvm_11.png)

- Ta đã tạo được Logical Volume là `lv-demo1`, giả sử Logical Volume này dung lượng đã đầy và chúng ta cần tăng kích thước của nó
- `lv-demo1` thuộc `vg-demo1`, để tăng kích thước, đầu tiên phải kiểm tra xem `vg-demo1` còn dư dung lượng để kéo giãn Logical Volume không?
- **NOTE**: Logical Volume thuộc 1 Volume Group nhất định, Volume Group đã cấp phát hết thì Logical Volume cũng không thể tăng dung lượng được.

- Để kiểm tra: `$ vgdisplay`

  ![alt text](../images/lab_lvm_12.png)

- Volume Group ở đây vẫn còn dung lượng để cấp phát, ta có thể nhận thấy điều này qua 2 trường thông tin là `VG Status  resizeable` và `Free PE / Size  510 / 1.99 GiB` với dung lượng Free là: 510 * 4 = 2040Mb

- Để tăng kích thước Logical Volume ta dùng lệnh:

  ```bash
  $ lvextend -L +50M /dev/vg-demo1/lv-demo1
  ```

- Trong đó:
  - `-L`: (--size) - để tăng kích thước

  ![alt text](../images/lab_lvm_13.png)

- Kiểm tra lại bằng `lvs`:

  ![alt text](../images/lab_lvm_14.png)

- Sau khi tăng kích thước cho Logical Volume thì Logical Volume đã được tăng nhưng filesystem trên volume này vẫn chưa thay đổi, ta phải dùng lệnh sau để thay đổi:

  ```bash
  $ resize2fs /dev/vg-demo1/lv-demo1
  ```

  ![alt text](../images/lab_lvm_15.png)

- Để giảm kích thước của Logical Volume, trước hết ta phải umount Logical Volume mà mình muốn giảm

  ```bash
  $ umount /dev/vg-demo1/lv-demo1
  ```

- Tiến hành giảm kích thước của Logical Volume

  ```bash
  $ lvreduce -L 20M /dev/vg-demo1/lv-demo1
  ```

- Sau đó tiến hành format lại Logical Volume

  ```bash
  mkfs -t ext4 /dev/vg-demo1/lv-demo1
  ```

- Cuối cùng là mount lại Logical Volume

  ```bash
  $ mount /dev/vg-demo1/lv-demo1 demo1
  ```

- Kiểm tra lại:

  ![alt text](../images/lab_lvm_16.png)
  
## 4. Thay đổi dung lượng Volume Group trên LVM
- Ở phần trước ta có thể tăng kích thước của LV nhưng với điều kiện VG đó còn dung lượng. 
- Phần này ta sẽ tìm hiểu làm thế nào có thể mở rộng thêm kích thước của VG cũng như thu hồi dung lượng của nó
- Việc thay đổi VG chính là việc nhóm thêm Physical Volume hay thu hồi Physical Volume ra khỏi VG
- Ta kiểm tra lại các partition và VG

  `$ vgs`

  `$ lsblk`

  ![alt text](../images/lab_lvm_17.png)

- Tiếp theo, thêm 1 partition vào VG:
  ```bash
  vgextend /dev/vg-demo1 /dev/sdb3
  ```

- **NOTE**: Vì muốn nhóm vào VG thì phải là PV nên hệ thống tự động tạo PV sdb3 ta không cần phải `pvcreate` nữa.

  ![alt text](../images/lab_lvm_18.png)

- Ta có thể cắt 1 PV ra khỏi VG như sau:

  ```bash
  $ vgreduce /dev/vg-demo1 /dev/sdb3
  ```

  ![alt text](../images/lab_lvm_19.png)

## 5. Xóa Logical Volume, Volume Group, Physical Volume
### Xóa Logical Volume
- Trước tiên ta phải umount Logical Volume
  
  ```bash
  $ umount /dev/vg-demo1/lv-demo1
  ```

- Sau đó tiến hành xóa Logical Volume bằng lệnh:

  ```bash
  $ lvremove /dev/vg-demo1/lv-demo1
  ```

- Kiểm tra lại:

  ![alt text](../images/lab_lvm_20.png)

### Xóa Volume Group
- Trước khi xóa Volume Group, ta phải xóa Logical Volume
- Xóa Volume Group bằng lênh:

  ```bash
  $ vgremove /dev/vg-demo1
  ```

  ![alt text](../images/lab_lvm_21.png)

### Xóa Physical Volume
- Xóa PV bằng lệnh:
  ```bash
  $ pvremove /dev/sdb3
  ```

  ![alt text](../images/lab_lvm_22.png)