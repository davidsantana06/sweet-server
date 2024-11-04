from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


Recipes = List['Recipe']


class Recipe(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    id_category: Mapped[int] = mapped_column(
        ForeignKey('category.id'),
        nullable=False
    )
    name = Column(String(100), nullable=False)
    preparation_time = Column(Integer, nullable=False)
    description = Column(String(1000))

    category: Mapped['Category'] = relationship(back_populates='recipes')
    ingredient_rels: Mapped[List['RecipeIngredient']] = relationship(
        back_populates='recipe',
        cascade='all, delete'
    )
    material_rels: Mapped[List['RecipeMaterial']] = relationship(
        back_populates='recipe',
        cascade='all, delete'
    )
    products: Mapped[List['Product']] = relationship(
        back_populates='recipe'
    )
    
    @classmethod
    def _query_all(cls, columns: List = None, filters: List = None) -> Recipes:
        return super()._query_all(
            columns=columns,
            filters=filters,
            ordinances=[cls.name, cls.preparation_time, cls.id]
        )

    @classmethod
    def find_all(cls) -> Recipes:
        return cls._query_all()

    @classmethod
    def find_all_by_id_category(cls, id_category: int) -> Recipes:
        return cls._query_all(filters=[cls.id_category == id_category])

    @classmethod
    def find_all_by_name(cls, name: str) -> Recipes:
        return cls._query_all(filters=[cls.name.icontains(name)])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Recipe':
        return cls._query_first(filters=[cls.id == id])

    @property
    def preparation_time_in_hours(self) -> float:
        return (self.preparation_time / 60)

    @property
    def ingredients_value(self) -> float:
        return sum(
            (
                ingredient_rel.weight /
                ingredient_rel.ingredient.weight *
                ingredient_rel.ingredient.value
            )
            for ingredient_rel in self.ingredient_rels
        )

    @property
    def materials_value(self) -> float:
        return sum(
            (material_rel.material.value * material_rel.quantity)
            for material_rel in self.material_rels
        )


from .category import Category
from .product import Product
from .recipe_ingredient import RecipeIngredient
from .recipe_material import RecipeMaterial
