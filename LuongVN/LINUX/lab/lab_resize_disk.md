# Mục lục 

- [Mục lục](#mục-lục)
- [Thực hành resize partition](#thực-hành-resize-partition)
  - [I. Thông số hiện tại](#i-thông-số-hiện-tại)
  - [II. Thực hành](#ii-thực-hành)
    - [2.0 Kiểm tra loại filesystem của `/`](#20-kiểm-tra-loại-filesystem-của-)
    - [2.1 Cài công cụ và mở rộng phân vùng `sda2`](#21-cài-công-cụ-và-mở-rộng-phân-vùng-sda2)
    - [2.2 Mở rộng filesystem - Chỉ chạy lệnh phù hợp với `Type`](#22-mở-rộng-filesystem---chỉ-chạy-lệnh-phù-hợp-với-type)


# Thực hành resize partition 

## I. Thông số hiện tại 

```bash
root@control-01:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           791M  1.2M  790M   1% /run
/dev/sda2        20G  6.8G   12G  37% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           791M  4.0K  791M   1% /run/user/1000
root@control-01:~# lsblk
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda      8:0    0  40G  0 disk
├─sda1   8:1    0   1M  0 part
└─sda2   8:2    0  20G  0 part /
sr0     11:0    1   2G  0 rom
root@control-01:~#
```

- Ổ `/dev/sda` đã có 40GB, nhưng partition `/dev/sda2` chứa `/` mới có 20GB 

## II. Thực hành 

### 2.0 Kiểm tra loại filesystem của `/`

```bash
df -hT / 
```

```bash
root@control-01:~# df -hT /
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda2      ext4   20G  6.8G   12G  37% /
```

- Ở đây Type là `ext4`

### 2.1 Cài công cụ và mở rộng phân vùng `sda2`

```bash
apt update
apt install -y cloud-guest-utils
growpart /dev/sda 2
```

**NOTE:** `/dev/sda` và `2` có khoảng trắng. Lệnh này mở rộng phân vùng số 2 để sử dụng phần trống còn lại trên ổ đĩa. Nếu thành công sẽ có thông báo `CHANGED`

- Kiểm tra: 

```bash
root@control-01:~# lsblk
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda      8:0    0  40G  0 disk
├─sda1   8:1    0   1M  0 part
└─sda2   8:2    0  40G  0 part /
sr0     11:0    1   2G  0 rom
```

### 2.2 Mở rộng filesystem - Chỉ chạy lệnh phù hợp với `Type`

- ext4: 

```bash
resize2fs /dev/sda2
```

- Kiểm tra: 

```bash
root@control-01:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           791M  1.2M  790M   1% /run
/dev/sda2        40G  6.8G   31G  19% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           791M  4.0K  791M   1% /run/user/1000
```