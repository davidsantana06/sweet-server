from flask import Blueprint


setup = Blueprint('setup', __name__, url_prefix='/setup')


from .routes import *
