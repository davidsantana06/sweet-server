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
    def find_all_by_id_recipe(cls, id_recipe: int) -> RecipeMaterials:
        return cls.query.filter(
            RecipeMaterial.id_recipe == id_recipe
        ).order_by(
            RecipeMaterial.created_at
        ).all()
    
    @classmethod
    def find_all_related_ids_by_id_recipe(cls, id_recipe: int) -> RelatedIds:
        return cls.query.with_entities(
            RecipeMaterial.id
        ).filter(
            RecipeMaterial.id_recipe == id_recipe
        ).order_by(
            RecipeMaterial.created_at
        ).all()

    @classmethod
    def find_first_by_id_recipe_and_id_material(
        cls,
        id_recipe: int, id_material: int
    ) -> 'RecipeMaterial':
        return cls.query.filter(
            RecipeMaterial.id_recipe == id_recipe,
            RecipeMaterial.id_material == id_material
        ).first()

    def __init__(self, id_recipe: int, id_material: int, quantity: int) -> None:
        self.id_recipe = id_recipe
        self.id_material = id_material
        self.quantity = quantity


from .material import Material
from .recipe import Recipe
