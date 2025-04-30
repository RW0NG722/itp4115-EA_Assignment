from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from models import db, User, Seats, Showtimes, Orders
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/cinema"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create the database tables if they don't exist
if not os.path.exists("test_database.db"):
    with app.app_context():
        db.create_all()


# Sign Up Route
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json

    # Validate input
    required_fields = [
        "user_name",
        "password",
        "confirm_password",
        "first_name",
        "last_name",
        "phone",
        "email",
        "confirm_email",
        "email_subscription",
    ]

    if not all(key in data for key in required_fields):
        return jsonify({"message": "Missing required fields!"}), 400

    # Check password confirmation
    if data["password"] != data["confirm_password"]:
        return jsonify({"message": "Passwords do not match!"}), 400

    # Check if the user already exists
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "User already exists!"}), 400

    # Create a new user
    new_user = User(
        user_name=data["user_name"],
        password=data["password"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        gender=data["gender"],
        birth_date=(
            datetime.strptime(data["birth_date"], "%Y-%m-%d").date()
            if data["birth_date"] != ""
            else "1970-01-01"
        ),
        phone=data["phone"],
        email=data["email"],
        email_subscription=data["email_subscription"],
        occupation=data["occupation"] if "occupation" in data else None,
        income_level=data["income_level"] if "income_level" in data else None,
        work_location=data["work_location"] if "work_location" in data else None,
        residence_location=(
            data["residence_location"] if "residence_location" in data else None
        ),
    )

    db.session.add(new_user)
    db.session.commit()

    # Prepare the response in the desired format
    response_data = {
        "birth_date": new_user.birth_date.isoformat(),
        "occupation": new_user.occupation,
        "confirm_email": data["confirm_email"],
        "confirm_password": data["confirm_password"],
        "email": new_user.email,
        "first_name": new_user.first_name,
        "income_level": new_user.income_level,
        "last_name": new_user.last_name,
        "residence_location": new_user.residence_location,
        "password": data["password"],  # Be cautious about returning passwords
        "phone": new_user.phone,
        "email_subscription": new_user.email_subscription,
        "sex": new_user.gender,
        "work_location": new_user.work_location,
    }

    return jsonify(response_data), 200


# Login Route
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    print("---------------")
    print(data)
    print("---------------")
    user = User.query.filter_by(email=data["email"]).first()

    # Validate input
    if not all(key in data for key in ["email", "password"]):
        return jsonify({"message": "Missing required fields!"}), 400

    # # Check if user exists
    user = User.query.filter_by(email=data["email"]).first()
    print(user)
    if (
        not user or user.password != data["password"]
    ):  # Simple password check (not secure)
        return jsonify({"message": "Invalid credentials!"}), 401

    # Prepare the response data
    response_data = {
        "user_id": user.user_id,
        "user_name": user.user_name,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "gender": user.gender,
        "birth_date": user.birth_date.isoformat(),
        "phone": user.phone,
        "email": user.email,
        "email_subscription": user.email_subscription,
        "occupation": user.occupation,
        "income_level": user.income_level,
        "work_location": user.work_location,
        "residence_location": user.residence_location,
    }

    return (
        jsonify({"message": "Login successful!", "data": response_data, "code": 200}),
        200,
    )
    # return jsonify({}), 200


@app.route("/users/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json

    user.user_name = data.get("user_name", user.user_name)
    user.password = data.get("password", user.password)
    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)
    user.gender = data.get("gender", user.gender)
    user.birth_date = data.get("birth_date", user.birth_date)
    user.phone = data.get("phone", user.phone)
    user.email = data.get("email", user.email)
    user.email_subscription = data.get("email_subscription", user.email_subscription)
    user.occupation = data.get("occupation", user.occupation)
    user.income_level = data.get("income_level", user.income_level)
    user.work_location = data.get("work_location", user.work_location)
    user.residence_location = data.get("residence_location", user.residence_location)

    db.session.commit()
    return jsonify({"message": "User updated"}), 200


# order Route
@app.route("/orders", methods=["GET"])
def create_order():
    data = request.json
    new_order = Order(
        user_id=data["user_id"],
        showtime_id=data["showtime_id"],
        seat_name=data["seat_name"],
        ticket_type=data["ticket_type"],
        price=data["price"],
        service_fee=data["service_fee"],
        total_amount=data["total_amount"],
        email=data["email"],
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order created", "order_id": new_order.order_id}), 201


# Get all orders
@app.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    output = []
    for order in orders:
        order_data = {
            "order_id": order.order_id,
            "user_id": order.user_id,
            "showtime_id": order.showtime_id,
            "order_date": order.order_date,
            "seat_name": order.seat_name,
            "ticket_type": order.ticket_type,
            "price": order.price,
            "service_fee": order.service_fee,
            "total_amount": order.total_amount,
            "email": order.email,
        }
        output.append(order_data)
    return jsonify(output), 200


# Get a single order by ID
@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    order_data = {
        "order_id": order.order_id,
        "user_id": order.user_id,
        "showtime_id": order.showtime_id,
        "order_date": order.order_date,
        "seat_name": order.seat_name,
        "ticket_type": order.ticket_type,
        "price": order.price,
        "service_fee": order.service_fee,
        "total_amount": order.total_amount,
        "email": order.email,
    }
    return jsonify(order_data), 200


if __name__ == "__main__":
    app.run(debug=True)
