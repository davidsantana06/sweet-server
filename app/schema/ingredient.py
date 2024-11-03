from flask_restx.fields import Integer
from .supply import supply_info_schema, supply_stock_schema


ingredient_schema = {
    **supply_info_schema,
    'weight': Integer(title='Weight', required=True),
    **supply_stock_schema
}
