from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


SaleProducts = List['SaleProduct']


class SaleProduct(database.Model, Model, TimestampMixin):
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
    def find_all_by_id_sale(cls, id_sale: int) -> SaleProducts:
        return cls._query_all(
            filters=[cls.id_sale == id_sale],
            ordinances=[cls.created_at, cls.unit_value, cls.quantity]
        )

    @classmethod
    def find_first_by_ids(
        cls,
        id_sale: int, 
        id_product: int
    ) -> 'SaleProduct':
        return cls._query_first(
            filters=[cls.id_sale == id_sale, cls.id_product == id_product]
        )


from .sale import Sale
from .product import Product
