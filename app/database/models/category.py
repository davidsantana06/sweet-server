from sqlalchemy import Column, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database

from ..inheritable import Model
from ..typing import SelectChoices


Categories = List['Category']


class Category(database.Model, Model):
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
    def __query_all(cls, columns=[], filters=[]) -> Categories:
        return cls._query_all(
            columns=columns,
            filters=filters,
            ordinances=[
                Category.name,
                Category.id
            ]
        )

    @classmethod
    def find_all(cls) -> Categories:
        return cls.__query_all()
    
    @classmethod
    def find_all_by_name(cls, name: str) -> Categories:
        return cls.__query_all(
            filters=[Category.name.icontains(name)]
        )

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.__query_all(
            columns=[
                Category.id,
                Category.name
            ]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Category':
        return cls._query_first(filters=[Category.id == id])

    @classmethod
    def find_first_by_name(cls, name: str) -> 'Category':
        return cls._query_first(filters=[Category.name == name])

    def __init__(self, name: str) -> None:
        self.name = name


from .recipe import Recipe
