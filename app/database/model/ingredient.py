from sqlalchemy import Column, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, ResourceMixin, TimestampMixin


Ingredients = List['Ingredient']


class Ingredient(database.Model, Model, ResourceMixin, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    weight = Column(Integer, nullable=False)

    recipe_rels: Mapped[List['RecipeIngredient']] = relationship(
        back_populates='ingredient',
        cascade='all, delete'
    )

    @classmethod
    def _query_all(
        cls,
        columns: List = None,
        filters: List = None
    ) -> Ingredients:
        return super()._query_all(
            columns=columns,
            filters=filters,
            ordinances=[
                cls.name,
                cls.brand,
                cls.supplier,
                cls.value,
                cls.weight,
                cls.current_quantity,
                cls.minimum_quantity,
                cls.id
            ]
        )

    @classmethod
    def find_all(cls) -> Ingredients:
        return cls._query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Ingredients:
        return cls._query_all(filters=[cls.name.icontains(name)])

    @classmethod
    def find_all_except(cls, ids: List[int]) -> Ingredients:
        return cls._query_all(filters=[cls.id.not_in(ids)])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Ingredient':
        return cls._query_first(filters=[cls.id == id])


from .recipe_ingredient import RecipeIngredient
