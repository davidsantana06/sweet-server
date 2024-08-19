from typing import List, TypedDict


CategoryNames = List[str]
PaymentMethodNames = List[str]


class DefaultLaborData(TypedDict):
    person_name: str
    hourly_rate: float


class SetupData(TypedDict):
    category_names: CategoryNames
    payment_method_names: PaymentMethodNames
    default_labor_data: DefaultLaborData
