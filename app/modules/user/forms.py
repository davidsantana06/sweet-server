from wtforms import StringField
from wtforms.validators import DataRequired, Length

from app.modules.common.forms import Form


class _Form(Form):
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 30)
        ]
    )
    nickname = StringField(
        validators=[
            DataRequired(),
            Length(1, 15)
        ]
    )
    password = StringField(
        validators=[
            DataRequired(),
            Length(4, 20)
        ]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
