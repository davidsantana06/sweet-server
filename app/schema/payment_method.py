from flask_restx.fields import Integer, String


payment_method_schema = {
    'id': Integer(title='ID', readonly=True),
    'name': String(
        title='Name',
        required=True,
        min_length=1,
        max_length=50
    ),
    'sales_quantity': Integer(title='Sales quantity', readonly=True),
}
