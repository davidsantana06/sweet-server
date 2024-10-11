from wtforms import StringField
from wtforms.validators import DataRequired, Length

from app.modules.common.forms import Form


class AuthForm(Form):
    nickname = StringField(
        validators=[
            DataRequired(),
            Length(1, 15)
        ]
    )
    password = StringField(
        validators=[
            DataRequired(),
            Length(4, 20)
        ]
    )
