from sqlalchemy import Column, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


Customers = List['Customer']


class Customer(database.Model, Model, TimestampMixin):
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
    
    @classmethod
    def __query_all(cls, columns: List = None, filters: List = None) -> Customers:
        return cls._query_all(
            columns=columns,
            filters=filters,
            ordinances=[cls.name, cls.phone, cls.instagram, cls.id]
        )

    @classmethod
    def find_all(cls) -> Customers:
        return cls.__query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Customers:
        return cls.__query_all(filters=[cls.name.icontains(name)])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Customer':
        return cls._query_first(filters=[cls.id == id])


from .sale import Sale
