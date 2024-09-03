from flask_bcrypt import check_password_hash
from flask_login import (
    login_user, logout_user,
    current_user
)
from werkzeug.exceptions import Unauthorized

from app.database import User


def check_authentication() -> bool:
    return current_user.is_authenticated


def check_credentials(user: User, password: str) -> bool:
    if not check_password_hash(user.password, password):
        raise Unauthorized(
            'The credentials are incorrect. Please check your input and try again.'
        )
    return True


def login(user: User) -> None:
    login_user(user, remember=True)


def logout() -> None:
    logout_user()
