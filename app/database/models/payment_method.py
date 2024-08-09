from sqlalchemy import Column, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import Dict, List

from app.extensions import database
from app.typing import SelectChoices

from ..inheritable import Model


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

    @staticmethod
    def save(payment_method: 'PaymentMethod') -> None:
        Model.save(payment_method)

    @staticmethod
    def delete(payment_method: 'PaymentMethod') -> None:
        Model.delete(payment_method)

    @classmethod
    def find_all(cls) -> PaymentMethods:
        return cls.query.order_by(PaymentMethod.name).all()

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.query.with_entities(
            PaymentMethod.id, 
            PaymentMethod.name
        ).order_by(
            PaymentMethod.name
        ).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Labor':
        return cls.query.filter(PaymentMethod.id == id).first()

    @classmethod
    def find_first_by_name(cls, name: str) -> 'PaymentMethod':
        return cls.query.filter(PaymentMethod.name == name).first()
    
    @property
    def sales_quantity(self) -> int:
        return self.sales.__len__

    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self)-> Dict[str, object]:
        return {
            'id': self.id, 
            'name': self.name, 
            'sales_quantity': self.sales_quantity
        }


from .labor import Labor
from .sale import Sale
