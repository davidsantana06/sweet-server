from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length


class _Form(FlaskForm):
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
    password = PasswordField(
        validators=[
            DataRequired(),
            Length(4, 20)
        ]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
