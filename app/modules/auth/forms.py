from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    password = PasswordField(
        validators=[
            DataRequired(),
            Length(1, 8)
        ]
    )
