from http import HTTPStatus
from werkzeug.exceptions import Conflict


class RecipeIngredientAlreadyExists(Conflict):
    description = 'Recipe-ingredient relation already exists'


class RecipeMaterialAlreadyExists(Conflict):
    description = 'Recipe-material relation already exists'


class SaleProductAlreadyExists(Conflict):
    description = 'Sale-product relation already exists'


_response = lambda description: (HTTPStatus.CONFLICT, description)

recipe_ingredient_already_exists = _response(RecipeIngredientAlreadyExists.description)

recipe_material_already_exists = _response(RecipeMaterialAlreadyExists.description)

sale_product_already_exists = _response(SaleProductAlreadyExists.description)
