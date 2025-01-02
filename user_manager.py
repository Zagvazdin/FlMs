# user_manager.py

class UserManager:
    def __init__(self):
        self.users = {
            '0001': {'password': '000000', 'role': 'admin'},
            '0010': {'password': '342134', 'role': 'user'},
            '0100': {'password': '121341', 'role': 'user'}
        }

    def validate_user(self, username, password):
        return username in self.users and self.users[username]['password'] == password

    def get_user_role(self, username):
        return self.users[username]['role'] if username in self.users else None
