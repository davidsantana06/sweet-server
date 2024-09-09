from typing import Literal, Union
from werkzeug.exceptions import NotFound

from app.database import (
    Category, Categories,
    SelectChoices
)

from .forms import UpdateForm


def create(name: str) -> None:
    category = Category(name)
    Category.save(category)


def get_all() -> Categories:
    return Category.find_all()


def get_all_by_name(name: str) -> Categories:
    return Category.find_all_by_name(name)


def get_all_select_choices() -> SelectChoices:
    return Category.find_all_select_choices()


def _get_one_or_except_by(
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


def get_one_by_id(id: int) -> Category:
    return _get_one_or_except_by('id', id)


def get_one_by_name(name: str) -> Category:
    return _get_one_or_except_by('name', name)


def update(category: Category, form: UpdateForm) -> Category:
    form.populate_obj(category)
    Category.save(category)
    return category


def delete(category: Category) -> None:
    Category.delete(category)
