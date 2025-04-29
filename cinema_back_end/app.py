from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from models import db, User, Movie
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/cinema"
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
    required_fields = [
        'username', 'password', 'confirmPassword', 'firstName', 
        'lastName', 'sex', 'birthDate', 'phone', 
        'email', 'confirmEmail', 'receiveEmail', 
        'career', 'income', 'workArea', 'livingArea'
    ]
    
    if not all(key in data for key in required_fields):
        return jsonify({'message': 'Missing required fields!'}), 400

    # Check password confirmation
    if data['password'] != data['confirmPassword']:
        return jsonify({'message': 'Passwords do not match!'}), 400

    # Check if the user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists!'}), 400

    # Create a new user
    new_user = User(
        username=data['username'],
        password=data['password'],  # Store the password directly (not recommended for production)
        first_name=data['firstName'],
        last_name=data['lastName'],
        gender=data['sex'],
        birth_date=datetime.strptime(data['birthDate'], '%Y-%m-%d').date(),
        mobile=data['phone'],
        email=data['email'],
        receive_email=data['receiveEmail'],
        career=data['career'],
        income=data['income'],
        work_area=data['workArea'],
        living_area=data['livingArea']
    )

    db.session.add(new_user)
    db.session.commit()

    # Prepare the response in the desired format
    response_data = {
        "birthDate": new_user.birth_date.isoformat(),
        "career": new_user.career,
        "confirmEmail": data['confirmEmail'],
        "confirmPassword": data['confirmPassword'],
        "email": new_user.email,
        "firstName": new_user.first_name,
        "income": new_user.income,
        "lastName": new_user.last_name,
        "livingArea": new_user.living_area,
        "password": data['password'],  # Be cautious about returning passwords
        "phone": new_user.mobile,
        "receiveEmail": new_user.receive_email,
        "sex": new_user.gender,
        "workArea": new_user.work_area
    }

    return jsonify(response_data), 201



# Login Route
@app.route('/login', methods=['GET'])
def login():
    # data = request.json
    data = {
        "email": "asdasda@qwe.com",
        "password": "123456"
    }
    user = User.query.filter_by(email=data['email']).first()
    print("-----------------------------")
    print(user)
    print("-----------------------------")
    # Validate input
    if not all(key in data for key in ['email', 'password']):
        return jsonify({'message': 'Missing required fields!'}), 400

    # # Check if user exists
    user = User.query.filter_by(email=data['email']).first()
    print(user)
    if not user or user.password != data['password']:  # Simple password check (not secure)
        return jsonify({'message': 'Invalid credentials!'}), 401

    # Prepare the response data
    response_data = {
        "id": user.user_id,
        "username": user.username,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "gender": user.gender,
        "birthDate": user.birth_date.isoformat(),
        "phone": user.phone,
        "email": user.email,
        "receiveEmail": user.email,
        "career": user.occupation,
        "income": user.income_level,
        "workArea": user.work_location,
        "livingArea": user.residence_location
    }

    return jsonify({'message': 'Login successful!', 'user': response_data}), 200
    # return jsonify({}), 200

if __name__ == '__main__':
    app.run(debug=True)