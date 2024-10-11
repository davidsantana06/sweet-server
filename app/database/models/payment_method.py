from sqlalchemy import Column, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import Dict, List

from app.extensions import database

from ..inheritable import Model
from ..typing import SelectChoices


PaymentMethods = List['PaymentMethod']


class PaymentMethod(database.Model, Model):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(100), nullable=False)

    sales: Mapped[List['Sale']] = relationship(
        back_populates='payment_method'
    )
    
    @classmethod
    def __query_all(cls, columns=[], filters=[]) -> PaymentMethods:
        return cls._query_all(
            columns=columns,
            filters=filters,
            ordinances=[
                PaymentMethod.name, 
                PaymentMethod.id
            ]
        )

    @classmethod
    def find_all(cls) -> PaymentMethods:
        return cls.__query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> PaymentMethods:
        return cls.__query_all(
            filters=[PaymentMethod.name.icontains(name)]
        )

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.__query_all(
            columns=[
                PaymentMethod.id, 
                PaymentMethod.name
            ]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'PaymentMethod':
        return cls._query_first(filters=[PaymentMethod.id == id])

    @classmethod
    def find_first_by_name(cls, name: str) -> 'PaymentMethod':
        return cls._query_first(filters=[PaymentMethod.name == name])
    
    @property
    def sales_quantity(self) -> int:
        return len(self.sales)

    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self)-> Dict[str, object]:
        return {
            'id': self.id, 
            'name': self.name, 
            'sales_quantity': self.sales_quantity
        }


from .sale import Sale
