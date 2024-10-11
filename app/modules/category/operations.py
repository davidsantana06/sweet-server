from typing import Literal, Union
from werkzeug.exceptions import NotFound

from app.database import (
    Category, Categories,
    SelectChoices
)

from .forms import CategoryForm


def create(name: str) -> None:
    category = Category(name)
    Category.save(category)


def get_all() -> Categories:
    return Category.find_all()


def get_all_by_name(name: str) -> Categories:
    return Category.find_all_by_name(name)


def get_all_select_choices() -> SelectChoices:
    return Category.find_all_select_choices()


def get_one_by(
    field: Literal['id', 'name'],
    value: Union[int, str]
) -> Category:
    function = {
        'id': Category.find_first_by_id,
        'name': Category.find_first_by_name
    }[field]
    category = function(value)
    if not category:
        raise NotFound('The category was not found.')
    return category


def update(category: Category, form: CategoryForm) -> Category:
    form.populate_obj(category)
    Category.save(category)
    return category


def delete(category: Category) -> None:
    Category.delete(category)
