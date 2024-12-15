from domain.entities.user import User
from infra.db.database import db
from sqlalchemy.exc import SQLAlchemyError


class UserRepository:

    @staticmethod
    def create_user(user: User) -> User:
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error creating user: {e}")

    @staticmethod
    def find_user_by_email(email: str) -> User:

        try:
            return User.query.filter_by(email=email).first()
        except SQLAlchemyError as e:
            raise Exception(f"Error fetching user by email: {e}")
