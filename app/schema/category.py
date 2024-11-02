from flask_restx.fields import Integer, String


category_schema = {
    'id': Integer(title='ID', readonly=True),
    'name': String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100
    )
}
