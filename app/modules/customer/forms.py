from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

from app.modules.common.forms import Form


class _Form(Form):
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ],
    )
    phone = StringField(
        validators=[Length(0, 15)]
    )
    instagram = StringField(
        validators=[Length(0, 31)]
    )
    notes = TextAreaField(
        validators=[Length(0, 1_000)]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
