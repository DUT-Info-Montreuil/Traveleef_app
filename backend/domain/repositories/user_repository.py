from domain.entities.user import User
from shared.dto.mappers.user_dto_mapper import UserDTOMapper


class UserRepository:

    def __init__(self, database):
        self.database = database

    def create_user(self, user: User) -> User:
        conn = self.database.connect()
        try:
            query = """
               INSERT INTO users (first_name, last_name, password, email, role)
               VALUES (%s, %s, %s, %s, %s)
               RETURNING id;
               """
            with conn.cursor() as cursor:
                cursor.execute(query, (user.first_name, user.last_name, user.password, user.email, user.role))
                user_id = cursor.fetchone()[0]
                conn.commit()

            user.id = user_id
            return user
        except Exception as e:
            conn.rollback()
            raise f"Error creating user: {e}"
        finally:
            self.database.close_connection()
