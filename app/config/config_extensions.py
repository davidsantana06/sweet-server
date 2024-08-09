from flask import Flask

from app.extensions import cors, database, bcrypt, login_manager
from app.database import *


def _configure_cors(app: Flask) -> None:
    cors.init_app(app, origins='*')


def _configure_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def _configure_bcrypt(app: Flask) -> None:
    bcrypt.init_app(app)


def _configure_login_manager(app: Flask) -> None:
    login_manager.init_app(app)
    login_manager.user_loader(
        lambda user_id: User.find_first_by_id(int(user_id))
    )


def configure_extensions(app: Flask) -> None:
    _configure_database(app)
    _configure_cors(app)
    _configure_bcrypt(app)
    _configure_login_manager(app)
