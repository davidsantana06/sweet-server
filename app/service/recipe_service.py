from typing import List, Union

from app.database import (
    Recipe, Recipes,
    RecipeIngredient, RecipeIngredients,
    RecipeMaterial, RecipeMaterials,
)
from app.exception import (
    RecipeIngredientAlreadyExists,
    RecipeIngredientNotFound,
    RecipeMaterialAlreadyExists,
    RecipeMaterialNotFound,
    RecipeNotFound
)
from app.schema import (
    RecipeIngredientSchema,
    RecipeMaterialSchema,
    RecipeSchema
)
from app.service import category_service, ingredient_service, material_service


def create(data: RecipeSchema) -> Recipe:
    category_service.get_one_by('id', data['id_category'])
    recipe = Recipe(**data)
    Recipe.save(recipe)
    return recipe


def create_ingredient_rel(data: RecipeIngredientSchema) -> RecipeIngredient:
    get_one_by_id(data['id_recipe'])
    ingredient_service.get_one_by_id(data['id_ingredient'])
    already_exists = RecipeIngredient.find_first_by_ids(
        data['id_recipe'],
        data['id_ingredient']
    )
    if already_exists: raise RecipeIngredientAlreadyExists()
    recipe_ingredient = RecipeIngredient(**data)
    RecipeIngredient.save(recipe_ingredient)
    return recipe_ingredient


def create_material_rel(data: RecipeMaterialSchema) -> RecipeMaterial:
    get_one_by_id(data['id_recipe'])
    material_service.get_one_by_id(data['id_material'])
    already_exists = RecipeMaterial.find_first_by_ids(
        data['id_recipe'],
        data['id_material']
    )
    if already_exists: raise RecipeMaterialAlreadyExists()
    recipe_material = RecipeMaterial(**data)
    RecipeMaterial.save(recipe_material)
    return recipe_material


def get_all() -> Recipes:
    return Recipe.find_all()


def get_all_by_id_category(id_category: int) -> Recipes:
    return Recipe.find_all_by_id_category(id_category)


def get_all_by_name(name: str) -> Recipes:
    return Recipe.find_all_by_name(name)


def get_all_ingredient_rels_by_id(
    id: int,
    only_id_ingredient: bool = False
) -> Union[RecipeIngredients, List[int]]:
    return RecipeIngredient.find_all_by_id_recipe(id, only_id_ingredient)


def get_all_material_rels_by_id(
    id: int,
    only_id_material: bool = False
) -> Union[RecipeMaterials, List[int]]:
    return RecipeMaterial.find_all_by_id_recipe(id, only_id_material)


def get_one_by_id(id: int) -> Recipe:
    recipe = Recipe.find_first_by_id(id)
    if not recipe: raise RecipeNotFound()
    return recipe


def get_one_ingredient_rel_by_ids(
    id: int, 
    id_ingredient: int
) -> RecipeIngredient:
    recipe_ingredient = RecipeIngredient.find_first_by_ids(id, id_ingredient)
    if not recipe_ingredient: raise RecipeIngredientNotFound()
    return recipe_ingredient


def get_one_material_rel_by_ids(
    id: int,
    id_material: int
) -> RecipeMaterial:
    recipe_material = RecipeMaterial.find_first_by_ids(id, id_material)
    if not recipe_material: raise RecipeMaterialNotFound()
    return recipe_material


def update(id: int, data: RecipeSchema) -> Recipe:
    category_service.get_one_by('id', data['id_category'])
    recipe = get_one_by_id(id)
    recipe.update(**data)
    Recipe.save(recipe)
    return recipe


def update_ingredient_rel(data: RecipeIngredientSchema) -> RecipeIngredient:
    recipe_ingredient = get_one_ingredient_rel_by_ids(
        data['id_recipe'],
        data['id_ingredient']
    )
    recipe_ingredient.update(**data)
    RecipeIngredient.save(recipe_ingredient)
    return recipe_ingredient


def update_material_rel(data: RecipeMaterialSchema) -> RecipeMaterial:
    recipe_material = get_one_material_rel_by_ids(
        data['id_recipe'],
        data['id_material']
    )
    recipe_material.update(**data)
    RecipeMaterial.save(recipe_material)
    return recipe_material


def delete(id: int) -> None:
    recipe = get_one_by_id(id)
    Recipe.delete(recipe)


def delete_ingredient_rel(id: int, id_recipe: int) -> None:
    recipe_ingredient = get_one_ingredient_rel_by_ids(id, id_recipe)
    RecipeIngredient.delete(recipe_ingredient)


def delete_material_rel(id: int, id_material: int) -> None:
    recipe_material = get_one_material_rel_by_ids(id, id_material)
    RecipeMaterial.delete(recipe_material)
