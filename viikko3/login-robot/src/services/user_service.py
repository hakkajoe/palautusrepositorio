from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if len(username) < 3 or not re.match("^[a-zA-Z]+$", username):
            raise UserInputError("Invalid username")
        if len(password) < 8 or not (any(c.isdigit() for c in password) and any(c.isalpha() for c in password)):
            raise UserInputError("Invalid password")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
