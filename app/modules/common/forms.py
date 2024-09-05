from flask_wtf import FlaskForm
from typing import List
from werkzeug.datastructures import ImmutableDict
from werkzeug.exceptions import BadRequest


class Form(FlaskForm):
    def __init__(self, data: ImmutableDict[str, object]) -> None:
        super().__init__(data)
        self.validate()

    @property
    def data(self) -> List[object]:
        return [field.data for field in self]

    def validate(self) -> bool:
        if not super().validate():
            fields = [field for field, _ in self.errors.items()]
            description = (
                'The submitted data is not valid. '
                f'Please review and correct [{', '.join(fields)}] before resubmitting.'
            )
            raise BadRequest(description)
        return True
