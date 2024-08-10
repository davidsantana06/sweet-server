from sqlalchemy import Column, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database
from app.typing import SelectChoices

from ..inheritable import Model


Customers = List['Customer']


class Customer(database.Model, Model):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(100), nullable=False)
    phone = Column(String(15))
    instagram = Column(String(31))
    notes = Column(String(1000))

    purchases: Mapped[List['Sale']] = relationship(
        back_populates='customer', 
        cascade='all, delete'
    )

    @staticmethod
    def save(customer: 'Customer') -> None:
        Model.save(customer)

    @staticmethod
    def delete(customer: 'Customer') -> None:
        Model.delete(customer)

    @classmethod
    def find_all(cls) -> Customers:
        return cls.query.order_by(
            Customer.name,
            Customer.instagram,
            Customer.phone
        ).all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Customers:
        return cls.query.filter(
            Customer.name.icontains(name)
        ).order_by(
            Customer.name,
            Customer.instagram,
            Customer.phone
        ).all()

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.query.with_entities(
            Customer.id, 
            Customer.name
        ).order_by(
            Customer.name,
            Customer.instagram,
            Customer.phone
        ).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Labor':
        return cls.query.filter(Customer.id == id).first()

    def __init__(self, name: str, phone: str, instagram: str, notes: str) -> None:
        self.name = name
        self.phone = phone
        self.instagram = instagram
        self.notes = notes


from .labor import Labor
from .sale import Sale
