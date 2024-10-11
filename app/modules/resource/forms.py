from wtforms import FloatField, IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form


class ResourceForm(Form):
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ]
    )
    brand = StringField(
        validators=[Length(0, 100)]
    )
    supplier = StringField(
        validators=[Length(0, 100)]
    )
    value = FloatField(
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )
    current_quantity = FloatField(
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )
    minimum_quantity = IntegerField(
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )
