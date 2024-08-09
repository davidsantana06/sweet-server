from app.database import Category
from app.typing import SelectChoices


def create(name: str) -> None:
    category = Category(name)
    Category.save(category)


def get_all_select_choices() -> SelectChoices:
    return Category.find_all_select_choices()


def get_one_by_name(name: str) -> Category:
    return Category.find_first_by_name(name)
