from typing import List, TypedDict


class DefaultCollaborator(TypedDict):
    name: str
    hourly_rate: float
    notes: str


class User(TypedDict):
    name: str


class SetupData(TypedDict):
    default_categories: List[str]
    default_payment_methods: List[str]
    default_collaborator: DefaultCollaborator
    user: User
