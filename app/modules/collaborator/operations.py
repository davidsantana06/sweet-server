from werkzeug.exceptions import NotFound
from app.database import (
    Collaborator, Collaborators,
    SelectChoices
)
from .forms import CollaboratorForm


def create(
    name: str,
    hourly_rate: float,
    notes: str
) -> Collaborator:
    collaborator = Collaborator(
        name,
        hourly_rate,
        notes
    )
    Collaborator.save(collaborator)
    return collaborator


def get_all() -> Collaborators:
    return Collaborator.find_all_except_default()


def get_all_by_name(name: str) -> Collaborators:
    return Collaborator.find_all_by_name_except_default(
        name
    )


def get_all_select_choices() -> SelectChoices:
    return Collaborator.find_all_select_choices()


def get_one_by_id(id: int, except_default: bool = True) -> Collaborator:
    collaborator = Collaborator.find_first_by_id(
        id,
        except_default
    )
    if not collaborator:
        raise NotFound('The collaborator was not found.')
    return collaborator


def update(collaborator: Collaborator, form: CollaboratorForm) -> Collaborator:
    form.populate_obj(collaborator)
    Collaborator.save(collaborator)
    return collaborator


def delete(collaborator: Collaborator) -> None:
    Collaborator.delete(collaborator)
