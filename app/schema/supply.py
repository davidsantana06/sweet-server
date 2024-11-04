from flask_restx.fields import Float, Integer, String
from typing import NotRequired, TypedDict


class SupplyInfoSchema(TypedDict):
    id: NotRequired[int]
    name: str
    brand: str
    supplier: str
    value: float


class SupplyStockSchema(TypedDict):
    current_quantity: float
    minimum_quantity: int


supply_info_schema = SupplyInfoSchema(
    id=Integer(
        title='ID',
        readonly=True
    ),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100,
    ),
    brand=String(
        title='Brand',
        required=True,
        max_length=100,
    ),
    supplier=String(
        title='Supplier',
        required=True,
        max_length=100,
    ),
    value=Float(
        title='Value',
        required=True,
        min=0,
        max=10_000
    )
)

supply_stock_schema = SupplyStockSchema(
    current_quantity=Float(
        title='Current quantity',
        required=True,
        min=0,
        max=10_000
    ),
    minimum_quantity=Integer(
        title='Minimum quantity',
        required=True,
        min=0,
        max=10_000
    )
)
