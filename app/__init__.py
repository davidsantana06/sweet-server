from flask import Flask

from .config import configure_enviroment, configure_error_handler, configure_extensions
from .modules.auth import auth
from .modules.category import category
from .modules.common import common
from .modules.customer import customer
from .modules.labor import labor
from .modules.monthly_fee import monthly_fee
from .modules.payment_method import payment_method
from .modules.product import product
from .modules.recipe import recipe
from .modules.resource import resource
from .modules.setup import setup
from .modules.user import user


app = Flask(__name__)

configure_enviroment(app)
configure_extensions(app)
configure_error_handler(app)

for blueprint in (
    auth, category, common, customer, labor, monthly_fee,
    payment_method, product, recipe, resource, setup, user,
):
    app.register_blueprint(blueprint)
