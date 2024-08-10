from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class _Form(FlaskForm):
    person_name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ]
    )
    hourly_rate = FloatField(
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )
    description = TextAreaField(
        validators=[Length(0, 1_000)]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
