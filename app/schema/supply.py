from flask_restx.fields import Float, Integer, String


supply_info_schema = {
    'id': Integer(
        title='ID',
        readonly=True
    ),
    'name': String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100,
    ),
    'brand': String(
        title='Brand',
        required=True,
        max_length=100,
    ),
    'supplier': String(
        title='Supplier',
        required=True,
        max_length=100,
    ),
    'value': Float(
        title='Value',
        required=True,
        min=0,
        max=10_000
    )
}

supply_stock_schema = {
    'current_quantity': Float(
        title='Current quantity',
        required=True,
        min=0,
        max=10_000
    ),
    'minimum_quantity': Integer(
        title='Minimum quantity',
        required=True,
        min=0,
        max=10_000
    )
}
