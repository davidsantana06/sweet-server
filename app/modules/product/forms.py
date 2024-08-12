from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange


class _Form(FlaskForm):
    id_recipe = SelectField(
        validators=[DataRequired()]
    )
    id_labor = SelectField(
        validators=[DataRequired()]
    )
    loss_margin = FloatField(
        default=0.0,
        validators=[
            DataRequired(),
            NumberRange(0, 100)
        ]
    )
    contribuition_margin = FloatField(
        default=0.0,
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
