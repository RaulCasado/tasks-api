from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app import db
from app.models.user import User
from app.models.task import Task

class UserController:
    @staticmethod
    def get_users():
        users = User.query.all()
        return jsonify([{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at
        } for user in users])

    @staticmethod
    def get_user(user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at
        })

    @staticmethod
    def create_user():
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201

    @staticmethod
    def update_user(user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        if 'password' in data:
            user.password_hash = generate_password_hash(data['password'], method='pbkdf2:sha256')
        db.session.commit()
        return jsonify({'message': 'User updated successfully!'})

    @staticmethod
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
    
        tasks = Task.query.filter_by(user_id=user_id).all()
        if tasks:
            return jsonify({'error': 'User cannot be deleted because they have associated tasks'}), 400

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully!'})

