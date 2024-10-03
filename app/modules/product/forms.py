from wtforms import FloatField, IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form


class _Form(Form):
    id_recipe = IntegerField(
        validators=[DataRequired()]
    )
    id_labor = IntegerField(
        validators=[DataRequired()]
    )
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ]
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
