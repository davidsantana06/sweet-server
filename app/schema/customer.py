from flask_restx.fields import Integer, String


_PHONE_REGEX = r'^\(\d{2}\) 9\d{4}-\d{4}$'
''' (00) 00000-0000 '''

_INSTAGRAM_REGEX = r'^@[a-zA-Z0-9._]{0,29}$'
''' @username '''


customer_schema = {
    'id': Integer(title='ID', readonly=True),
    'name': String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100
    ),
    'phone': String(
        title='Phone',
        required=True,
        min_length=15,
        max_length=15,
        pattern=_PHONE_REGEX
    ),
    'instagram': String(
        title='Instagram',
        required=True,
        min_length=2,
        max_length=30,
        pattern=_INSTAGRAM_REGEX,
        example='@username'
    ),
    'notes': String(
        title='Notes',
        required=True,
        max_length=1_000
    )
}
