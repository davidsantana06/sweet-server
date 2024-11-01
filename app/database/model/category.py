from sqlalchemy import Column, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


Categories = List['Category']


class Category(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(100), nullable=False)

    recipes: Mapped[List['Recipe']] = relationship(
        back_populates='category'
    )

    @classmethod
    def _query_all(
        cls, 
        columns: List = None, 
        filters: List = None
    ) -> Categories:
        return super()._query_all(
            columns=columns,
            filters=filters,
            ordinances=[cls.name, cls.id]
        )

    @classmethod
    def find_all(cls) -> Categories:
        return cls._query_all()
    
    @classmethod
    def find_all_by_name(cls, name: str) -> Categories:
        return cls._query_all(filters=[cls.name.icontains(name)])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Category':
        return cls._query_first(filters=[cls.id == id])

    @classmethod
    def find_first_by_name(cls, name: str) -> 'Category':
        return cls._query_first(filters=[cls.name == name])


from .recipe import Recipe
