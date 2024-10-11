from flask import Blueprint


collaborator = Blueprint('collaborator', __name__, url_prefix='/collaborator')


from .routes import *
