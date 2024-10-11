from werkzeug.exceptions import NotFound
from app.database import (
    Material, Materials,
    RelatedIds, SelectChoices
)
from .forms import MaterialForm


def create(
    name: str, brand: str, supplier: str, value: float,
    current_quantity: int, minimun_quantity: int
) -> Material:
    material = Material(
        name, brand, supplier, value,
        current_quantity, minimun_quantity
    )
    Material.save(material)
    return material


def get_all() -> Materials:
    return Material.find_all()


def get_all_by_name(name: str) -> Materials:
    return Material.find_all_by_name(name)


def get_all_select_choices(related_ids: RelatedIds) -> SelectChoices:
    return Material.find_all_select_choices_not_related_to_recipe(
        related_ids
    )


def get_one_by_id(id: int) -> Material:
    material = Material.find_first_by_id(id)
    if not material:
        raise NotFound('The material was not found.')
    return material


def update(material: Material, form: MaterialForm) -> Material:
    form.populate_obj(material)
    Material.save(material)
    return material


def delete(material: Material) -> None:
    Material.delete(material)
