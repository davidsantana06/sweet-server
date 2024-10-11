from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import Dict, List

from app.extensions import database

from ..inheritable import Model
from ..typing import RelatedIds, SelectChoices


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
    id_collaborator: Mapped[int] = mapped_column(
        ForeignKey('collaborator.id'),
        nullable=False
    )
    name = Column(String(100), nullable=False)
    loss_margin = Column(Float(), nullable=False)
    contribuition_margin = Column(Float(), nullable=False)

    recipe: Mapped['Recipe'] = relationship(
        back_populates='products'
    )
    collaborator: Mapped['Collaborator'] = relationship(
        back_populates='products'
    )
    sale_rels: Mapped[List['SaleProduct']] = relationship(
        back_populates='product',
        cascade='all, delete'
    )

    @classmethod
    def __query_all(cls, columns=[], filters=[]) -> Products:
        return cls._query_all(
            columns=columns,
            filters=filters,
            ordinances=[
                Product.name,
                Product.contribuition_margin,
                Product.loss_margin,
                Product.id
            ]
        )

    @classmethod
    def find_all(cls) -> Products:
        return cls.__query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Products:
        return cls.__query_all(
            filters=[Product.name.icontains(name)]
        )

    @classmethod
    def find_all_select_choices_not_related_to_sale(
        cls, related_ids: RelatedIds
    ) -> SelectChoices:
        return cls.__query_all(
            columns=[
                Product.id,
                Product.name
            ],
            filters=[Product.id.not_in(related_ids)]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Product':
        return cls._query_first(filters=[Product.id == id])

    def __init__(
        self,
        id_recipe: int, id_collaborator: int, name: str,
        loss_margin: float, contribuition_margin: float
    ) -> None:
        self.id_recipe = id_recipe
        self.id_collaborator = id_collaborator
        self.name = name
        self.loss_margin = loss_margin
        self.contribuition_margin = contribuition_margin

    @property
    def monthly_fees_value(self) -> float:
        return sum(
            (
                monthly_fee.hourly_rate * 
                self.recipe.preparation_time_in_hours
            )
            for monthly_fee in MonthlyFee.find_all()
        )

    @property
    def collaborator_value(self) -> float:
        return (
            self.collaborator.hourly_rate * 
            self.recipe.preparation_time_in_hours
        )

    @property
    def cost_value(self) -> float:
        return (
            self.monthly_fees_value + 
            self.recipe.ingredients_value + 
            self.recipe.materials_value + 
            self.collaborator_value
        )

    @property
    def loss_value(self) -> float:
        return (self.cost_value * (self.loss_margin / 10))

    @property
    def contribuition_value(self) -> float:
        return (self.cost_value * (self.contribuition_margin / 10))

    @property
    def sell_value(self) -> float:
        return (
            self.cost_value - 
            self.loss_value + 
            self.contribuition_value
        )
    
    def to_dict(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'id_recipe': self.id_recipe,
            'id_collaborator': self.id_collaborator,
            'name': self.name,
            'loss_margin': self.loss_margin,
            'contribuition_margin': self.contribuition_margin,
            'monthly_fees_value': self.monthly_fees_value,
            'collaborator_value': self.collaborator_value,
            'cost_value': self.cost_value,
            'loss_value': self.loss_value,
            'contribuition_value': self.contribuition_value,
            'sell_value': self.sell_value
        }


from .collaborator import Collaborator
from .monthly_fee import MonthlyFee
from .recipe import Recipe
from .sale_product import SaleProduct
