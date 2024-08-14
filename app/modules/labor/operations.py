from werkzeug.exceptions import NotFound

from app.database import Labor, Labors
from app.typing import SelectChoices

from .forms import UpdateForm


def create(person_name: str, hourly_rate: float) -> Labor:
    labor = Labor(person_name, hourly_rate)
    Labor.save(labor)
    return labor


def get_all() -> Labors:
    return Labor.find_all_except_default()


def get_all_by_person_name(person_name: str) -> Labors:
    return Labor.find_all_by_person_name_except_default(person_name)


def get_all_select_choices() -> SelectChoices:
    return Labor.find_all_select_choices()


def get_one_by_id(id: int, except_default: bool = True) -> Labor:
    labor = Labor.find_first_by_id(id, except_default=except_default)
    if not labor:
        raise NotFound('The labor was not found.')
    return labor


def update(labor: Labor, form: UpdateForm) -> Labor:
    form.populate_obj(labor)
    Labor.save(labor)
    return labor


def delete(labor: Labor) -> None:
    Labor.delete(labor)
