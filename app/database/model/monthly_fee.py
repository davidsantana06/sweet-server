from sqlalchemy import Column, Float, Integer, String
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


MonthlyFees = List['MonthlyFee']


class MonthlyFee(database.Model, Model, TimestampMixin):
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(100), nullable=False)
    value = Column(Float, nullable=False)
    description = Column(String(1000))
    
    @classmethod
    def _query_all(cls, filters: List = None) -> MonthlyFees:
        return super()._query_all(
            filters=filters,
            ordinances=[cls.name, cls.value, cls.id]
        )

    @classmethod
    def find_all(cls) -> MonthlyFees:
        return cls._query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> MonthlyFees:
        return cls._query_all(filters=[cls.name.icontains(name)])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'MonthlyFee':
        return cls._query_first(filters=[cls.id == id])

    @property
    def hourly_rate(self) -> float:
        return (self.value / 730.56)
