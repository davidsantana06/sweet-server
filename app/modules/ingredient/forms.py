from wtforms import FloatField
from wtforms.validators import DataRequired, NumberRange

from app.forms import ResourceForm


class _Form(ResourceForm):
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
