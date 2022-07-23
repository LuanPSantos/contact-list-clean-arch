
class User:
    def __init__(self, name: str, email: str, password: str, user_id: str = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

