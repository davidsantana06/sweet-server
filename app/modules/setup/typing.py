from typing import List, TypedDict


class _DefaultLaborData(TypedDict):
    person_name: str
    hourly_rate: float


class SetupData(TypedDict):
    category_names: List[str]
    payment_method_names: List[str]
    default_labor_data: _DefaultLaborData
