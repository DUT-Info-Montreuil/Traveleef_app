from domain.entities.user import User


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

    def find_user_by_email(self, email: str) -> User:
        conn = self.database.connect()
        try:
            query = """
                SELECT * FROM users WHERE email = (%s);
            """
            with conn.cursor() as cursor:
                cursor.execute(query, (email,))
                result = cursor.fetchone()
                if result:
                    return User(
                        id=result[0],
                        first_name=result[1],
                        last_name=result[2],
                        email=result[3],
                        password=result[4],
                        role=result[5]
                    )
                return None
        except Exception as e:
            raise f"Error user does exist : {e}"
        finally:
            self.database.close_connection()
