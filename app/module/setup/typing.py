from typing import List, TypedDict


class DefaultCollaboratorData(TypedDict):
    name: str
    hourly_rate: float
    notes: str


class SetupData(TypedDict):
    category_names: List[str]
    payment_method_names: List[str]
    default_collaborator_data: DefaultCollaboratorData
