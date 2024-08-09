from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from typing import Dict, List

from app.extensions import database

from ..inheritable import Model


Users = List['User']


class User(database.Model, Model, UserMixin):
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(30), nullable=False)
    password = Column(String(60), nullable=False)

    @staticmethod
    def save(user: 'User') -> None:
        Model.save(user)

    @staticmethod
    def delete(user: 'User') -> None:
        Model.delete(user)

    @classmethod
    def find_all(cls) -> Users:
        return cls.query.order_by(User.nickname).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'User':
        return cls.query.filter(User.id == id).first()

    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.password = password

    def to_dict(self) -> Dict[str, object]:
        return {'id': self.id, 'name': self.name}
