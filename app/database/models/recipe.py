from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import Dict, List

from app.extensions import database
from app.typing import SelectChoices

from ..inheritable import Model


Recipes = List['Recipe']


class Recipe(database.Model, Model):
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
    preparation_time = Column(Integer(), nullable=False)
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

    @staticmethod
    def save(recipe: 'Recipe') -> None:
        Model.save(recipe)

    @staticmethod
    def delete(recipe: 'Recipe') -> None:
        Model.delete(recipe)

    @classmethod
    def find_all_by_name(cls, name: str) -> Recipes:
        return cls.query.filter(
            Recipe.name.icontains(name)
        ).order_by(
            Recipe.name
        ).all()

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.query.with_entities(
            Recipe.id, 
            Recipe.name
        ).order_by(
            Recipe.name
        ).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Recipe':
        return cls.query.filter(Recipe.id == id).first()

    def __init__(
        self,
        id_category: int, name: str,
        preparation_time: int, description: str
    ) -> None:
        self.id_category = id_category
        self.name = name
        self.preparation_time = preparation_time
        self.description = description

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

    @property
    def preparation_time_in_hours(self) -> float:
        return (self.preparation_time / 60)
    
    def to_dict(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'id_category': self.id_category,
            'name': self.name,
            'preparation_time': self.preparation_time,
            'description': self.description,
            'ingredients_value': self.ingredients_value,
            'materials_value': self.materials_value,
            'preparation_time_in_hours': self.preparation_time_in_hours
        }


from .category import Category
from .product import Product
from .recipe_ingredient import RecipeIngredient
from .recipe_material import RecipeMaterial
