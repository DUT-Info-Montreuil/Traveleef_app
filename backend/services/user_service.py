import bcrypt
from flask_jwt_extended import create_access_token
from domain.repositories.user_repository import UserRepository
from domain.entities.user import User


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, dto: dict) -> User:
        if 'password' not in dto or not dto['password']:
            raise ValueError("Password is required.")

        hashed_password = bcrypt.hashpw(dto['password'].encode('utf-8'), bcrypt.gensalt())

        user = User(
            first_name=dto.get('first_name', '').strip(),
            last_name=dto.get('last_name', '').strip(),
            email=dto['email'].strip().lower(),
            password=hashed_password.decode('utf-8'),
            role=dto['role']
        )

        try:
            return self.user_repository.create_user(user)
        except Exception as e:
            raise Exception(f"Failed to create user: {e}")

    def login_user(self, email: str, password: str) -> dict:

        user = self.user_repository.find_user_by_email(email)
        if not user:
            raise ValueError("Invalid email or password")

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise ValueError("Invalid email or password")

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token, "role": user.role}