from flask_restx.fields import Integer
from app.extension import api
from .supply import (
    SupplyInfoSchema, supply_info_schema,
    SupplyStockSchema, supply_stock_schema
)


class IngredientSchema(SupplyInfoSchema, SupplyStockSchema):
    weight: int


ingredient_schema = api.model('Ingredient', IngredientSchema(
    **supply_info_schema,
    weight=Integer(
        title='Weight in grams',
        required=True,
        min=1,
        max=10_000
    ),
    **supply_stock_schema
))
