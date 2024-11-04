from .supply import (
    SupplyInfoSchema, supply_info_schema,
    SupplyStockSchema, supply_stock_schema
)


class MaterialSchema(SupplyInfoSchema, SupplyStockSchema):
    ...


material_schema = MaterialSchema(
    **supply_info_schema,
    **supply_stock_schema
)
