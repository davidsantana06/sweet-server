from flask_bcrypt import generate_password_hash
from flask_login import current_user
from typing import Literal, Union
from werkzeug.exceptions import NotFound

from app.database import User, Users

from .forms import UserForm


def check_acess(is_super: bool, is_self: bool, id: int) -> bool:
    is_super = is_super and current_user.id == 1
    is_self = is_self and current_user.id == id
    return (is_super or is_self)


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


def get_one_by(
    field: Literal['id', 'nickname'],
    value: Union[int, str],
    except_super: bool = True
) -> User:
    function = {
        'id': (lambda v: User.find_first_by_id(v, except_super)),
        'nickname': (lambda v: User.find_first_by_nickname(v))
    }[field]
    user = function(value)
    if not user:
        raise NotFound('The user was not found.')
    return user


def update(user: User, form: UserForm) -> User:
    form.populate_obj(user)
    user = User.save(user)
    return user


def delete(user: User) -> None:
    User.delete(user)
