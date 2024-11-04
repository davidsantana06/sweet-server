from app.database import User
from app.exception import UserNotFound
from app.schema import UserSchema


def create(data: UserSchema) -> User:
    user = User(**data)
    User.save(user)
    return user


def get_one() -> User:
    user = User.find_first()
    if not user: raise UserNotFound()
    return user


def update(data: UserSchema) -> User:
    user = get_one()
    user.update(**data)
    User.save(user)
    return user
