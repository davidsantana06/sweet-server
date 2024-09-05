from datetime import timedelta
from flask_bcrypt import check_password_hash
from flask_login import login_user, logout_user
from werkzeug.exceptions import Unauthorized

from app.database import User
from app.modules.user import operations as user_operations


def login(user: User) -> None:
    login_user(user, remember=True, duration=timedelta(days=365))


def logout() -> None:
    logout_user()


def check_authentication() -> bool:
    return user_operations.get_current().is_authenticated


def check_credentials(user: User, password: str) -> bool:
    if not check_password_hash(user.password, password):
        raise Unauthorized(
            'The credentials are incorrect. Please check your input and try again.'
        )
    return True
