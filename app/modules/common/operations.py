from flask_wtf import FlaskForm
from typing import List
from werkzeug.exceptions import BadRequest


def get_data(form: FlaskForm) -> List[object]:
    return [field.data for field in form]


def validate(form: FlaskForm) -> bool:
    if not form.validate():
        fields = ', '.join(
            field for field, errors
            in form.errors.items() if errors
        )
        description = \
            'The submitted data is not valid. ' + \
            f'Please review and correct [{fields}] before resubmitting.'
        raise BadRequest(description)
    return True
