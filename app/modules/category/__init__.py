from flask import Blueprint


category = Blueprint('category', __name__, url_prefix='/category')


from .routes import *
