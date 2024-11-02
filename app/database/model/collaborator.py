from sqlalchemy import Column, ColumnElement, Float, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


Collaborators = List['Collaborator']


class Collaborator(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(100), nullable=False)
    hourly_rate = Column(Float, nullable=False)
    notes = Column(String(1000))

    products: Mapped[List['Product']] = relationship(
        back_populates='collaborator'
    )

    @classmethod
    def __compose_filters(
        cls,
        except_default: bool,
        filters: List = None,
    ) -> List[ColumnElement[bool]]:
        return (filters + [cls.id != 1]) if except_default else filters

    @classmethod
    def _query_all(
        cls,
        except_default: bool,
        columns: List = None,
        filters: List = None,
    ) -> Collaborators:
        return super()._query_all(
            columns=columns,
            filters=cls.__compose_filters(except_default, filters),
            ordinances=[cls.name, cls.hourly_rate, cls.id]
        )

    @classmethod
    def find_all(cls) -> Collaborators:
        return cls._query_all(except_default=False)

    @classmethod
    def find_all_by_name(cls, name: str) -> Collaborators:
        return cls._query_all(
            except_default=False, 
            filters=[cls.name.icontains(name)]
        )

    @classmethod
    def find_first_by_id(cls, id: int, except_default: bool) -> 'Collaborator':
        return cls._query_first(
            filters=cls.__compose_filters(except_default, [cls.id == id])
        )


from .product import Product
