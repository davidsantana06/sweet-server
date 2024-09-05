from flask_bcrypt import generate_password_hash
from flask_login import current_user
from werkzeug.exceptions import NotFound, Unauthorized

from app.database import User, Users

from .forms import UpdateForm


def create(name: str, nickname: str, password: str) -> None:
    password_hash = generate_password_hash(password, 10)
    user = User(name, nickname, password_hash)
    User.save(user)
    return user


def get_all() -> Users:
    return User.find_all_except_super()


def get_all_by_name(name: str) -> Users:
    return User.find_all_by_name_except_super(name)


def get_current() -> User:
    return current_user


def get_one_by_nickname(nickname: str) -> User:
    user = User.find_first_by_nickname(nickname)
    _check_existance(user)
    return user


def get_one_by_id(id: int, except_super: bool = True) -> User:
    user = User.find_first_by_id(id, except_super)
    _check_existance(user)
    print(user.to_dict())
    return user


def update(user: User, form: UpdateForm) -> User:
    form.populate_obj(user)
    user = User.save(user)
    return user


def delete(user: User) -> None:
    User.delete(user)


def check_acess(is_super: bool, is_self: bool, id: int) -> bool:
    is_super = is_super and current_user.id == 1
    is_self = is_self and current_user.id == id
    if not (is_super or is_self):
        raise Unauthorized(
            'You do not have the required acess to manage users.'
        )
    return True


def _check_existance(user: User) -> bool:
    if not user:
        raise NotFound('The user was not found.')
    return True
