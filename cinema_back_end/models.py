from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Advertisement(db.Model):
    __tablename__ = 'advertisements'

    ad_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad_title = db.Column(db.String(100), nullable=False)
    ad_content = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    member_type = db.Column(db.String(10), db.ForeignKey('members.member_type'), nullable=True)

    member = db.relationship('Member', backref='advertisements')

class Cinema(db.Model):
    __tablename__ = 'cinemas'

    cinema_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cinema_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    houses = db.relationship('House', backref='cinema')
    showtimes = db.relationship('Showtime', backref='cinema')

class House(db.Model):
    __tablename__ = 'houses'

    house_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinemas.cinema_id'), nullable=False)
    house_name = db.Column(db.String(100), nullable=False)
    house_type = db.Column(db.String(100), nullable=False)
    house_available = db.Column(db.String(1), nullable=False)  #char(1)

    seats = db.relationship('Seat', backref='house')
    showtimes = db.relationship('Showtime', backref='house')

class Member(db.Model):
    __tablename__ = 'members'

    member_type = db.Column(db.String(10), primary_key=True)
    member_price = db.Column(db.Integer, nullable=False)

    users = db.relationship('User', backref='member')
    advertisements = db.relationship('Advertisement', backref='member')
    orders = db.relationship('Order', backref='member')

class Movie(db.Model):
    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    director = db.Column(db.String(100), nullable=False)
    cast = db.Column(db.Text, nullable=False)
    movie_type = db.Column(db.String(11), nullable=False)  #char(11)

    showtimes = db.relationship('Showtime', backref='movie')

class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtimes.showtime_id'), nullable=False)
    order_date = db.Column(db.DateTime, server_default=db.func.now(), nullable=False) #timestamp
    seat_id = db.Column(db.Integer, db.ForeignKey('seats.seat_id'), nullable=False)
    ticket_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    service_fee = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    member_type = db.Column(db.String(10), db.ForeignKey('members.member_type'), nullable=True)

    user = db.relationship('User', backref='orders')
    seat = db.relationship('Seat', backref='orders')
    showtime = db.relationship('Showtime', backref='orders')

class Seat(db.Model):
    __tablename__ = 'seats'

    seat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.house_id'), nullable=False)
    seat_name = db.Column(db.String(10), nullable=False)
    seat_type = db.Column(db.String(10), nullable=False)
    seat_available = db.Column(db.String(1), nullable=False)  #char(1)

class Showtime(db.Model):
    __tablename__ = 'showtimes'

    showtime_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinemas.cinema_id'), nullable=False)
    show_date = db.Column(db.Date, nullable=False)
    show_time = db.Column(db.Time, nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.house_id'), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)  #decimal(10,2)

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)  #char(1)
    birth_date = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    email_subscription = db.Column(db.String(1), nullable=False) #char(1)
    occupation = db.Column(db.String(50), nullable=True)
    income_level = db.Column(db.String(50), nullable=True)
    work_location = db.Column(db.String(100), nullable=True)
    residence_location = db.Column(db.String(100), nullable=True)
    member_type = db.Column(db.String(10), db.ForeignKey('members.member_type'), nullable=True)

    member = db.relationship('Member', backref='users')