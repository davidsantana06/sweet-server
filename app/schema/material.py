from .supply import supply_info_schema, supply_stock_schema


material_schema = supply_info_schema | supply_stock_schema
