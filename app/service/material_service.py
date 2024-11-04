from app.database import Material, Materials
from app.exception import MaterialNotFound
from app.schema import MaterialSchema
from app.service import recipe_service


def create(data: MaterialSchema) -> Material:
    material = Material(**data)
    Material.save(material)
    return material


def get_all() -> Materials:
    return Material.find_all()


def get_all_by_name(name: str) -> Materials:
    return Material.find_all_by_name(name)


def get_all_unrelated_to_recipe(id_recipe: int) -> Materials:
    related_ids = recipe_service.get_all_material_rels_by_id(
        id_recipe,
        only_id_material=True
    )
    return Material.find_all_except(related_ids)


def get_one_by_id(id: int) -> Material:
    material = Material.find_first_by_id(id)
    if not material: raise MaterialNotFound()
    return material


def update(id: int, data: MaterialSchema) -> Material:
    material = get_one_by_id(id)
    material.update(**data)
    Material.save(material)
    return material


def delete(id: int) -> None:
    material = get_one_by_id(id)
    Material.delete(material)
