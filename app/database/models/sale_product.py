from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database

from ..inheritable import Model


SaleProducts = List['SaleProduct']


class SaleProduct(database.Model, Model):
    id_sale: Mapped[int] = mapped_column(
        ForeignKey('sale.id'),
        nullable=False,
        primary_key=True
    )
    id_product: Mapped[int] = mapped_column(
        ForeignKey('product.id'),
        nullable=False,
        primary_key=True
    )
    quantity = Column(Integer(), nullable=False)
    unit_value = Column(Float(), nullable=False)

    sale: Mapped['Sale'] = relationship(
        back_populates='product_rels'
    )
    product: Mapped['Product'] = relationship(
        back_populates='sale_rels'
    )

    @classmethod
    def __query_all(cls, filters=[]) -> SaleProducts:
        return cls._query_all(
            filters=filters,
            ordinances=[
                SaleProduct.created_at,
                SaleProduct.unit_value,
                SaleProduct.quantity
            ]
        )

    @classmethod
    def find_all_by_id_sale(cls, id_sale: int) -> SaleProducts:
        return cls.__query_all(
            filters=[SaleProduct.id_sale == id_sale]
        )

    @classmethod
    def find_first_by_id_sale_and_id_product(
        cls,
        id_sale: int, id_product: int
    ) -> 'SaleProduct':
        return cls._query_first(
            filters=[
                SaleProduct.id_sale == id_sale,
                SaleProduct.id_product == id_product
            ]
        )

    def __init__(
        self,
        id_sale: int,
        id_product: int,
        value: float
    ) -> None:
        self.id_sale = id_sale
        self.id_product = id_product
        self.value = value


from .sale import Sale
from .product import Product
