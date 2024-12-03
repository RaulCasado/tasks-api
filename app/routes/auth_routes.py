from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.auth_controller import AuthController
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response, status = AuthController.register(data)
    return jsonify(response), status

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response, status = AuthController.login(data)
    return jsonify(response), status

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(int(current_user_id))
    return jsonify(logged_in_as=user.username), 200
