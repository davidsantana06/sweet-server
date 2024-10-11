from flask import Blueprint


payment_method = Blueprint('payment_method', __name__, url_prefix='/payment-method')


from .routes import *
