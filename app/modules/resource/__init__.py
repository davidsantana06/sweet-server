from flask import Blueprint

from .modules.ingredient import ingredient
from .modules.material import material


resource = Blueprint('resource', __name__)
resource.register_blueprint(ingredient)
resource.register_blueprint(material)
