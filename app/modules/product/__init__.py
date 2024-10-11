from flask import Blueprint


product = Blueprint('product', __name__, url_prefix='/product')


from .routes import *
