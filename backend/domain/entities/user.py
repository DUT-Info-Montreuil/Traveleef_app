from infra.db.database import db


class User(db.Model):
    __tablename__ = 'users'

    VALID_ROLES = {'admin', 'user'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    @staticmethod
    def create(first_name: str, last_name: str, email: str, password: str, role: str):
        if role not in User.VALID_ROLES:
            raise ValueError(f"Role '{role}' not recognized. Valid roles are: {User.VALID_ROLES}")
        return User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role=role
        )