from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import Dict, List

from app.extensions import database
from app.typing import SelectChoices

from ..inheritable import Model


Products = List['Product']


class Product(database.Model, Model):
    id: Mapped[int] = mapped_column(
        Integer(),
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    id_recipe: Mapped[int] = mapped_column(
        ForeignKey('recipe.id'),
        nullable=False
    )
    id_labor: Mapped[int] = mapped_column(
        ForeignKey('labor.id'),
        nullable=False
    )
    loss_margin = Column(Float(), nullable=False)
    contribuition_margin = Column(Float(), nullable=False)

    recipe: Mapped['Recipe'] = relationship(
        back_populates='products'
    )
    labor: Mapped['Labor'] = relationship(
        back_populates='products'
    )
    sale_rels: Mapped[List['SaleProduct']] = relationship(
        back_populates='product',
        cascade='all, delete'
    )

    @staticmethod
    def save(product: 'Product') -> None:
        Model.save(product)

    @staticmethod
    def delete(product: 'Product') -> None:
        Model.delete(product)

    @classmethod
    def find_all_by_name(cls, name: str) -> Products:
        return cls.query.join(
            Product.recipe
        ).join(
            Recipe.category
        ).filter(
            Recipe.name.icontains(name)
        ).order_by(
            Recipe.name, 
            Category.name
        ).all()

    @classmethod
    def find_all_select_choices_not_related_to_sell(
        cls, related_product_ids: List[int]
    ) -> SelectChoices:
        return cls.query.with_entities(
            Product.id, 
            Product.name
        ).filter(
            Product.id.not_in(related_product_ids)
        ).order_by(
            Product.name
        ).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Product':
        return cls.query.filter(Product.id == id).first()

    def __init__(
        self,
        id_recipe: int, id_labor: int,
        loss_margin: float, contribuition_margin: float
    ) -> None:
        self.id_recipe = id_recipe
        self.id_labor = id_labor
        self.loss_margin = loss_margin
        self.contribuition_margin = contribuition_margin

    @property
    def monthly_fees_value(self) -> float:
        return sum(
            (monthly_fee.hourly_rate * self.recipe.preparation_time_in_hours)
            for monthly_fee in MonthlyFee.find_all()
        )

    @property
    def labor_value(self) -> float:
        return (self.labor.hourly_rate * self.recipe.preparation_time_in_hours)

    @property
    def cost_value(self) -> float:
        return (
            self.monthly_fees_value + 
            self.recipe.ingredients_value + 
            self.recipe.materials_value + self.labor_value
        )

    @property
    def loss_value(self) -> float:
        return (self.cost_value * (self.loss_margin / 10))

    @property
    def contribuition_value(self) -> float:
        return (self.cost_value * (self.contribuition_margin / 10))

    @property
    def sell_value(self) -> float:
        return (self.cost_value - self.loss_value + self.contribuition_value)
    
    def to_dict(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'id_recipe': self.id_recipe,
            'id_labor': self.id_labor,
            'loss_margin': self.loss_margin,
            'contribuition_margin': self.contribuition_margin,
            'monthly_fees_value': self.monthly_fees_value,
            'labor_value': self.labor_value,
            'cost_value': self.cost_value,
            'loss_value': self.loss_value,
            'contribuition_value': self.contribuition_value,
            'sell_value': self.sell_value
        }


from .category import Category
from .labor import Labor
from .monthly_fee import MonthlyFee
from .recipe import Recipe
from .sale_product import SaleProduct
