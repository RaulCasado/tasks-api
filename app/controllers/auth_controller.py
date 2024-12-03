from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db

class AuthController:
    @staticmethod
    def validate_register_data(data):
        errors = {}
        if 'username' not in data or not data['username'].strip():
            errors['username'] = 'Username is required.'
        elif len(data['username']) < 3:
            errors['username'] = 'Username must be at least 3 characters long.'
        if 'email' not in data or not data['email'].strip():
            errors['email'] = 'Email is required.'
        elif '@' not in data['email']:
            errors['email'] = 'Email must be a valid email address.'
        if 'password' not in data or not data['password'].strip():
            errors['password'] = 'Password is required.'
        elif len(data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long.'
        return errors

    @staticmethod
    def register(data):
        errors = AuthController.validate_register_data(data)
        if errors:
            return {'error': errors}, 400
        existing_user = User.query.filter(
            (User.username == data['username']) | (User.email == data['email'])
        ).first()
        if existing_user:
            return {'error': 'Username or email already exists'}, 400
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User registered successfully!'}, 201

    @staticmethod
    def validate_login_data(data):
        errors = {}
        if 'email' not in data or not data['email'].strip():
            errors['email'] = 'Email is required.'
        elif '@' not in data['email']:
            errors['email'] = 'Email must be a valid email address.'
        if 'password' not in data or not data['password'].strip():
            errors['password'] = 'Password is required.'
        return errors

    @staticmethod
    def login(data):
        errors = AuthController.validate_login_data(data)
        if errors:
            return {'error': errors}, 400
        user = User.query.filter_by(email=data['email']).first()
        if not user or not check_password_hash(user.password_hash, data['password']):
            return {'error': 'Invalid credentials'}, 401
        access_token = create_access_token(identity=str(user.id))
        return {'access_token': access_token}, 200
