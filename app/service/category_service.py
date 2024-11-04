from typing import Literal, Union

from app.database import Category, Categories
from app.exception import CategoryNotFound
from app.schema import CategorySchema


def create(data: CategorySchema) -> Category:
    category = Category(**data)
    Category.save(category)
    return category


def get_all() -> Categories:
    return Category.find_all()


def get_one_by(
    field: Literal['id', 'name'],
    value: Union[int, str]
) -> Category:
    function = getattr(Category, f'find_first_by_{field}')
    category = function(value)
    if not category: raise CategoryNotFound()
    return category


def update(id: int, data: CategorySchema) -> Category:
    category = get_one_by('id', id)
    category.update(**data)
    Category.save(category)
    return category


def delete(id: int) -> None:
    category = get_one_by('id', id)
    Category.delete(category)
