from flask import Blueprint


monthly_fee = Blueprint('monthly_fee', __name__, url_prefix='/monthly-fee')


from .routes import *
