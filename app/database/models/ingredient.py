from sqlalchemy import Column, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database

from ..inheritable import Resource
from ..typing import RelatedIds, SelectChoices


Ingredients = List['Ingredient']


class Ingredient(database.Model, Resource):
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
    
    @classmethod
    def __query_all(cls, columns=[], filters=[]) -> Ingredients:
        return cls._query_all(
            columns=columns,
            filters=filters,
            ordinances=[
                Ingredient.name, 
                Ingredient.brand, 
                Ingredient.supplier, 
                Ingredient.value,
                Ingredient.weight,
                Ingredient.current_quantity,
                Ingredient.minimum_quantity,
                Ingredient.id
            ]
        )

    @classmethod
    def find_all(cls) -> Ingredients:
        return cls.__query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Ingredients:
        return cls.__query_all(
            filters=[Ingredient.name.icontains(name)]
        )

    @classmethod
    def find_all_select_choices_not_related_to_recipe(
        cls,
        related_ids: RelatedIds
    ) -> SelectChoices:
        return cls.__query_all(
            columns=[
                Ingredient.id, 
                Ingredient.name
            ],
            filters=[Ingredient.id.not_in(related_ids)]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Ingredient':
        return cls._query_first(filters=[Ingredient.id == id])

    def __init__(
        self,
        name: str, brand: str, supplier: str,
        weight: int, value: float,
        current_quantity: float, minimum_quantity: int
    ) -> None:
        Resource.__init__(
            self,
            name, brand, supplier, value,
            current_quantity, minimum_quantity
        )
        self.weight = weight


from .recipe_ingredient import RecipeIngredient
