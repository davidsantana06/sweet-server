from sqlalchemy import Column, ColumnElement, Float, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database

from ..inheritable import Model
from ..typing import SelectChoices


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
    def __compose_filters(
        cls,
        filters=[],
        except_default: bool = True
    ) -> List[ColumnElement[bool]]:
        return (filters + [Labor.id != 1]) if except_default else filters

    @classmethod
    def __query_all(
        cls, 
        columns=[], 
        filters=[],
        except_default: bool = True
    ) -> Labors:
        return cls._query_all(
            columns=columns,
            filters=cls.__compose_filters(filters, except_default),
            ordinances=[
                Labor.person_name,
                Labor.hourly_rate,
                Labor.id
            ]
        )

    @classmethod
    def find_all_except_default(cls) -> Labors:
        return cls.__query_all()

    @classmethod
    def find_all_by_person_name_except_default(cls, person_name: str) -> Labors:
        return cls._query_all(filters=[Labor.person_name == person_name])

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.__query_all(
            columns=[
                Labor.id, 
                Labor.person_name
            ]
        )

    @classmethod
    def find_first_by_id(cls, id: int, except_default: bool = True) -> 'Labor':
        return cls._query_first(
            filters=cls.__compose_filters([Labor.id == id], except_default)
        )

    def __init__(self, person_name: str, hourly_rate: float) -> None:
        self.person_name = person_name
        self.hourly_rate = hourly_rate


from .product import Product
