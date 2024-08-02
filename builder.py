class DataValidator:
    def __init__(self, data):
        self.data = data
        self.errors = []

    def validate_email(self):
        if '@' not in self.data.get('email', ''):
            self.errors.append('Invalid email')
        return self

    def validate_password(self):
        if len(self.data.get('password', '')) < 8:
            self.errors.append('Password is too short')
        return self

    def get_errors(self):
        return self.errors