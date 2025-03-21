#用户表
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    -- 账户资料
    username VARCHAR(10) NOT NULL UNIQUE CHECK (LENGTH(username) BETWEEN 5 AND 10),
    password_hash CHAR(60) NOT NULL, 
    email VARCHAR(255) NOT NULL UNIQUE,
    confirmed_email VARCHAR(255) NOT NULL,
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
    -- 隐私条款
    agreed_to_terms BOOLEAN NOT NULL DEFAULT FALSE,
    -- 系统信息
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- 外键约束
    FOREIGN KEY (work_region_id) REFERENCES regions(region_id),
    FOREIGN KEY (residence_region_id) REFERENCES regions(region_id)
);

-- 地区层级表
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

#doing
