from flask import Blueprint

from .modules.ingredient import ingredient
from .modules.material import material


resource = Blueprint('resource', __name__)
for blueprint in (ingredient, material):
    resource.register_blueprint(blueprint)
