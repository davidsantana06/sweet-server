from flask_wtf import FlaskForm
from werkzeug.exceptions import BadRequest


def validate_form(form: FlaskForm) -> bool:
    if not form.validate():
        raise BadRequest(
            'The submitted data is not valid. ' + \
            'Please review and correct the input before resubmitting.'
        )
    return True
