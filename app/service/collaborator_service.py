from app.database import Collaborator, Collaborators
from app.exception import CollaboratorNotFound
from app.schema import CollaboratorSchema


def create(data: CollaboratorSchema) -> Collaborator:
    collaborator = Collaborator(**data)
    Collaborator.save(collaborator)
    return collaborator


def get_all() -> Collaborators:
    return Collaborator.find_all()


def get_all_by_name(name: str) -> Collaborators:
    return Collaborator.find_all_by_name(name)


def get_one_by_id(id: int, except_default: bool = True) -> Collaborator:
    collaborator = Collaborator.find_first_by_id(id, except_default)
    if not collaborator: raise CollaboratorNotFound()
    return collaborator


def update(id: int, data: CollaboratorSchema) -> Collaborator:
    collaborator = get_one_by_id(id)
    collaborator.update(**data)
    Collaborator.save(collaborator)
    return collaborator


def delete(id: int) -> None:
    collaborator = get_one_by_id(id)
    Collaborator.delete(collaborator)
