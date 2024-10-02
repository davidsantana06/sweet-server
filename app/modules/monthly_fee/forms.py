from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form


class _Form(Form):
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
    description = TextAreaField(
        validators=[Length(0, 1_000)]
    )
    
    def _cast_fields(self) -> None:
        self.value.data = float(self.value.data)


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
