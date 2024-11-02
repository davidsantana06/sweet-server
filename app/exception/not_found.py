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


class UserNotFound(NotFound):
    description = 'User not found'


_exception = lambda exception: (HTTPStatus.NOT_FOUND, exception.description)
category_not_found = _exception(CategoryNotFound)
collaborator_not_found = _exception(CollaboratorNotFound)
customer_not_found = _exception(CustomerNotFound)
ingredient_not_found = _exception(IngredientNotFound)
material_not_found = _exception(MaterialNotFound)
monthly_fee_not_found = _exception(MonthlyFeeNotFound)
payment_method_not_found = _exception(PaymentMethotNotFound)
product_not_found = _exception(ProductNotFound)
recipe_not_found = _exception(RecipeNotFound)
user_not_found = _exception(UserNotFound)
