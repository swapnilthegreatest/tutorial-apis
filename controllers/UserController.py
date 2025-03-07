from flask import request, jsonify, json, Blueprint
from typing import List
from flask_jwt_extended import jwt_required
from models.User import User

user_controller = Blueprint('user_controller', __name__)
users : List[User] = []

@user_controller.route('/users', methods=['GET'])
def get_user():
    user_id: int = int(request.args.get('user_id'))
    try:
        user: User = users[user_id]
        return jsonify(user)
    except:
        return jsonify({'error': 'data not found'})

@user_controller.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    request_data = json.loads(request.data)
    user_id = len(users)
    user = User(user_id, request_data['name'], request_data['status'])
    users.append(user)
    return jsonify(user)