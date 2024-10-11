from datetime import datetime, timezone
from flask_bcrypt import check_password_hash
from flask_login import login_user, logout_user
from werkzeug.exceptions import Unauthorized

from app.config import parameters
from app.database import User
from app.modules.user import operations as user_operations


def check_authentication() -> bool:
    return user_operations.get_current().is_authenticated


def _calculate_expiration() -> datetime:
    return (
        datetime.now(timezone.utc) +
        parameters.PERMANENT_SESSION_LIFETIME
    )


def login(user: User, password: str) -> str:
    is_credentials_correct = check_password_hash(
        user.password,
        password
    )
    if not is_credentials_correct:
        raise Unauthorized(
            'The credentials are incorrect. '
            'Please check your input and try again.'
        )
    login_user(user, remember=True)
    expiration = _calculate_expiration()
    return expiration.isoformat()


def logout() -> None:
    logout_user()
