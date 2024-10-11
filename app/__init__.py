from flask import Flask

from .config import configure_enviroment, configure_extensions
from .modules.auth import auth
from .modules.category import category
from .modules.collaborator import collaborator
from .modules.common import common
from .modules.customer import customer
from .modules.monthly_fee import monthly_fee
from .modules.payment_method import payment_method
from .modules.user import user


app = Flask(__name__)
configure_enviroment(app)
configure_extensions(app)
app.register_blueprint(auth)
app.register_blueprint(category)
app.register_blueprint(collaborator)
app.register_blueprint(common)
app.register_blueprint(customer)
app.register_blueprint(monthly_fee)
app.register_blueprint(payment_method)
app.register_blueprint(user)
