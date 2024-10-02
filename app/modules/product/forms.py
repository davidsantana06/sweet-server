from wtforms import FloatField, SelectField, StringField
from wtforms.validators import DataRequired, Length, NumberRange

from app.modules.common.forms import Form


class _Form(Form):
    id_recipe = SelectField(
        validators=[DataRequired()]
    )
    id_labor = SelectField(
        validators=[DataRequired()]
    )
    name = StringField(
        validators=[
            DataRequired(),
            Length(1, 100)
        ]
    )
    loss_margin = FloatField(
        default=0.0,
        validators=[
            DataRequired(),
            NumberRange(0, 100)
        ]
    )
    contribuition_margin = FloatField(
        default=0.0,
        validators=[
            DataRequired(),
            NumberRange(0, 10_000)
        ]
    )

    def _cast_fields(self) -> None:
        self.loss_margin.data = float(
            self.loss_margin.data
        )
        self.contribuition_margin.data = float(
            self.contribuition_margin.data
        )


class CreateForm(_Form):
    ...


class UpdateForm(_Form):
    ...
