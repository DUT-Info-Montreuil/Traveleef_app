from domain.repositories.user_repository import UserRepository
from infra.db.postgresql_driver import PostgresqlDriver
from services.user_service import UserService
from shared.dto.mappers.user_dto_mapper import UserDTOMapper
from shared.dto.schemas.user_dto import user_dto

database = PostgresqlDriver()
_user_repository = UserRepository(database)
_user_service = UserService(_user_repository)
_mapper = UserDTOMapper()

user_module = {
    "service": _user_service,
    "dto_mapper": _mapper,
    "dto_schema": user_dto
}