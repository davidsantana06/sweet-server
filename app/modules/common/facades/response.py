from http import HTTPStatus
from typing import Dict, List, Tuple, Union

from app.database import (
    Model, Models,
    SelectChoices
)


_Response = Tuple[
    Union[
        List[Dict[str, object]],
        Dict[str, object]
    ],
    HTTPStatus
]


class ResponseFacade():
    def as_dict(
        self,
        dict: Dict,
        status: HTTPStatus = HTTPStatus.OK
    ) -> _Response:
        return dict, status

    def as_message(
        self,
        message: str,
        status: HTTPStatus = HTTPStatus.OK
    ) -> _Response:
        return {'message': message}, status

    def as_model(
        self,
        model: Model,
        status: HTTPStatus = HTTPStatus.OK
    ) -> _Response:
        return model.to_dict(), status

    def as_models(
        self,
        models: Models,
        status: HTTPStatus = HTTPStatus.OK
    ) -> _Response:
        return [model.to_dict() for model in models], status

    def as_select_choices(
        self,
        select_choices: SelectChoices,
        status: HTTPStatus = HTTPStatus.OK
    ) -> _Response:
        return [
            {'value': value, 'label': label}
            for value, label in select_choices
        ], status
