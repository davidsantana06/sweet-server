from flask import Flask

from app.modules.auth import auth
from app.modules.category import category
from app.modules.common import common
from app.modules.customer import customer
from app.modules.labor import labor
from app.modules.monthly_fee import monthly_fee
from app.modules.payment_method import payment_method
from app.modules.product import product
from app.modules.recipe import recipe
from app.modules.resource import resource
from app.modules.setup import setup
from app.modules.user import user


def configure_modules(app: Flask) -> None:
    for blueprint in (
        auth, category, common, customer, labor, monthly_fee,
        payment_method, product, recipe, resource, setup, user
    ):
        app.register_blueprint(blueprint)
