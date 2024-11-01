from dotenv import load_dotenv
from flask import Flask

from app.database.model import *
from app.extension import api, cors, database

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


def _setup_cors(app: Flask) -> None:
    cors.init_app(app, origins=parameter.ALLOWED_HOSTS)


def setup_extensions(app: Flask) -> None:
    _setup_database(app)
    _setup_api(app)
    _setup_cors(app)
