from http import HTTPStatus
from werkzeug.exceptions import NotFound


class CategoryNotFound(NotFound):
    description = 'Category not found'


class CollaboratorNotFound(NotFound):
    description = 'Collaborator not found'


class CustomerNotFound(NotFound):
    description = 'Customer not found'


class IngredientNotFound(NotFound):
    description = 'Ingredient not found'


class MaterialNotFound(NotFound):
    description = 'Material not found'


class MonthlyFeeNotFound(NotFound):
    description = 'Monthly fee not found'


class PaymentMethotNotFound(NotFound):
    description = 'Payment method not found'


class ProductNotFound(NotFound):
    description = 'Product not found'


class RecipeNotFound(NotFound):
    description = 'Recipe not found'


class RecipeIngredientNotFound(NotFound):
    description = 'Recipe-ingredient relation not found'


class RecipeMaterialNotFound(NotFound):
    description = 'Recipe-material relation not found'


class UserNotFound(NotFound):
    description = 'User not found'


_response = lambda exception: (HTTPStatus.NOT_FOUND, exception.description)

category_not_found = _response(CategoryNotFound)

collaborator_not_found = _response(CollaboratorNotFound)

customer_not_found = _response(CustomerNotFound)

ingredient_not_found = _response(IngredientNotFound)

material_not_found = _response(MaterialNotFound)

monthly_fee_not_found = _response(MonthlyFeeNotFound)

payment_method_not_found = _response(PaymentMethotNotFound)

product_not_found = _response(ProductNotFound)

recipe_not_found = _response(RecipeNotFound)

recipe_ingredient_not_found = _response(RecipeIngredientNotFound)

recipe_material_not_found = _response(RecipeMaterialNotFound)

user_not_found = _response(UserNotFound)
