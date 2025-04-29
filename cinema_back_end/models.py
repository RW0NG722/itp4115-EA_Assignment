from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cinema(db.Model):
<<<<<<< HEAD
    __tablename__ = 'cinemas'
    
    cinema_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    house = db.Column(db.String(50), nullable=False)
    sent = db.Column(db.String(255), nullable=False)
    format = db.Column(db.String(255), nullable=False)
    ticket_information = db.Column(db.String(255), nullable=False)
=======
    __tablename__ = 'cinema'
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # 影院名称
    district = db.Column(db.String(200), nullable=False)  # 所属区域
    address = db.Column(db.String(200), nullable=False)  # 影院地址
    total_seats = db.Column(db.Integer, nullable=False)  # 总座位数（所有影厅座位之和）
    house_count = db.Column(db.Integer, nullable=False)  # 影厅数量
    available = db.Column(db.Boolean, default=True)  # 是否可用
    houses = db.relationship('House', backref='cinema', lazy=True)  # 与影厅的一对多关系

class House(db.Model):
    __tablename__ = 'house'
    
    id = db.Column(db.Integer, primary_key=True)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'), nullable=False)  # 关联影院外键
    name = db.Column(db.String(100), nullable=False)  # 影厅名称（如 H2、MM Plus）
    seats = db.Column(db.Integer, nullable=False)  # 影厅座位数
    sound_effect = db.Column(db.String(100), nullable=False)  # 音效（如 USL 8 Channels、AuroMax 3D）
    available = db.Column(db.Boolean, default=True)  # 是否可用

class Seat(db.Model):
    __tablename__ = 'seat'
    
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)  # 关联影厅
    seat_number = db.Column(db.String(50), nullable=False)  # 座位号
    seat_available = db.Column(db.Boolean, default=True)  # 是否可用
    seat_type = db.Column(db.String(20), nullable=False)  # 座位类型，如 'non_vibrating'（非震动）、'vibrating'（震动）、'wheelchair'（轮椅）

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    username = db.Column(db.String(50), unique=True, nullable=False)  # User's username
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password
    first_name = db.Column(db.String(50), nullable=False)  # User's first name
    last_name = db.Column(db.String(50), nullable=False)  # User's last name
    gender = db.Column(db.String(10), nullable=False)  # User's gender
    birth_date = db.Column(db.Date, nullable=False)  # User's birth date
    mobile = db.Column(db.String(15), nullable=False)  # User's mobile number
    email = db.Column(db.String(100), unique=True, nullable=False)  # User's email
    email_confirmed = db.Column(db.Boolean, default=False)  # Email confirmation status
    occupation = db.Column(db.String(50), nullable=True)  # User's occupation
    income = db.Column(db.String(50), nullable=True)  # User's income range
    work_area = db.Column(db.String(50), nullable=True)  # User's work area
    residential_area = db.Column(db.String(50), nullable=True)  # User's residential area
    promotional_email = db.Column(db.Boolean, default=False)

class Orders(db.Model):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    screening_id = db.Column(db.Integer, db.ForeignKey('Screening.id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(120), nullable=False) 
    orders_time = db.Column(db.DateTime, nullable=False)  


class Promotion(db.Model):#ing
    __tablename__ = 'promotion'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
>>>>>>> ad624a505961fb5cd5fdf7bd9bf0351670d9dbb3

class Movie(db.Model):
    __tablename__ = 'movies'
    
<<<<<<< HEAD
    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    director = db.Column(db.String(100), nullable=False)
    cast = db.Column(db.Text, nullable=False)
    format = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(1), nullable=False)  # Assuming type is a single character

class Order(db.Model):
    __tablename__ = 'orders'
=======
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(200), nullable=False) #区域
    release_date = db.Column(db.Date, nullable=False)  # 上映时间（日期类型）
    duration = db.Column(db.Integer, nullable=False)    # 时长（分钟，整数类型）
    language = db.Column(db.String(200), nullable=False)  # 语言
    story_intro = db.Column(db.Text, nullable=False)     # 故事简介（长文本）
    director = db.Column(db.String(200), nullable=False)  # 导演
    actors = db.Column(db.String(500), nullable=False)   # 演员（is ok存储多个演员，用逗号等分隔）

class Review(db.Model):   #？？
    __tablename__ = 'review'
>>>>>>> ad624a505961fb5cd5fdf7bd9bf0351670d9dbb3
    
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtimes.showtime_id'), nullable=False)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    ticket_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    service_fee = db.Column(db.String(10), nullable=False)
    total_amount = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class PasswordReset(db.Model):
    __tablename__ = 'password_resets'
    
    reset_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    reset_token = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

<<<<<<< HEAD
class Showtime(db.Model):
    __tablename__ = 'showtimes'
    
    showtime_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinemas.cinema_id'), nullable=False)
    show_date = db.Column(db.Date, nullable=False)
    show_time = db.Column(db.Time, nullable=False)
    hall_number = db.Column(db.String(10), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)  # Assuming gender is a single character
    birth_date = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    email_subscription = db.Column(db.String(1), nullable=False)  # Assuming it's a single character
    occupation = db.Column(db.String(50), nullable=True)
    income_level = db.Column(db.String(50), nullable=True)
    work_location = db.Column(db.String(100), nullable=True)
    residence_location = db.Column(db.String(100), nullable=True)
=======
class Screening(db.Model):  #放映场次
    __tablename__ = 'screening'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)  # 关联电影外键
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)  # 关联影厅外键
    start_time = db.Column(db.DateTime, nullable=False)  # 放映时间
    price = db.Column(db.Float, nullable=False)  # 新增价格字段
>>>>>>> ad624a505961fb5cd5fdf7bd9bf0351670d9dbb3
