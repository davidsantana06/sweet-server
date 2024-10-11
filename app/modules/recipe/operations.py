from werkzeug.exceptions import NotFound
from app.database import (
    Recipe, Recipes,
    RecipeIngredient, RecipeIngredients,
    RecipeMaterial, RecipeMaterials,
    RelatedIds, SelectChoices
)
from .forms import IngredientRelForm, MaterialRelForm, RecipeForm


def create(
    id_category: int,
    name: int,
    preparation_time: int,
    description: str
) -> Recipe:
    recipe = Recipe(
        id_category,
        name,
        preparation_time,
        description
    )
    Recipe.save(recipe)
    return recipe


def create_ingredient_rel(
    id: int, id_ingredient: int, weight: int
) -> RecipeIngredient:
    ingredient_rel = RecipeIngredient(id, id_ingredient, weight)
    RecipeIngredient.save(ingredient_rel)
    return ingredient_rel


def create_material_rel(
    id: int, id_material: int, quantity: int
) -> RecipeMaterial:
    material_rel = RecipeMaterial(id, id_material, quantity)
    RecipeMaterial.save(material_rel)
    return material_rel


def get_all() -> Recipes:
    return Recipe.find_all()


def get_all_by_name(name: str) -> Recipes:
    return Recipe.find_all_by_name(name)


def get_all_select_choices() -> SelectChoices:
    return Recipe.find_all_select_choices()


def get_all_ingredient_rels_by_id(id: int) -> RecipeIngredients:
    return RecipeIngredient.find_all_by_id_recipe(id)


def get_all_ingredient_rel_related_ids_by_id(id: int) -> RelatedIds:
    return RecipeIngredient.find_all_related_ids_by_id_recipe(id)


def get_all_material_rels_by_id(id: int) -> RecipeMaterials:
    return RecipeMaterial.find_all_by_id_recipe(id)


def get_all_material_rel_related_ids_by_id(id: int) -> RelatedIds:
    return RecipeMaterial.find_all_related_ids_by_id_recipe(id)


def get_one_by_id(id: int) -> Recipe:
    recipe = Recipe.find_first_by_id(id)
    if not recipe:
        raise NotFound('The recipe was not found.')
    return recipe


def get_one_ingredient_rel_by_id_and_id_ingredient(
    id: int, id_ingredient: int
) -> RecipeIngredient:
    ingredient_rel = RecipeIngredient.find_first_by_id_recipe_and_id_ingredient(
        id,
        id_ingredient
    )
    if not ingredient_rel:
        raise NotFound('The ingredient rel was not found.')
    return ingredient_rel


def get_one_material_rel_by_id_and_id_material(
    id: int,
    id_material: int
) -> RecipeMaterial:
    material_rel = RecipeMaterial.find_first_by_id_recipe_and_id_material(
        id,
        id_material
    )
    if not material_rel:
        raise NotFound('The material rel was not found.')
    return material_rel


def update(recipe: Recipe, form: RecipeForm) -> Recipe:
    form.populate_obj(recipe)
    Recipe.save(recipe)
    return recipe


def update_ingredient_rel(
    ingredient_rel: RecipeIngredient, form: IngredientRelForm
) -> RecipeIngredient:
    form.populate_obj(ingredient_rel)
    RecipeIngredient.save(ingredient_rel)
    return ingredient_rel


def update_material_rel(
    material_rel: RecipeMaterial, form: MaterialRelForm
) -> RecipeMaterial:
    form.populate_obj(material_rel)
    RecipeMaterial.save(material_rel)
    return material_rel


def delete(recipe: Recipe) -> None:
    Recipe.delete(recipe)


def delete_ingredient_rel(ingredient_rel: RecipeIngredient) -> None:
    RecipeIngredient.delete(ingredient_rel)


def delete_material_rel(material_rel: RecipeMaterial) -> None:
    RecipeMaterial.delete(material_rel)
