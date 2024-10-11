from wtforms import StringField
from wtforms.validators import DataRequired, Length

from app.modules.common.forms import Form


class CustomerForm(Form):
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ],
    )
    phone = StringField(
        validators=[Length(0, 15)]
    )
    instagram = StringField(
        validators=[Length(0, 31)]
    )
    notes = StringField(
        validators=[Length(0, 1_000)]
    )
