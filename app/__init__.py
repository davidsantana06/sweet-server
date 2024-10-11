from flask import Flask

from .config import configure_enviroment, configure_extensions
from .modules.common import common
from .modules.user import user


app = Flask(__name__)
configure_enviroment(app)
configure_extensions(app)
app.register_blueprint(common)
app.register_blueprint(user)
