from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length

from app.modules.common.forms import Form


class LoginForm(Form):
    nickname = StringField(
        validators=[
            DataRequired(),
            Length(1, 15)
        ]
    )
    password = PasswordField(
        validators=[
            DataRequired(),
            Length(4, 20)
        ]
    )
