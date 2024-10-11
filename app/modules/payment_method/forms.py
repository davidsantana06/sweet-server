from wtforms import StringField
from wtforms.validators import DataRequired, Length

from app.modules.common.forms import Form


class PaymentMethodForm(Form):
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ],
    )
