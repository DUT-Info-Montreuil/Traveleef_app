import bcrypt

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
