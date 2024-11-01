from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


Sales = List['Sale']


class Sale(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    id_customer: Mapped[int] = mapped_column(
        ForeignKey('customer.id'),
        nullable=False
    )
    id_payment_method: Mapped[int] = mapped_column(
        ForeignKey('payment_method.id'),
        nullable=False
    )
    freight = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    completed = Column(Integer, nullable=False, default=0)

    customer: Mapped['Customer'] = relationship(
        back_populates='purchases'
    )
    payment_method: Mapped['PaymentMethod'] = relationship(
        back_populates='sales'
    )
    product_rels: Mapped[List['SaleProduct']] = relationship(
        back_populates='sale', 
        cascade='all, delete'
    )

    @classmethod
    def find_all(cls) -> Sales:
        return cls._query_all(ordinances=[cls.id.desc()])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Sale':
        return cls._query_first(filters=[cls.id == id])

    @property
    def products_value(self) -> float:
        return sum(
            (product_rel.quantity * product_rel.unit_value)
            for product_rel in self.product_rels
        )

    @property
    def sub_total(self) -> float:
        return (self.products_value + self.freight)

    @property
    def total(self) -> float:
        return (self.sub_total - self.discount)


from .customer import Customer
from .payment_method import PaymentMethod
from .sale_product import SaleProduct
