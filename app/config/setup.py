from dotenv import load_dotenv
from flask import Flask
from pathlib import Path
from typing import List
import json

from app.database.model import *
from app.extension import api, cors, database
from app.resource import (
    category_ns,
    collaborator_ns,
    customer_ns,
    ingredient_ns,
    material_ns,
    monthly_fee_ns,
    payment_method_ns,
    product_ns,
    recipe_ns,
    user_ns
)
from app.schema import (
    CategorySchema,
    CollaboratorSchema,
    PaymentMethodSchema,
    UserSchema
)
from app.service import (
    category_service,
    collaborator_service,
    payment_method_service,
    user_service
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
    api.add_namespace(ingredient_ns)
    api.add_namespace(material_ns)
    api.add_namespace(monthly_fee_ns)
    api.add_namespace(payment_method_ns)
    api.add_namespace(product_ns)
    api.add_namespace(recipe_ns)
    api.add_namespace(user_ns)


def _setup_cors(app: Flask) -> None:
    cors.init_app(app, origins=parameter.ALLOWED_HOSTS)


def setup_extensions(app: Flask) -> None:
    _setup_database(app)
    _setup_api(app)
    _setup_cors(app)


def _get_setup_data(file_path: Path) -> object:
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


def _create_default_categories(data: List[CategorySchema]) -> None:
    for category in data:
        try: category_service.get_one_by(category['name'])
        except: category_service.create(category)


def _create_default_collaborator(data: CollaboratorSchema) -> None:
    try: collaborator_service.get_one_by_id(1, except_default=False)
    except: collaborator_service.create(data)


def _create_default_payment_methods(data: List[PaymentMethodSchema]) -> None:
    for payment_method in data:
        try: payment_method_service.get_one_by(payment_method['name'])
        except: payment_method_service.create(payment_method)


def _create_user(data: UserSchema) -> None:
    try: user_service.get_one()
    except: user_service.create(data)


def setup_entities(app: Flask) -> None:
    with app.app_context():
        _create_default_categories(
            _get_setup_data(path.DEFAULT_CATEGORIES_DATA_FILE)
        )
        _create_default_collaborator(
            _get_setup_data(path.DEFAULT_COLLABORATOR_DATA_FILE)
        )
        _create_default_payment_methods(
            _get_setup_data(path.DEFAULT_PAYMENT_METHODS_DATA_FILE)
        )
        _create_user(
            _get_setup_data(path.USER_DATA_FILE)
        )
