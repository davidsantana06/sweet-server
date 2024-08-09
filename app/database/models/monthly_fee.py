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

    @staticmethod
    def save(monthlyFee: 'MonthlyFee') -> None:
        Model.save(monthlyFee)

    @staticmethod
    def delete(monthlyFee: 'MonthlyFee') -> None:
        Model.delete(monthlyFee)

    @classmethod
    def find_all(cls) -> MonthlyFees:
        return cls.query.order_by(
            MonthlyFee.name, 
            MonthlyFee.value
        ).all()

    @classmethod
    def find_all_by_name(cls, name: str) -> MonthlyFees:
        return cls.query.filter(
            MonthlyFee.name.icontains(name)
        ).order_by(
            MonthlyFee.name, 
            MonthlyFee.value
        ).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'MonthlyFee':
        return cls.query.filter(MonthlyFee.id == id).first()

    def __init__(self, name: str, description: str, value: float) -> None:
        self.name = name
        self.description = description
        self.value = value

    @property
    def hourly_rate(self) -> float:
        return (self.value / 730.56)
