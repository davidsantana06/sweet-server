from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database
from app.typing import RelatedIds

from ..inheritable import Model


RecipeIngredients = List['RecipeIngredient']


class RecipeIngredient(database.Model, Model):
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
    weight = Column(Integer(), nullable=False)

    recipe: Mapped['Recipe'] = relationship(
        back_populates='ingredient_rels'
    )
    ingredient: Mapped['Ingredient'] = relationship(
        back_populates='recipe_rels'
    )

    @staticmethod
    def save(recipe_ingredient: 'RecipeIngredient') -> None:
        Model.save(recipe_ingredient)

    @staticmethod
    def delete(recipe_ingredient: 'RecipeIngredient') -> None:
        Model.delete(recipe_ingredient)

    @classmethod
    def find_all_by_id_recipe(cls, id_recipe: int) -> RecipeIngredients:
        return cls.query.filter(
            RecipeIngredient.id_recipe == id_recipe
        ).order_by(
            RecipeIngredient.created_at
        ).all()
    
    @classmethod
    def find_all_related_ids_by_id_recipe(cls, id_recipe: int) -> RelatedIds:
        return cls.query.with_entities(
            RecipeIngredient.id
        ).filter(
            RecipeIngredient.id_recipe == id_recipe
        ).order_by(
            RecipeIngredient.created_at
        ).all()

    @classmethod
    def find_first_by_id_recipe_and_id_ingredient(
        cls,
        id_recipe: int, id_ingredient: int
    ) -> 'RecipeIngredient':
        return cls.query.filter(
            RecipeIngredient.id_recipe == id_recipe,
            RecipeIngredient.id_ingredient == id_ingredient
        ).first()

    def __init__(self, id_recipe: int, id_ingredient: int, weight: int) -> None:
        self.id_recipe = id_recipe
        self.id_ingredient = id_ingredient
        self.weight = weight


from .ingredient import Ingredient
from .recipe import Recipe
from .recipe_ingredient import RecipeIngredient
