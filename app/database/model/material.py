from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extension import database

from ..inheritable import Model, ResourceMixin, TimestampMixin


Materials = List['Material']


class Material(database.Model, Model, ResourceMixin, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )

    recipe_rels: Mapped[List['RecipeMaterial']] = relationship(
        back_populates='material',
        cascade='all, delete'
    )

    @classmethod
    def _query_all(cls, columns: List = None, filters: List = None) -> Materials:
        return super()._query_all(
            columns=columns,
            filters=filters,
            ordinances=[
                cls.name, 
                cls.brand, 
                cls.supplier, 
                cls.value,
                cls.current_quantity,
                cls.minimum_quantity,
                cls.id
            ]
        )

    @classmethod
    def find_all(cls) -> Materials:
        return cls._query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Materials:
        return cls._query_all(filters=[cls.name.icontains(name)])

    @classmethod
    def find_all_except(cls, ids: List[int]) -> Materials:
        return cls._query_all(filters=[cls.id.not_in(ids)])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Material':
        return cls._query_first(filters=[cls.id == id])


from .recipe_material import RecipeMaterial
