from flask import Response, jsonify, make_response
from http import HTTPStatus
from typing import Dict

from app.database import (
    Model, Models,
    SelectChoices
)


class ResponseFacade():
    def as_dict(
        self,
        data: Dict,
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return self.__jsonify(data, status)

    def as_message(
        self,
        message: str,
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return self.__jsonify(
            {'message': message},
            status
        )

    def as_model(
        self,
        model: Model,
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return self.__jsonify(model.to_dict(), status)

    def as_models(
        self,
        models: Models,
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return self.__jsonify(
            [model.to_dict() for model in models],
            status
        )

    def as_select_choices(
        self,
        select_choices: SelectChoices,
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return self.__jsonify(
            [
                {'value': value, 'label': label}
                for value, label in select_choices
            ], status
        )

    def __jsonify(
        self,
        data: object,
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return make_response(
            jsonify(data),
            status
        )
