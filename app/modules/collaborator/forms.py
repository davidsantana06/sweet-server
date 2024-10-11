from wtforms import FloatField, StringField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form


class CollaboratorForm(Form):
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
    description = StringField(
        validators=[Length(0, 1_000)]
    )
