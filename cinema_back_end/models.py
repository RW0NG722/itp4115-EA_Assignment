from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cinemas(db.Model):
    __tablename__ = "cinemas"

    cinema_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)


class Houses(db.Model):
    __tablename__ = "houses"

    house_id = db.Column(db.Integer, primary_key=True)
    cinema_id = db.Column(
        db.Integer, db.ForeignKey("cinemas.cinema_id"), nullable=False
    )
    house_name = db.Column(db.String(100), nullable=False)
    house_type = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, default=True)


class Seats(db.Model):
    __tablename__ = "seats"

    seat_id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey("houses.house_id"), nullable=False)
    seat_number = db.Column(db.String(50), nullable=False)
    seat_available = db.Column(db.Boolean, default=True)
    seat_type = db.Column(db.String(20), nullable=False)


class Movies(db.Model):
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    director = db.Column(db.String(100), nullable=False)
    cast = db.Column(db.Text, nullable=False)
    movie_type = db.Column(db.String(11), nullable=False)


class Orders(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    showtime_id = db.Column(
        db.Integer, db.ForeignKey("showtimes.showtime_id"), nullable=False
    )
    order_date = db.Column(
        db.DateTime, default=db.func.current_timestamp(), nullable=False
    )
    seat_number = db.Column(
        db.Integer, db.ForeignKey("seats.seat_number"), nullable=False
    )
    price = db.Column(db.String(10), nullable=False)
    email = db.Column(db.Integer, db.ForeignKey("seats.seat_number"), nullable=False)


class Showtimes(db.Model):
    __tablename__ = "showtimes"

    showtime_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"), nullable=False)
    cinema_id = db.Column(
        db.Integer, db.ForeignKey("cinemas.cinema_id"), nullable=False
    )
    show_date = db.Column(db.Date, nullable=False)
    show_time = db.Column(db.Time, nullable=False)
    hall_number = db.Column(db.String(10), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    email_subscription = db.Column(db.String(1), nullable=False)
    occupation = db.Column(db.String(50), nullable=True)
    income_level = db.Column(db.String(50), nullable=True)
    work_location = db.Column(db.String(100), nullable=True)
    residence_location = db.Column(db.String(100), nullable=True)

class Member(db.Model):
    __tablename__ = 'members'

    member_type = db.Column(db.String(50), primary_key=True)
    member_price = db.Column(db.Integer, nullable=False)

class Advertisement(db.Model):
    __tablename__ = 'advertisements'

    ad_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad_title = db.Column(db.String(100), nullable=False)
    ad_content = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    member_type = db.Column(db.String(50), db.ForeignKey('members.member_type'), nullable=True)