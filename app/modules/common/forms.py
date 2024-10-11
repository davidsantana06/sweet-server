from flask_wtf import FlaskForm
from typing import List, Type
from werkzeug.datastructures import ImmutableDict
from werkzeug.exceptions import BadRequest
from wtforms import IntegerField, Field, FloatField, StringField


class Form(FlaskForm):
    def __init__(self, data: ImmutableDict[str, str]) -> None:
        super().__init__(data)
        self._cast_fields()
        if not super().validate():
            raise BadRequest(self._error_description)

    @property
    def data(self) -> List[object]:
        return [field.data for field in self]

    @property
    def _error_description(self) -> str:
        fields = ', '.join(self.errors.keys())
        return (
            'The submitted data is not valid. '
            f'Please review and correct [{fields}] before resubmitting.'
        )

    def _get_primitive_type(field: Field) -> Type:
        return {
            IntegerField: int,
            FloatField: float,
            StringField: str
        }[type(field)]

    def _cast_fields(self) -> None:
        for field in self:
            data = field.data
            primitive_type = self._get_primitive_type(field)
            is_primitive_instance = isinstance(data, primitive_type)
            is_cast_necessary = data is not None and not is_primitive_instance
            if is_cast_necessary:
                try:
                    field.data = primitive_type(data)
                except (TypeError, ValueError):
                    pass
