from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from shared.modules.user_module import user_module

user_dto_schema = user_module['dto_schema']
service = user_module['service']
mapper = user_module['dto_mapper']

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
@expects_json(user_dto_schema)
def create_user():
    dto = request.json
    try:
        created_user = service.create_user(dto)
        return jsonify({"message": "User created successfully!", "user": mapper.to_external(created_user)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        login_response = service.login_user(email, password)
        return jsonify({"access_token": login_response['access_token'], "role": login_response['role']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
