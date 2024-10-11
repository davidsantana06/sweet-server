from flask import Flask

from .config import configure_enviroment, configure_extensions
from .modules.auth import auth
from .modules.category import category
from .modules.collaborator import collaborator
from .modules.common import common
from .modules.user import user


app = Flask(__name__)
configure_enviroment(app)
configure_extensions(app)
app.register_blueprint(auth)
app.register_blueprint(category)
app.register_blueprint(collaborator)
app.register_blueprint(common)
app.register_blueprint(user)
