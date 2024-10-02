from flask_wtf import FlaskForm
from typing import List
from werkzeug.datastructures import ImmutableDict
from werkzeug.exceptions import BadRequest


class Form(FlaskForm):
    def __init__(self, data: ImmutableDict[str, str]) -> None:
        super().__init__(data)
        self._cast_fields()
        if not super().validate():
            raise BadRequest(self.__error_description)

    @property
    def data(self) -> List[object]:
        return [field.data for field in self]

    @property
    def __error_description(self) -> str:
        fields = ', '.join(self.errors.keys())
        return (
            'The submitted data is not valid. '
            f'Please review and correct [{fields}] before resubmitting.'
        )

    def _cast_fields(self) -> None:
        ...
