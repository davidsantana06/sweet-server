from werkzeug.exceptions import NotFound
from app.database import Category, SelectChoices


def create(name: str) -> None:
    category = Category(name)
    Category.save(category)


def get_all_select_choices() -> SelectChoices:
    return Category.find_all_select_choices()


def _check_existance(category: Category) -> bool:
    if not category:
        raise NotFound('The category was not found.')
    return True


def get_one_by_id(id: int) -> Category:
    category = Category.find_first_by_id(id)
    _check_existance(category)
    return category


def get_one_by_name(name: str) -> Category:
    category = Category.find_first_by_name(name)
    _check_existance(category)
    return category
