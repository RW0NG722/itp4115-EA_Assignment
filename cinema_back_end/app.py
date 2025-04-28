from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os
from models import db, User, Cinema, House, Seat, Order, Promotion, Movie, Review, Showtime

app = Flask(__name__)
CORS(app)  # Enable CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create the database tables if they don't exist
if not os.path.exists('test_database.db'):
    with app.app_context():
        db.create_all()

# Sign Up Route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    # Validate input
    if not all(key in data for key in ['username', 'password', 'first_name', 'last_name', 'gender', 'birth_date', 'mobile', 'email']):
        return jsonify({'message': 'Missing required fields!'}), 400

    # Check if the user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists!'}), 400

    # Create a new user
    new_user = User(
        username=data['username'],
        password_hash=generate_password_hash(data['password']),
        first_name=data['first_name'],
        last_name=data['last_name'],
        gender=data['gender'],
        birth_date=data['birth_date'],  # Ensure this is in YYYY-MM-DD format
        mobile=data['mobile'],
        email=data['email'],
        email_confirmed=False,  # Default to not confirmed
        occupation=data.get('occupation'),
        income=data.get('income'),
        work_area=data.get('work_area'),
        residential_area=data.get('residential_area'),
        promotional_email=data.get('promotional_email', False)  # Default to False if not provided
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401

    return jsonify({'message': 'Login successful!', 'user_id': user.id}), 200

# Place Order Route
@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    user_id = data['user_id']
    order = Order(
        user_id=user_id,
        showtime_id=data['showtime_id'],
        seat_id=data['seat_id'],
        price=data['price']
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order placed successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)