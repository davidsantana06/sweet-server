from sqlalchemy import Column, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database
from app.typing import SelectChoices

from ..inheritable import Model, Resource


Ingredients = List['Ingredient']


class Ingredient(database.Model, Model, Resource):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    weight = Column(Integer(), nullable=False)

    recipe_rels: Mapped[List['RecipeIngredient']] = relationship(
        back_populates='ingredient',
        cascade='all, delete'
    )

    @staticmethod
    def save(ingredient: 'Ingredient') -> None:
        Model.save(ingredient)

    @staticmethod
    def delete(ingredient: 'Ingredient') -> None:
        Model.delete(ingredient)

    @classmethod
    def find_all_by_name(cls, name: str) -> Ingredients:
        return cls.query.filter(
            Ingredient.name.icontains(name)
        ).order_by(
            Ingredient.name, 
            Ingredient.brand,
            Ingredient.supplier, 
            Ingredient.value
        ).all()

    @classmethod
    def find_all_select_choices_not_related_to_recipe(
        cls,
        related_recipe_ids: List[int]
    ) -> SelectChoices:
        return cls.query.with_entities(
            Ingredient.id, 
            Ingredient.name
        ).filter(
            Ingredient.id.not_in(related_recipe_ids)
        ).order_by(
            Ingredient.name
        ).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Ingredient':
        return cls.query.filter(Ingredient.id == id).first()

    def __init__(
        self,
        name: str, brand: str, supplier: str,
        weight: int, value: float,
        current_quantity: float, minimum_quantity: int
    ) -> None:
        Resource.__init__(
            self,
            name, brand, supplier,
            value,
            current_quantity, minimum_quantity
        )
        self.weight = weight


from .recipe_ingredient import RecipeIngredient
