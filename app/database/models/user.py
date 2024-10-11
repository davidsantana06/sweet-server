from flask_login import UserMixin
from sqlalchemy import Column, ColumnElement, Integer, String
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
    nickname = Column(String(15), unique=True, nullable=False)
    password = Column(String(60), nullable=False)

    @classmethod
    def __compose_filters(
        cls,
        except_super: bool,
        filters=[],
    ) -> List[ColumnElement[bool]]:
        return (filters + [User.id != 1]) if except_super else filters

    @classmethod
    def __query_all(cls, except_super: bool, filters=[]) -> Users:
        return cls._query_all(
            filters=cls.__compose_filters(except_super, filters),
            ordinances=[
                User.name,
                User.nickname,
                User.id
            ]
        )

    @classmethod
    def find_all_except_super(cls) -> Users:
        return cls.__query_all(except_super=True)

    @classmethod
    def find_all_by_name_except_super(cls, name: str) -> Users:
        return cls.__query_all(
            except_super=True,
            filters=[User.name.icontains(name)]
        )

    @classmethod
    def find_first_by_nickname(cls, nickname: str) -> 'User':
        return cls._query_first(
            filters=[User.nickname == nickname]
        )

    @classmethod
    def find_first_by_id(cls, id: int, except_super: bool) -> 'User':
        return cls._query_first(
            filters=cls.__compose_filters(
                except_super,
                [User.id == id]
            )
        )

    def __init__(
        self,
        name: str,
        nickname: str,
        password: str
    ) -> None:
        self.name = name
        self.nickname = nickname
        self.password = password

    def to_dict(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname
        }
