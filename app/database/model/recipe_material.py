from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


RecipeMaterials = List['RecipeMaterial']


class RecipeMaterial(database.Model, Model, TimestampMixin):
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
    quantity = Column(Integer, nullable=False)

    recipe: Mapped['Recipe'] = relationship(
        back_populates='material_rels'
    )
    material: Mapped['Material'] = relationship(
        back_populates='recipe_rels'
    )

    @classmethod
    def _query_all(cls, filters: List = None) -> RecipeMaterials:
        return super()._query_all(
            filters=filters,
            ordinances=[cls.created_at, cls.quantity]
        )

    @classmethod
    def find_all_by_id_recipe(
        cls, 
        id_recipe: int,
        only_id_material: bool
    ) -> RecipeMaterials:
        return cls._query_all(
            columns=[cls.id_material] if only_id_material else None,
            filters=[cls.id_recipe == id_recipe]
        )

    @classmethod
    def find_first_by_ids(
        cls,
        id_recipe: int, 
        id_material: int
    ) -> 'RecipeMaterial':
        return cls._query_first(
            filters=[
                cls.id_recipe == id_recipe,
                cls.id_material == id_material
            ]
        )


from .recipe import Recipe
from .material import Material
