from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)
from typing import List

from app.extensions import database

from ..inheritable import Resource
from ..typing import RelatedIds, SelectChoices


Materials = List['Material']


class Material(database.Model, Resource):
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
    def __query_all(cls, columns=[], filters=[]) -> Materials:
        return cls._query_all(
            columns=columns,
            filters=filters,
            ordinances=[
                Material.name, 
                Material.brand, 
                Material.supplier, 
                Material.value,
                Material.current_quantity,
                Material.minimum_quantity,
                Material.id
            ]
        )

    @classmethod
    def find_all(cls) -> Materials:
        return cls.__query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Materials:
        return cls.__query_all(
            filters=[Material.name.icontains(name)]
        )

    @classmethod
    def find_all_select_choices_not_related_to_recipe(
        cls,
        related_ids: RelatedIds
    ) -> SelectChoices:
        return cls.__query_all(
            columns=[
                Material.id, 
                Material.name
            ],
            filters=[Material.id.not_in(related_ids)]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Material':
        return cls._query_first(filters=[Material.id == id])
    
    def __init__(
        self,
        name: str, brand: str, supplier: str, value: float,
        current_quantity: float, minimum_quantity: int
    ) -> None:
        Resource.__init__(
            self,
            name, brand, supplier, value,
            current_quantity, minimum_quantity
        )


from .recipe_material import RecipeMaterial
