from http import HTTPStatus
from typing import Tuple
from werkzeug.exceptions import HTTPException, InternalServerError


def get_details(e: Exception) -> Tuple[str, HTTPStatus]:
    is_http_exception = isinstance(e, HTTPException)
    code, description = (
        (e.code, e.description) if is_http_exception else
        (InternalServerError.code, InternalServerError.description)
    )
    return description, HTTPStatus(code)
