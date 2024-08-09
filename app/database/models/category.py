from sqlalchemy import Column, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database
from app.typing import SelectChoices

from ..inheritable import Model


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

    @staticmethod
    def save(category: 'Category') -> None:
        Model.save(category)

    @staticmethod
    def delete(category: 'Category') -> None:
        Model.delete(category)

    @classmethod
    def find_all(cls) -> Categories:
        return cls.query.order_by(Category.name).all()

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.query.with_entities(
            Category.id, 
            Category.name
        ).order_by(
            Category.name
        ).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Category':
        return cls.query.filter(Category.id == id).first()

    @classmethod
    def find_first_by_name(cls, name: str) -> 'Category':
        return cls.query.filter(Category.name == name).first()

    def __init__(self, name: str) -> None:
        self.name = name


from .recipe import Recipe
