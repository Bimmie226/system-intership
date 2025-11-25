# MySQL CROSS JOIN
## Examples
- Dùng cross join tạo bộ bài gồm 52 lá
- Đầu tiên, tạo 1 bảng để lưu các chất(suits):

    ```sql
    CREATE TABLE suits (
        suitId INT,
        suitName VARCHAR(10)
    );
    ```
- Tạo 1 bảng để lưu các hạng bài(ranks):

    ```sql
    CREATE TABLE ranks (
        rankId INT,
        rankName VARCHAR(5)
    );
    ```

- Chèn dữ liệu vào bảng suits và ranks:

    ```sql
    INSERT INTO suits (suitId, suitName) VALUES
        (1, 'Ro'),
        (2, 'Co'),
        (3, 'Tep'),
        (4, 'Bich');

    INSERT INTO ranks (rankId, rankName) VALUES
        (1, 'A'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, 'J'),
        (12, 'Q'),
        (13, 'K');
    ```
    `
- sử dụng cross join để kết hợp các chất và các hạng, nhằm tạo ra bộ bài 52 lá:

    ![alt text](../images/cross_join_01.png)

