from app.database import Ingredient, Ingredients
from app.exception import IngredientNotFound
from app.schema import IngredientSchema
from app.service import recipe_service


def create(data: IngredientSchema) -> Ingredient:
    ingredient = Ingredient(**data)
    Ingredient.save(ingredient)
    return ingredient


def get_all() -> Ingredients:
    return Ingredient.find_all()


def get_all_by_name(name: str) -> Ingredients:
    return Ingredient.find_all_by_name(name)


def get_all_unrelated_to_recipe(id_recipe: int) -> Ingredients:
    related_ids = recipe_service.get_all_ingredient_rels_by_id(
        id_recipe,
        only_id_ingredient=True
    )
    return Ingredient.find_all_except(related_ids)


def get_one_by_id(id: int) -> Ingredient:
    ingredient = Ingredient.find_first_by_id(id)
    if not ingredient: raise IngredientNotFound()
    return ingredient


def update(id: int, data: IngredientSchema) -> Ingredient:
    ingredient = get_one_by_id(id)
    ingredient.update(**data)
    Ingredient.save(ingredient)
    return ingredient


def delete(id: int) -> None:
    ingredient = get_one_by_id(id)
    Ingredient.delete(ingredient)
