from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cinema(db.Model):
    __tablename__ = 'cinema'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    total_houses = db.Column(db.Integer, nullable=False)

class House(db.Model):
    __tablename__ = 'house'
    
    id = db.Column(db.Integer, primary_key=True)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'), nullable=False)
    house_number = db.Column(db.String(10), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

class Seat(db.Model):
    __tablename__ = 'seat'
    
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    row = db.Column(db.String(5), nullable=False)
    is_available = db.Column(db.Boolean, default=True)

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Order(db.Model):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtime.id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)


class Promotion(db.Model):
    __tablename__ = 'promotion'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)

class Movie(db.Model):
    __tablename__ = 'movie'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
    type = db.Column(db.String(50), nullable=False)
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