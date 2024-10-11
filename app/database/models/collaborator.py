from sqlalchemy import Column, ColumnElement, Float, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database

from ..inheritable import Model
from ..typing import SelectChoices


Collaborators = List['Collaborator']


class Collaborator(database.Model, Model):
    id: Mapped[int] = mapped_column(
        Integer(),
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(100), nullable=False)
    hourly_rate = Column(Float(), nullable=False)
    notes = Column(String(1000))

    products: Mapped[List['Product']] = relationship(
        back_populates='collaborator'
    )

    @classmethod
    def __compose_filters(
        cls,
        except_default: bool,
        filters=[],
    ) -> List[ColumnElement[bool]]:
        return (filters + [Collaborator.id != 1]) if except_default else filters

    @classmethod
    def __query_all(
        cls,
        except_default: bool,
        columns=[],
        filters=[],
    ) -> Collaborators:
        return cls._query_all(
            columns=columns,
            filters=cls.__compose_filters(except_default, filters),
            ordinances=[
                Collaborator.name,
                Collaborator.hourly_rate,
                Collaborator.id
            ]
        )

    @classmethod
    def find_all_except_default(cls) -> Collaborators:
        return cls.__query_all(except_default=True)

    @classmethod
    def find_all_by_name_except_default(
        cls,
        name: str
    ) -> Collaborators:
        return cls.__query_all(
            except_default=True,
            filters=[Collaborator.name == name]
        )

    @classmethod
    def find_all_select_choices(cls) -> SelectChoices:
        return cls.__query_all(
            except_default=False,
            columns=[
                Collaborator.id,
                Collaborator.name
            ]
        )

    @classmethod
    def find_first_by_id(
        cls, 
        id: int, 
        except_default: bool
    ) -> 'Collaborator':
        return cls._query_first(
            filters=cls.__compose_filters(
                except_default,
                [Collaborator.id == id]
            )
        )

    def __init__(self,
        name: str,
        hourly_rate: float,
        notes: str
    ) -> None:
        self.name = name
        self.hourly_rate = hourly_rate
        self.notes = notes


from .product import Product
