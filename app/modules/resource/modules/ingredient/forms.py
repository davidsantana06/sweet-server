from wtforms import FloatField
from wtforms.validators import DataRequired, NumberRange

from app.modules.resource.forms import Form


class _Form(Form):
    weight = FloatField(
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
