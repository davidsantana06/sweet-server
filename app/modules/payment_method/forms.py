from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class _Form(FlaskForm):
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ],
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
