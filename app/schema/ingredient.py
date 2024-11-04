from flask_restx.fields import Integer
from .supply import (
    SupplyInfoSchema, supply_info_schema,
    SupplyStockSchema, supply_stock_schema
)


class IngredientSchema(SupplyInfoSchema, SupplyStockSchema):
    weight: int


ingredient_schema = IngredientSchema(
    **supply_info_schema,
    weight=Integer(title='Weight', required=True),
    **supply_stock_schema
)
