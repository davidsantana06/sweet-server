from flask_bcrypt import generate_password_hash
from werkzeug.exceptions import NotFound

from app.database import User


def create(name: str, password: str) -> None:
    password_hash = generate_password_hash(password, 10)
    user = User(name, password_hash)
    User.save(user)


def _check_existance(user: User) -> bool:
    if not user:
        raise NotFound('The user was not found.')
    return True


def get_one_by_id(id: int) -> User:
    user = User.find_first_by_id(id)
    _check_existance(user)
    return user
