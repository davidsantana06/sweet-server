from flask_restx.fields import Float, Integer, String


monthly_fee_schema = {
    'id': Integer(title='ID', readonly=True),
    'name': String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100
    ),
    'value': Float(
        title='Value',
        required=True,
        min=0,
        max=10_000
    ),
    'hourly_rate': Float(
        title='Hourly rate',
        readonly=True
    ),
    'description': String(
        title='Description',
        required=True,
        max_length=1_000
    )
}
