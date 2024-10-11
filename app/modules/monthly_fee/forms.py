from wtforms import StringField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form


class MonthlyFeeForm(Form):
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
    description = StringField(
        validators=[Length(0, 1_000)]
    )
