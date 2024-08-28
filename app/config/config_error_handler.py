from flask import Flask
from http import HTTPStatus
from werkzeug.exceptions import HTTPException, InternalServerError

from app.facades import response


_GENERIC_DESCRIPTION = \
    'The server encountered an unexpected condition that prevented it from fulfilling the request.'


def _error_handler(e: Exception):
    code, description = (
        (e.code, e.description or _GENERIC_DESCRIPTION) if isinstance(e, HTTPException)
        else (InternalServerError.code, InternalServerError.description)
    )
    status = HTTPStatus(code)
    return response.as_message(description, status)


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, _error_handler)
