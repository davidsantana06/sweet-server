from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form


class _Form(Form):
    id_category = IntegerField(
        validators=[DataRequired()]
    )
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ]
    )
    preparation_time = IntegerField(
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )
    description = StringField(
        validators=[
            Length(0, 1_000)
        ]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...


class _IngredientRelForm(Form):
    id_ingredient = IntegerField(
        validators=[DataRequired()]
    )
    weight = IntegerField(
        validators=[DataRequired()]
    )


class CreateIngredientRelForm(_IngredientRelForm):
    ...


class UpdateIngredientRelForm(_IngredientRelForm):
    ...


class _MaterialRelForm(Form):
    id_material = IntegerField(
        validators=[DataRequired()]
    )
    quantity = IntegerField(
        validators=[DataRequired()]
    )


class CreateMaterialRelForm(_MaterialRelForm):
    ...


class UpdateMaterialRelForm(_MaterialRelForm):
    ...
