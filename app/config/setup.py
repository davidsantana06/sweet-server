from dotenv import load_dotenv
from flask import Flask
from typing import List
import json

from app.database.model import *
from app.extension import api, cors, database
from app.resource import (
    category_ns,
    collaborator_ns,
    customer_ns,
    payment_method_ns,
    user_ns
)
from app.service import (
    category_service,
    collaborator_service,
    payment_method_service,
    user_service
)
from app.typing import DefaultCollaborator, SetupData, User

from . import parameter
from . import path


def _apply_parameteres(app: Flask) -> None:
    app.json.sort_keys = parameter.JSON_SORT_KEYS
    for key in dir(parameter):
        is_parameter = key.isupper()
        if is_parameter:
            app.config[key] = getattr(parameter, key)


def setup_enviroment(app: Flask) -> None:
    load_dotenv(path.ENV_FILE)
    _apply_parameteres(app)


def _setup_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def _setup_api(app: Flask) -> None:
    api.init_app(app)
    api.add_namespace(category_ns)
    api.add_namespace(collaborator_ns)
    api.add_namespace(customer_ns)
    api.add_namespace(payment_method_ns)
    api.add_namespace(user_ns)


def _setup_cors(app: Flask) -> None:
    cors.init_app(app, origins=parameter.ALLOWED_HOSTS)


def setup_extensions(app: Flask) -> None:
    _setup_database(app)
    _setup_api(app)
    _setup_cors(app)


def _get_setup_data() -> SetupData:
    with open(path.SETUP_FILE, encoding='utf-8') as file:
        return json.load(file)


def _create_default_categories(names: List[str]) -> None:
    for name in names:
        try: category_service.get_one_by('name', name)
        except: category_service.create({'name': name})


def _create_default_collaborator(data: DefaultCollaborator) -> None:
    try: collaborator_service.get_one_by_id(1, except_default=False)
    except: collaborator_service.create(data)


def _create_default_payment_methods(names: List[str]) -> None:
    for name in names:
        try: payment_method_service.get_one_by('name', name)
        except: payment_method_service.create({'name': name})


def _create_user(data: User) -> None:
    try: user_service.get_one()
    except: user_service.create(data)


def setup_entities(app: Flask) -> None:
    data = _get_setup_data()
    with app.app_context():
        _create_default_categories(data['default_categories'])
        _create_default_collaborator(data['default_collaborator'])
        _create_default_payment_methods(data['default_payment_methods'])
        _create_user(data['user'])
