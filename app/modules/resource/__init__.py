from flask import Blueprint

from .modules.ingredient import ingredient


resource = Blueprint('resource', __name__)
resource.register_blueprint(ingredient)
