from dotenv import load_dotenv
from flask import Flask

from app.database.model import *
from app.extension import api, cors, database
from app.resource import (
    category_ns,
    collaborator_ns,
    customer_ns,
    payment_method_ns,
    user_ns
)

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
