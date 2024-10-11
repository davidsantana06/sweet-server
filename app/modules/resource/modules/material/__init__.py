from flask import Blueprint


material = Blueprint('material', __name__, url_prefix='/material')


from .routes import *
