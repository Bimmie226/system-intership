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

