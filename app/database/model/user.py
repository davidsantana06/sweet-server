from sqlalchemy import Column, Integer, String
from app.extension import database
from ..inheritable import Model, TimestampMixin


class User(database.Model, Model, TimestampMixin):
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(50), nullable=False)

    @classmethod
    def find_first(cls) -> 'User':
        return cls._query_first([cls.id == 1])
