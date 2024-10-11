from typing import List, TypedDict


CategoryNames = List[str]
PaymentMethodNames = List[str]


class DefaultCollaboratorData(TypedDict):
    name: str
    hourly_rate: float
    notes: str


class SetupData(TypedDict):
    category_names: CategoryNames
    payment_method_names: PaymentMethodNames
    default_collaborator_data: DefaultCollaboratorData
