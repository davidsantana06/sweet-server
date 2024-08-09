from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class _Form(FlaskForm):
    name = StringField(
        validators=[
            DataRequired(), 
            Length(1, 100)
        ]
    )
    value = StringField(
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
