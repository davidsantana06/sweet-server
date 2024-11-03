from typing import Dict

from app.database import Ingredient, Ingredients
from app.exception import IngredientNotFound


def create(data: Dict[str, object]) -> Ingredient:
    ingredient = Ingredient(**data)
    Ingredient.save(ingredient)
    return ingredient


def get_all() -> Ingredients:
    return Ingredient.find_all()


def get_all_by_name(name: str) -> Ingredients:
    return Ingredient.find_all_by_name(name)


def get_all_unrelated_to_recipe(id_recipe: int) -> Ingredients:
    related_ids = []
    return Ingredient.find_all_except(related_ids)


def get_one_by_id(id: int) -> Ingredient:
    ingredient = Ingredient.find_first_by_id(id)
    if not ingredient: raise IngredientNotFound()
    return ingredient


def update(id: int, data: Dict[str, object]) -> Ingredient:
    ingredient = get_one_by_id(id)
    ingredient.update(**data)
    Ingredient.save(ingredient)
    return ingredient


def delete(id: int) -> None:
    Ingredient = get_one_by_id(id)
    Ingredient.delete(Ingredient)
