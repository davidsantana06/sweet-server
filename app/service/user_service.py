from typing import Dict

from app.database import User
from app.exception import UserNotFound


def create(data: Dict[str, object]) -> User:
    user = User(**data)
    User.save(user)
    return user


def get_one() -> User:
    user = User.find_first()
    if not user: raise UserNotFound()
    return user


def update(data: Dict[str, object]) -> User:
    user = get_one()
    user.update(**data)
    User.save(user)
    return user
