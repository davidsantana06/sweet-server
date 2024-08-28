from http import HTTPStatus
from typing import Dict, Tuple

from app.database.inheritable import Model, Models
from app.typing import SelectChoices


_Response = Tuple[
    Dict[str, object],
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
            {'id': id, 'name': name} for id, name in select_choices
        ], status
