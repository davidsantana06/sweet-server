from http import HTTPStatus
from werkzeug.exceptions import BadRequest


class InvalidPayload(BadRequest):
    description = 'Invalid payload'


invalid_payload = (HTTPStatus.BAD_REQUEST, InvalidPayload.description)
