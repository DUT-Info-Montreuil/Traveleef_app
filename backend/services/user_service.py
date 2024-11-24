import bcrypt
from flask_jwt_extended import create_access_token

from domain.repositories.user_repository import UserRepository
from domain.entities.user import User


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, dto: dict) -> User:
        password = dto['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = User(
            id=0,
            first_name=dto['first_name'],
            last_name=dto['last_name'],
            email=dto['email'],
            password=hashed_password.decode('utf-8'),
            role=dto['role']
        )
        return self.user_repository.create_user(user)

    def login_user(self, mail: str, password: str):
        user = self.user_repository.find_user_by_email(mail)
        if not user:
            raise Exception("Invalid email or password")

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise Exception("Invalid email or password")

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token, "role": user.role}