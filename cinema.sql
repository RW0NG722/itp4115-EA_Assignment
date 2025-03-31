-- 1地区层级表
CREATE TABLE regions (
    region_id INT PRIMARY KEY AUTO_INCREMENT,
    parent_id INT DEFAULT NULL,
    region_type ENUM('main', 'district', 'subdistrict') NOT NULL,
    name_zh VARCHAR(20) NOT NULL,
    -- 层级关系
    FOREIGN KEY (parent_id) REFERENCES regions(region_id)
);

-- 预填充
INSERT INTO regions (region_type, name_zh, parent_id) VALUES
('main', '香港區', NULL),
('main', '九龍區', NULL),
('main', '新界區', NULL),
('district', '中西區', 1),
('district', '東區', 1),
('district', '南區', 1),
('district', '灣仔', 1),
('district', '九龍城', 2),
('district', '觀塘', 2),
('district', '深水埗', 2),
('district', '黃大仙', 2),
('district', '油尖旺', 2),
('district', '北區', 3),
('district', '沙田', 3),
('district', '大埔', 3),
('district', '西貢', 3);

--2用户表
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    -- 账户资料
    username VARCHAR(10) NOT NULL UNIQUE CHECK (LENGTH(username) BETWEEN 5 AND 10),
    password_hash CHAR(60) NOT NULL, 
    email VARCHAR(255) NOT NULL UNIQUE,
    -- 基本资料
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender ENUM('男', '女') NOT NULL,
    birth_date DATE NOT NULL, 
    -- 联络资料
    mobile VARCHAR(15) NOT NULL,
    -- 宣传偏好
    accept_promo_chinese BOOLEAN DEFAULT FALSE,
    accept_promo_english BOOLEAN DEFAULT FALSE,
    -- 职业与收入
    occupation ENUM(
        '學生',
        '經理及行政級人員',
        '專業人員',
        '文職人員',
        '服務及銷售',
        '技術人員',
        '其他'
    ) DEFAULT NULL,
    income_range ENUM(
        '$5000或以下',
        '$5001 - $10000',
        '$10001 - $15000',
        '$15001 - $20000',
        '$20001 - $25000',
        '$25001 - $30000',
        '$30001或以上'
    ) DEFAULT NULL,
    -- 统一地区表关联
    work_region_id INT,
    residence_region_id INT,
    -- 系统信息
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- 外键约束
    FOREIGN KEY (work_region_id) REFERENCES regions(region_id),
    FOREIGN KEY (residence_region_id) REFERENCES regions(region_id)
);

--3. 影院表（关联区域表）
CREATE TABLE cinemas (
    cinema_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,            -- 影院名称（如"B+ cinema MOKO"）
    address VARCHAR(255),                  -- 地址（如"旺角東"）
    region_id INT NOT NULL,                -- 关联次区域（如region_id=6对应"旺角東"）
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

-- 示例影院数据（需要根据新的 regions 表调整 region_id）
-- 这里假设需要手动调整 region_id 以匹配新的 regions 表
INSERT INTO cinemas (name, address, region_id) VALUES
('MOVIE MOVIE Pacific Place', '太古城', 4), -- 需要确认 region_id 是否正确
('B+ cinema MOKO', '旺角東', 6), -- 需要确认 region_id 是否正确
('B+ cinema apm', '觀塘', 7), -- 需要确认 region_id 是否正确
('PALACE ifc', 'ifc', 5), -- 需要确认 region_id 是否正确
('GALA CINEMA', '朗豪坊', 6); -- 需要确认 region_id 是否正确

--4. 电影表
CREATE TABLE movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title_zh VARCHAR(100) NOT NULL,        -- 中文片名（如"IMAX PINK FLOYD AT POMPEII"）
    title_en VARCHAR(100),                 -- 英文片名
    director VARCHAR(50),                  -- 导演
    cast TEXT,                             -- 主演（JSON存储，如'["David Gilmour", "Roger Waters"]'）
    release_date DATE NOT NULL,            -- 上映日期
    duration SMALLINT NOT NULL,            -- 时长（分钟）
    genre VARCHAR(50),                     -- 类型（如"音乐纪录片"）
    synopsis TEXT,                         -- 剧情简介
    poster_url VARCHAR(255)                -- 海报链接
);

-- 5. 放映场次表（含票价）
CREATE TABLE schedules (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT NOT NULL,                 -- 关联电影
    cinema_id INT NOT NULL,                -- 关联影院
    hall_type ENUM('IMAX', '4DX', '全景厅', 'VIP厅'), -- 影厅类型
    start_time DATETIME NOT NULL,          -- 放映时间（如'2025-04-24 19:50:00'）
    base_price DECIMAL(6,2) NOT NULL,      -- 基础票价（如170.00）
    additional_fee DECIMAL(6,2) DEFAULT 0, -- 附加费用（如10.00）
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (cinema_id) REFERENCES cinemas(cinema_id)
);

-- 6. 订单表
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,                  -- 关联用户
    schedule_id INT NOT NULL,              -- 关联场次
    total_price DECIMAL(8,2) NOT NULL,     -- 总价（含附加费）
    status ENUM('待支付', '已支付', '已取消') DEFAULT '待支付',
    payment_method ENUM('信用卡', '支付宝', '微信支付', 'PayPal'),
    transaction_id VARCHAR(50),            -- 第三方支付流水号
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id)
);

-- 7. 座位表（按场次管理）
CREATE TABLE seats (
    seat_id INT PRIMARY KEY AUTO_INCREMENT,
    schedule_id INT NOT NULL,             -- 关联场次
    seat_number VARCHAR(10) NOT NULL,     -- 座位号（如"A1"）
    is_booked BOOLEAN DEFAULT FALSE,      -- 是否已预订
    order_id INT,                         -- 关联订单（若已预订）
    FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
-- 8. 帳戶表
CREATE TABLE Account (
    user_id VARCHAR(10) NOT NULL,
    password VARCHAR(10) NOT NULL);
