from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class _Form(FlaskForm):
    id_category = SelectField(
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
    description = TextAreaField(
        validators=[
            Length(0, 1_000)
        ]
    )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...


class _IngredientRelForm(FlaskForm):
    id_ingredient = SelectField(
        validators=[DataRequired()]
    )
    weight = IntegerField(
        validators=[DataRequired()]
    )


class CreateIngredientRelForm(_IngredientRelForm):
    ...


class UpdateIngredientRelForm(_IngredientRelForm):
    ...


class _MaterialRelForm(FlaskForm):
    id_material = SelectField(
        validators=[DataRequired()]
    )
    quantity = IntegerField(
        validators=[DataRequired()]
    )


class CreateMaterialRelForm(_MaterialRelForm):
    ...


class UpdateMaterialRelForm(_MaterialRelForm):
    ...
