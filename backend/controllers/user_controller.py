from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from infra.db.postgresql_driver import PostgresqlDriver
from services.user_service import UserService
from shared.dto.schemas.user_dto import user_dto as user_dto_schema
from domain.repositories.user_repository import UserRepository


database = PostgresqlDriver()
user_repository = UserRepository(database)
user_service = UserService(user_repository)

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
@expects_json(user_dto_schema)
def create_user():
    dto = request.json
    try:
        created_user = user_service.create_user(dto)
        return jsonify({"message": "User created successfully!", "user": created_user.__repr__()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
