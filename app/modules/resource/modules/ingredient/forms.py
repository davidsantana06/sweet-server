from wtforms import FloatField
from wtforms.validators import DataRequired, NumberRange

from app.modules.resource.forms import ResourceForm


class IngredientForm(ResourceForm):
    weight = FloatField(
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )
