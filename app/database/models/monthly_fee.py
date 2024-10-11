from sqlalchemy import Column, Float, Integer, String
from typing import List

from app.extensions import database

from ..inheritable import Model


MonthlyFees = List['MonthlyFee']


class MonthlyFee(database.Model, Model):
    id = Column(
        Integer(),
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(100), nullable=False)
    value = Column(Float(), nullable=False)
    description = Column(String(1000))
    
    @classmethod
    def __query_all(cls, filters=[]) -> MonthlyFees:
        return cls._query_all(
            filters=filters,
            ordinances=[
                MonthlyFee.name, 
                MonthlyFee.value, 
                MonthlyFee.id
            ]
        )

    @classmethod
    def find_all(cls) -> MonthlyFees:
        return cls.__query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> MonthlyFees:
        return cls.__query_all(
            filters=[MonthlyFee.name.icontains(name)]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'MonthlyFee':
        return cls._query_first(filters=[MonthlyFee.id == id])

    def __init__(
        self, 
        name: str, 
        description: str, 
        value: float
    ) -> None:
        self.name = name
        self.description = description
        self.value = value

    @property
    def hourly_rate(self) -> float:
        return (self.value / 730.56)
