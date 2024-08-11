from typing import List
from werkzeug.exceptions import NotFound

from app.database import Ingredient, Ingredients
from app.typing import SelectChoices

from .forms import UpdateForm


def create(
    name: str, brand: str, supplier: str, 
    value: float, weight: int,
    current_quantity: int, minimun_quantity: int
) -> Ingredient:
    ingredient = Ingredient(
        name, brand, supplier, value, weight,
        current_quantity, minimun_quantity
    )
    Ingredient.save(ingredient)
    return ingredient


def get_all() -> Ingredients:
    return Ingredient.find_all()


def get_all_by_name(name: str) -> Ingredients:
    return Ingredient.find_all_by_name(name)


def get_all_select_choices(related_ids: List[int]) -> SelectChoices:
    return Ingredient.find_all_select_choices_not_related_to_recipe(
        related_ids
    )


def get_one_by_id(id: int) -> Ingredient:
    ingredient = Ingredient.find_first_by_id(id)
    if not ingredient:
        raise NotFound('The ingredient was not found.')
    return ingredient


def update(ingredient: Ingredient, form: UpdateForm) -> Ingredient:
    form.populate_obj(ingredient)
    Ingredient.save(ingredient)
    return ingredient


def delete(ingredient: Ingredient) -> None:
    Ingredient.delete(ingredient)
