from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database
from app.typing import SelectChoices

from ..inheritable import Model


Labors = List['Labor']


class Labor(database.Model, Model):
    id: Mapped[int] = mapped_column(
        Integer(),
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    person_name = Column(String(100), nullable=False)
    hourly_rate = Column(Float(), nullable=False)
    description = Column(String(1000))

    products: Mapped[List['Product']] = relationship(
        back_populates='labor'
    )

    @staticmethod
    def save(labor: 'Labor') -> None:
        Model.save(labor)

    @staticmethod
    def delete(labor: 'Labor') -> None:
        Model.delete(labor)

    @classmethod
    def find_all_except_default(cls) -> Labors:
        return cls.query.filter(
            Labor.id != 1
        ).order_by(
            Labor.person_name,
            Labor.hourly_rate
        ).all()

    @classmethod
    def find_all_by_person_name_except_default(cls, person_name: str) -> Labors:
        return cls.query.filter(
            Labor.id != 1,
            Labor.person_name.icontains(person_name)
        ).order_by(
            Labor.person_name, 
            Labor.hourly_rate
        ).all()

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.query.with_entities(
            Labor.id, 
            Labor.person_name
        ).order_by(
            Labor.person_name, 
            Labor.hourly_rate
        ).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Labor':
        return cls.query.filter(Labor.id == id).first()
    
    @classmethod
    def find_first_by_id_except_default(cls, id: int) -> 'Labor':
        return cls.query.filter(
            Labor.id != 1,
            Labor.id == id
        ).first()

    def __init__(self, person_name: str, hourly_rate: float) -> None:
        self.person_name = person_name
        self.hourly_rate = hourly_rate


from .product import Product
