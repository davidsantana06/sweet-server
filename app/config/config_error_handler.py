from flask import Flask
from werkzeug.exceptions import HTTPException, InternalServerError


_GENERIC_DESCRIPTION = \
    'The server encountered an unexpected condition that prevented it from fulfilling the request.'


def _error_handler(e: Exception):
    code, description = (
        (e.code, e.description or _GENERIC_DESCRIPTION) if isinstance(e, HTTPException)
        else (InternalServerError.code, InternalServerError.description)
    )
    return {'message': description}, code


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, _error_handler)
