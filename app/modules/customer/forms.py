from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class _Form(FlaskForm):
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ],
    )
    phone = StringField(
        validators=[Length(15, 15)]
    )
    instagram = StringField(
        validators=[Length(1, 30)]
    )
    notes = TextAreaField(
        validators=[Length(0, 1_000)]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
