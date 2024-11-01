from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


RecipeIngredients = List['RecipeIngredient']


class RecipeIngredient(database.Model, Model, TimestampMixin):
    id_recipe: Mapped[int] = mapped_column(
        ForeignKey('recipe.id'),
        nullable=False,
        primary_key=True
    )
    id_ingredient: Mapped[int] = mapped_column(
        ForeignKey('ingredient.id'),
        nullable=False,
        primary_key=True
    )
    weight = Column(Integer, nullable=False)

    recipe: Mapped['Recipe'] = relationship(
        back_populates='ingredient_rels'
    )
    ingredient: Mapped['Ingredient'] = relationship(
        back_populates='recipe_rels'
    )

    @classmethod
    def _query_all(cls, filters: List = None) -> RecipeIngredients:
        return super()._query_all(
            filters=filters,
            ordinances=[cls.created_at, cls.weight]
        )

    @classmethod
    def find_all_by_id_recipe(cls, id_recipe: int) -> RecipeIngredients:
        return cls._query_all(filters=[cls.id_recipe == id_recipe])
    
    @classmethod
    def find_first_by_ids(
        cls,
        id_recipe: int, 
        id_ingredient: int
    ) -> 'RecipeIngredient':
        return cls._query_first(
            filters=[
                cls.id_recipe == id_recipe,
                cls.id_ingredient == id_ingredient
            ]
        )


from .ingredient import Ingredient
from .recipe import Recipe
from .recipe_ingredient import RecipeIngredient
