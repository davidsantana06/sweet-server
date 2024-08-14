from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database
from app.typing import RelatedIds

from ..inheritable import Model


RecipeMaterials = List['RecipeMaterial']


class RecipeMaterial(database.Model, Model):
    id_recipe: Mapped[int] = mapped_column(
        ForeignKey('recipe.id'),
        nullable=False,
        primary_key=True
    )
    id_material: Mapped[int] = mapped_column(
        ForeignKey('material.id'),
        nullable=False,
        primary_key=True
    )
    quantity = Column(Integer(), nullable=False)

    recipe: Mapped['Recipe'] = relationship(
        back_populates='material_rels'
    )
    material: Mapped['Material'] = relationship(
        back_populates='recipe_rels'
    )

    @staticmethod
    def save(recipe_material: 'RecipeMaterial') -> None:
        Model.save(recipe_material)

    @staticmethod
    def delete(recipe_material: 'RecipeMaterial') -> None:
        Model.delete(recipe_material)

    @classmethod
    def __query_all(cls, filters=[]) -> RecipeMaterials:
        return cls._query_all(
            filters=filters,
            ordinances=[
                RecipeMaterial.created_at, 
                RecipeMaterial.quantity
            ]
        )

    @classmethod
    def find_all_by_id_recipe(cls, id_recipe: int) -> RecipeMaterials:
        return cls.__query_all(filters=[RecipeMaterial.id_recipe == id_recipe])
    
    @classmethod
    def find_all_related_ids_by_id_recipe(cls, id_recipe: int) -> RelatedIds:
        return cls.__query_all(
            columns=[RecipeMaterial.id],
            filters=[RecipeMaterial.id_recipe == id_recipe]
        )

    @classmethod
    def find_first_by_id_recipe_and_id_material(
        cls,
        id_recipe: int, id_material: int
    ) -> 'RecipeMaterial':
        cls._query_first(
            filters=[
                RecipeMaterial.id_recipe == id_recipe,
                RecipeMaterial.id_material == id_material
            ]
        )

    def __init__(self, id_recipe: int, id_material: int, quantity: int) -> None:
        self.id_recipe = id_recipe
        self.id_material = id_material
        self.quantity = quantity


from .material import Material
from .recipe import Recipe
