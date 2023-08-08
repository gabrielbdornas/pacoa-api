# app.py
from flask import (
                   Blueprint,
                   jsonify,
                   request,
                  )
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from werkzeug.security import check_password_hash
from models import User

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the user exists
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Invalid username'}), 401

    # Check the password
    if not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid password'}), 401

    # Create and return an access token
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200
