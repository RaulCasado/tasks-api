from flask import Blueprint, request, jsonify
from app.controllers.user_controller import UserController
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app import db

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    return UserController.get_users()

@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return UserController.get_user(user_id)

@user_bp.route('/users', methods=['POST'])
def create_user():
    return UserController.create_user()

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    return UserController.update_user(user_id)

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return UserController.delete_user(user_id)
