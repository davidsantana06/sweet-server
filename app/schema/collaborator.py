from flask_restx.fields import Float, Integer, String


collaborator_schema = {
    'id': Integer(title='ID', readonly=True),
    'name': String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100
    ),
    'hourly_rate': Float(
        title='Hourly rate',
        required=True,
        min=0,
        max=10_000
    ),
    'notes': String(
        title='Notes',
        required=True,
        max_length=1_000
    ),
}
