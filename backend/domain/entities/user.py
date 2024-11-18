class User:
    VALID_ROLES = {'admin', 'user'}

    def __init__(self, id, first_name, last_name, email, password, role):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role

    @staticmethod
    def create(id: int, first_name: str, last_name: str, email: str, role: str):
        if role not in User.VALID_ROLES:
            raise ValueError(f"Role '{role}' not recognized. Valid roles are: {User.VALID_ROLES}")
        return User(id, first_name, last_name, email, role)
