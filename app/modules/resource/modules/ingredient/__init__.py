from flask import Blueprint


ingredient = Blueprint('ingredient', __name__, url_prefix='/ingredient')


from .routes import *
