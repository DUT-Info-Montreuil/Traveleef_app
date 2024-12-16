from domain.entities.user import User
from domain.kernel.mapper import BaseMapper


class UserDTOMapper(BaseMapper[User, dict]):
    def to_domain(self, dto: dict, user_id: int = 0) -> User:
        return User.create(
            id=user_id,
            first_name=dto["first_name"],
            last_name=dto["last_name"],
            email=dto["email"],
            role=dto["role"],
        )

    def to_external(self, user: User) -> dict:
        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "role": user.role,
        }