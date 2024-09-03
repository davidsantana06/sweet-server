from flask import Flask
from http import HTTPStatus
from werkzeug.exceptions import HTTPException, InternalServerError

from app.modules.common.facades import response


def _error_handler(e: Exception):
    code, description = (
        (e.code, e.description) if isinstance(e, HTTPException)
        else (InternalServerError.code, InternalServerError.description)
    )
    status = HTTPStatus(code)
    return response.as_message(description, status)


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, _error_handler)
