# Ghi chép về Dockerfile 
Dockerfile có thể hình dung như một script dùng để build các image trong container 

Dockerfile bao gồm các câu lệnh liên tiếp nhau được thực hiện tự động trên một image gốc để tạo ra một image mới. Dockerfile giúp đơn giản hóa tiến trình từ lúc bắt đầu đến khi kết thúc 

Trong Dockerfile có các câu lệnh chính sau: 

```dockerfile
FROM 
RUN 
CMD
...
```

## I. Docker Syntax 

```dockerfile
# Comment
INSTRUCTION arguments
```

Các INSTRUCTION là các chỉ thị, được Docker quy định. Khi khai báo, ta phải viết chữ hoa

Các arguments là đoạn nội dung mà chỉ thị sẽ làm gì 

**Ví dụ:**

```dockerfile
# Comment
RUN echo 'This is the first time I'm writting Dockerfile'
```

Ta sẽ đi tìm hiểu các INSTRUCTION

## II. Dockerfile Commands 

### 2.0 FROM 

Dùng để chỉ ra image được build từ đâu (từ image gốc nào)

```dockerfile 
FROM ubuntu

# Có thể chỉ rõ tag của image gốc 

FROM ubuntu:latest
```

### 2.1 RUN 
Dùng để chạy một lệnh nào đó khi build image

```dockerfile
FROM ubuntu
RUN apt update
RUN apt install curl -y
```

### 2.2 CMD 

Chỉ thị `CMD` dùng để truyền một lệnh của Linux mỗi khi thực hiện khởi tạo một container từ image (image này được build từ `Dockerfile`)

Ta có thể sử dụng chỉ thị `CMD` bằng các cách sau: 

```dockerfile
# Cách 1
FROM ubuntu
RUN apt update
RUN apt install curl -y
CMD ["curl", "ipinfo.io"]
```

Hoặc 

```dockerfile
# Cách 2
FROM ubuntu
RUN apt update
RUN apt install curl -y 
CMD curl ifconfig.io
```

### 2.3 LABEL 

**Cú pháp:**

```dockerfile
LABEL <key>=<value> <key>=<value> <key>=<value> ...
```

**Ví dụ:**

```dockerfile 
LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

Để xem các label của image, dùng lệnh `docker image inspect`:

```json
"Labels": {
    "com.example.vendor": "ACME Incorporated"
    "com.example.label-with-value": "foo",
    "version": "1.0",
    "description": "This text illustrates that label-values can span multiple lines.",
    "multi.label1": "value1",
    "multi.label2": "value2",
    "other": "value3"
},
```

### 2.4 MAINTAINER 

**Cú pháp:**

```dockerfile
MAINTAINER <name>
```

Dùng để đặt tên tác giả của image 

Ta cũng có thể sử dụng cách sau để đặt tên tác giả:

```dockerfile 
LABEL maintainer="luongngocvu"
```

### 2.5 EXPOSE 

**Cú pháp:**

```dockerfile
EXPOSE <port> [<port> ...]
```

`EXPOSE` chỉ là mô tả container dự kiến lắng nghe ở port nào.

Nó **KHÔNG**: 
- Tự publish port ra host
- Không mở firewall
- Không bind thật

**Ví dụ:**

Dockerfile: 

```dockerfile 
FROM nginx

EXPOSE 80 443
```

Build:

```bash
docker build -t demonginx .
```

Run: 

```bash
docker container run demonginx
```

=> Port vẫn chưa truy cập được từ host.

**Muốn truy cập từ ngoài host phải publish:**

```bash
docker run -p 80:80 -p 443:443 demonginx
```

Hoặc sử dụng flag `-P`:

- Nếu image có `EXPOSE`: 

  ```bash
  docker container run -P demonginx
  ```

  Docker sẽ tự map tất cả các expose ports sang random host ports

  ```bash
  80 -> 32768
  443 -> 32769
  ```

### 2.6 ENV 

**Cú pháp:**

```dockerfile 
ENV <key> <value>
ENV <key>=<value>
```

Khai báo các biến giá trị môi trường. Khi run container từ image, các biến môi trường này vẫn có hiệu lực 

Biến môi trường có thể được sử dụng trong các chỉ thị sau: 

- ADD
- COPY
- ENV
- EXPOSE
- FROM
- LABEL 
- STOPSIGNAL
- USER 
- VOLUME
- WORKDIR

### 2.7 ADD 

```dockerfile 
ADD has two forms:
ADD <src>... <dest>
ADD ["<src>",... "<dest>"] (this form is required for paths containing whitespace)
```

- Chỉ thị ADD copy file, thư mục, remote files URL (src) và thêm chúng vào filesystem của image (dest) 

- `src`: có thể khai báo nhiều file, thư mục, có thể dùng các ký hiệu như "*, ?, ..."
- `dest`: phải là đường dẫn tuyệt đối hoặc có quan hệ với chỉ thị WORKDIR

**Các quy tắc:**

- Đường dẫn phải nằm bên trong build context: 

  Ví dụ: 

  ```bash
  project/
  ├── Dockerfile
  ├── app/
  │   └── main.py
  └── secret.txt
  ```

  Dockerfile: 

  ```dockerfile
  COPY app/main.py /app/
  ```

  => Hợp lệ vì `app/main.py` nằm trong build context 

  ```dockerfile 
  COPY ../secret.txt /app/
  ```

  => Sai 

- If is a directory, the entire contents of the directory are copied, including filesystem metadata. The directory itself is not copied, just its contents.

  Ví dụ: 

  ```dockerfile
  COPY app/ /usr/src/app/
  ```

  Thư mục `app/`: 

  ```bash
  app/
  ├── a.txt
  └── b.txt
  ```

  Sau khi COPY: 

  ```bash
  /usr/src/app/
  ├── a.txt
  └── b.txt
  ```

  **NOTE:** Docker chỉ copy nội dung bên trong `app/`, không copy chính folder `app`

  Nếu muốn giữ nguyên tên folder: 

  ```
  COPY app /usr/src/
  ```

- If multiple resources are specified, either directly or due to the use of a wildcard, then must be a directory, and it must end with a slash `/`.

  Ví dụ: 

  ```dockerfile 
  COPY a.txt b.txt /data/
  ```

  Vì có nhiều source: 

  - a.txt
  - b.txt 

  Nên destination bắt buộc: 
  - Phải là directory 
  - Phải kết thúc bằng `/`

- If does not end with a trailing slash, it will be considered a regular file and the contents of will be written at

  Có dấu `/`:

  ```dockerfile 
  COPY test.txt /app/
  ```

  Kết quả: 

  ```bash
  /app/test.txt
  ```

  Không có dấu `/`: 

  ```dockerfile 
  COPY test.txt /app
  ```

  Docker hiểu `/app` là tên file do đó nó sẽ tạo `/app` là một file chứa nội dung của `test.txt`

- If doesn’t exist, it is created along with all missing directories in its path.

  Ví dụ: 

  ```dockerfile 
  COPY test.txt /a/b/c/
  ```

  Dù /a, /a/b, /a/b/c/ chưa tồn tại thì Docker cũng tự tạo toàn bộ

- `ADD URL` không hỗ trợ authentication 

  ```dockerfile 
  ADD https://example.com/file.zip /tmp/
  ```

  `ADD` có thể download từ URL 

  ```dockerfile 
  ADD https://private-site.com/file.zip /tmp/
  ```

  Không dùng được nếu URL cần: 
  - login
  - token
  - auth header 

  Vì ADD không hỗ trợ authentication 

  Lúc này phải dùng: 

  ```dockerfile
  RUN mkdir -p /downloads && \
    curl -L \
    -o /downloads/file.zip \
    https://example.com/file.zip
  ```

  hoặc: 

  ```dockerfile 
  RUN mkdir -p /downloads && \
    wget \
    -O /downloads/file.zip \
    https://example.com/file.zip
  ```

### 2.8 COPY 

```dockerfile 
COPY <src>... <dest>
COPY ["<src>",... "<dest>"] (this form is required for paths containing whitespace)
```

- Chỉ thị COPY copy file, thư mục (src) và thêm chúng vào filesystem của container (dest)
- Các lưu ý tương tự ADD 

### 2.9 ENTRYPOINT 

```dockerfile
ENTRYPOINT ["executable", "param1", "param2"] -> Dạng exec (được khuyến khích dùng)
ENTRYPOINT command param1 param2 -> Dạng shell 
```

`CMD` và `ENTRYPOINT` đều liên quan tới lệnh chạy khi container start, nhưng mục đích khác nhau.

1. CMD là default command 

Ví dụ: 

```dockerfile 
CMD ["nginx", "-g", "daemon off;"]
```

Khi chạy: 

```bash
docker container run myimg
```

Docker sẽ chạy: 

```bash
nginx -g daemon off;

Nhưng CMD dễ bị override: 

```bash
docker container run myimg ls 
```

- `ls` sẽ thay thế hoàn toàn `CMD`

2. `ENTRYPOINT` là lệnh chính cố định 

Ví dụ: 

```dockerfile 
ENTRYPOINT ["nginx"]
```

Khi chạy:

```bash
docker container run myimg
```

Docker chạy: 

```bash 
nginx
```

Nếu bạn chạy Container bằng:

```bash
docker container run myimg -g "daemon off;"
```

thì Docker chạy:

```bash
nginx -g "daemon off;"
```

=> ENTRYPOINT được giữ nguyên và argument phía sau được append vào 

3. Khi có cả CMD và ENTRYPOINT 

Ví dụ: 

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

Khi chạy: 

```bash
python app.py
```

Nếu user override: 

```bash
docker container run myimg test.py
```

Docker sẽ chạy: 

```bash
python test.py
```

4. Người ta dùng ENTRYPOINT nhằm chuẩn bị các điều kiện setup như tạo user, mkdir, change owner... cần thiết để chạy service trong container.

Ví dụ có script như sau:

```Bash
#!/bin/sh

mkdir -p /app/logs
chown -R appuser /app

exec python app.py
```

Dockerfile:

```dockerfile 
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
```

Khi container start: 
- script chạy trước
- setup environment
- cuối cùng chạy service 

### 2.10 VOLUME 

VOLUME trong Dockerfile dùng để khai báo một thư mục sẽ được Docker quản lý như một volume

Ví dụ: 

```dockerfile 
VOLUME ["/data"]
```

- Thư mục `/data` trong container sẽ trở thành volume 
- dữ liệu ở đó sẽ được lưu bên ngoài writable layer của container

### 2.11 USER 

```dockerfile 
USER daemon 
```

- Set username hoặc UID để chạy các lệnh RUN, CMD, ENTRYPOINT trong Dockerfile 

### 2.12 WORKDIR 

```dockerfile 
WORKDIR /path/to/workdir
```

- Chỉ thị WORKDIR dùng để đặt thư mục đang làm việc cho các chỉ thị khác nhau như: RUN, CMD, ENTRYPOINT, COPY, ADD, ... 
