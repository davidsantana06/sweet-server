from flask import Flask
from http import HTTPStatus
from werkzeug.exceptions import HTTPException, InternalServerError

from app.modules.common.facades import response


def _error_handler(exception: Exception):
    is_http_exception = isinstance(exception, HTTPException)
    code, description = (
        (exception.code, exception.description) if is_http_exception
        else (InternalServerError.code, InternalServerError.description)
    )
    status = HTTPStatus(code)
    return response.as_message(description, status)


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, _error_handler)
