from flask import Blueprint


labor = Blueprint('labor', __name__, url_prefix='/labor')


from .routes import *
