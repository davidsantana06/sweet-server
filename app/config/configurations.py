from dotenv import load_dotenv
from flask import Flask

from app.database.models import *
from app.extensions import bcrypt, cors, database, login_manager

from . import parameters
from . import paths


def _apply_parameteres(app: Flask) -> None:
    app.json.sort_keys = parameters.JSON_SORT_KEYS
    for key in dir(parameters):
        is_parameter = key.isupper()
        if is_parameter:
            app.config[key] = getattr(parameters, key)


def configure_enviroment(app: Flask) -> None:
    load_dotenv(paths.ENV_FILE)
    _apply_parameteres(app)


def _configure_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def _configure_bcrypt(app: Flask) -> None:
    bcrypt.init_app(app)


def _configure_cors(app: Flask) -> None:
    cors.init_app(app, origins=parameters.ALLOWED_HOSTS)


def _configure_login_manager(app: Flask) -> None:
    login_manager.init_app(app)
    login_manager.user_loader(
        lambda id: User.find_first_by_id(
            int(id),
            except_super=False
        )
    )


def configure_extensions(app: Flask) -> None:
    _configure_database(app)
    _configure_bcrypt(app)
    _configure_cors(app)
    _configure_login_manager(app)
