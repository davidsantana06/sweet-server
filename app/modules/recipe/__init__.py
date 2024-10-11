from flask import Blueprint


recipe = Blueprint('recipe', __name__, url_prefix='/recipe')


from .routes import *
