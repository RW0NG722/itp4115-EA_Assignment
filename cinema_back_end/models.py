from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cinema(db.Model):
    __tablename__ = 'cinema'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(200), nullable=False)
    available = db.Column(db.Boolean, default=True)

class House(db.Model):
    __tablename__ = 'house'
    
    id = db.Column(db.Integer, primary_key=True)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'), nullable=False)
    screen_genre = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, default=True)

class Seat(db.Model):
    __tablename__ = 'seat'
    
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    seat_number = db.Column(db.String(2), nullable=False)
    seat_available = db.Column(db.Boolean, default=True)

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

class Order(db.Model):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtime.id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Promotion(db.Model):
    __tablename__ = 'promotion'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)

class Movie(db.Model):
    __tablename__ = 'movie'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
    genre = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

class Review(db.Model):
    __tablename__ = 'review'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Rating out of 5
    comment = db.Column(db.Text, nullable=True)

class Showtime(db.Model):
    __tablename__ = 'showtime'
    
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
