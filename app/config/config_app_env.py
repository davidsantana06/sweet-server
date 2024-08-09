from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask
from os import environ

from ..constants import DATABASE_FILE, ENV_FILE, STATIC_FOLDER


def configure_app_env(app: Flask) -> None:
    load_dotenv(ENV_FILE)
    app.config.from_mapping({
        'SECRET_KEY': environ.get('SECRET_KEY'),
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{DATABASE_FILE}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'PERMANENT_SESSION_LIFETIME': timedelta(days=7),
        'WTF_CSRF_ENABLED': False
    })
    app.json.sort_keys = False
    app.static_folder = STATIC_FOLDER
