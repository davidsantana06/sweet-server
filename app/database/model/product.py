from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


Products = List['Product']


class Product(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        Integer,
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
    loss_margin = Column(Float, nullable=False)
    contribuition_margin = Column(Float, nullable=False)

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
    def _query_all(cls, columns: List = None, filters: List = None) -> Products:
        return super()._query_all(
            columns=columns,
            filters=filters,
            ordinances=[
                cls.name, 
                cls.contribuition_margin, 
                cls.loss_margin, 
                cls.id
            ]
        )

    @classmethod
    def find_all(cls) -> Products:
        return cls._query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Products:
        return cls._query_all(filters=[cls.name.icontains(name)])

    @classmethod
    def find_all_except(cls, ids: List[int]) -> Products:
        return cls._query_all(filters=[cls.id.not_in(ids)])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Product':
        return cls._query_first(filters=[cls.id == id])

    @property
    def monthly_fees_value(self) -> float:
        return sum(
            (monthly_fee.hourly_rate * self.recipe.preparation_time_in_hours)
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
        return self.cost_value * (self.loss_margin / 10)

    @property
    def contribuition_value(self) -> float:
        return self.cost_value * (self.contribuition_margin / 10)

    @property
    def sell_value(self) -> float:
        return self.cost_value - self.loss_value + self.contribuition_value


from .collaborator import Collaborator
from .monthly_fee import MonthlyFee
from .recipe import Recipe
from .sale_product import SaleProduct
