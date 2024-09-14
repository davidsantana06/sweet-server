from dotenv import load_dotenv
from flask import Flask

from . import parameters
from . import paths


def _configure_parameteres(app: Flask) -> None:
    app.json.sort_keys = parameters.JSON_SORT_KEYS
    for key in dir(parameters):
        is_parameter = key.isupper()
        if is_parameter:
            app.config[key] = getattr(parameters, key)


def configure_enviroment(app: Flask) -> None:
    load_dotenv(paths.ENV_FILE)
    _configure_parameteres(app)
