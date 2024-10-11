from sqlalchemy import (
    Column, Float, ForeignKey, Integer,
    desc
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import Dict, List

from app.extensions import database

from ..inheritable import Model


Sales = List['Sale']


class Sale(database.Model, Model):
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
    freight = Column(Float(), nullable=False)
    discount = Column(Float(), nullable=False)
    status = Column(Integer(), nullable=False, default=1)

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
        return cls._query_all(
            ordinances=[desc(Sale.id)]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Sale':
        return cls._query_first(filters=[Sale.id == id])

    def __init__(
        self,
        id_customer: int, id_payment_method: int,
        freight: float, discount: float
    ) -> None:
        self.id_customer = id_customer
        self.id_payment_method = id_payment_method
        self.freight = freight
        self.discount = discount

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
    
    def to_dict(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'id_customer': self.id_customer,
            'id_payment_method': self.id_payment_method,
            'freight': self.freight,
            'discount': self.discount,
            'status': self.status,
            'products_value': self.products_value,
            'sub_total': self.sub_total,
            'total': self.total
        }


from .customer import Customer
from .payment_method import PaymentMethod
from .sale_product import SaleProduct
