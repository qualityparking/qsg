from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models.user import User, RoleEnum
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed = generate_password_hash(data['password'])
    user = User(
        full_name = data['full_name'],
        username = data['username'],
        password = hashed,
        role = RoleEnum[data.get('role','member')]
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(msg='User registered'), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify(msg='Bad credentials'), 401
    token = create_access_token(identity={'id': user.id, 'role': user.role.value})
    return jsonify(token=token), 200
