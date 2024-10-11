from wtforms import FloatField, IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form


class ProductForm(Form):
    id_recipe = IntegerField(
        validators=[DataRequired()]
    )
    id_collaborator = IntegerField(
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
