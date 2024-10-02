from wtforms import FloatField, IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form as CommonForm


class Form(CommonForm):
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

    def _cast_fields(self) -> None:
        self.value.data = float(self.value.data)
        self.current_quantity.data = float(
            self.current_quantity.data
        )
        self.minimum_quantity.data = int(
            self.minimum_quantity.data
        )
