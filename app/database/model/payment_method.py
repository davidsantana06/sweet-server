from sqlalchemy import Column, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


PaymentMethods = List['PaymentMethod']


class PaymentMethod(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(50), nullable=False)

    sales: Mapped[List['Sale']] = relationship(
        back_populates='payment_method'
    )

    @classmethod
    def _query_all(cls, columns: List = None, filters: List = None) -> PaymentMethods:
        return super()._query_all(
            columns=columns,
            filters=filters,
            ordinances=[cls.name, cls.id]
        )

    @classmethod
    def find_all(cls) -> PaymentMethods:
        return cls._query_all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'PaymentMethod':
        return cls._query_first(filters=[cls.id == id])

    @classmethod
    def find_first_by_name(cls, name: str) -> 'PaymentMethod':
        return cls._query_first(filters=[cls.name == name])

    @property
    def sales_quantity(self) -> int:
        return len(self.sales)


from .sale import Sale
