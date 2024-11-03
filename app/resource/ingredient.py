from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import ingredient_not_found, invalid_payload
from app.service import ingredient_service
from app.schema import ingredient_schema


ingredient_ns = Namespace(
    'ingredient',
    description='Ingredient related operations',
    path='/ingredient',
    validate=True
)
ingredient = ingredient_ns.model('Ingredient', ingredient_schema)


@ingredient_ns.route('/')
class Ingredient(Resource):
    @ingredient_ns.doc('create')
    @ingredient_ns.expect(ingredient)
    @ingredient_ns.marshal_with(ingredient, code=HTTPStatus.CREATED)
    @ingredient_ns.response(*invalid_payload)
    def post(self):
        ''' Create a new ingredient '''
        return ingredient_service.create(ingredient_ns.payload), HTTPStatus.CREATED

    @ingredient_ns.doc('get_all')
    @ingredient_ns.marshal_list_with(ingredient)
    def get(self):
        ''' Get all ingredients '''
        return ingredient_service.get_all()


@ingredient_ns.route('/<int:id>')
@ingredient_ns.param('id', 'The ingredient identifier')
@ingredient_ns.response(*ingredient_not_found)
class IngredientById(Resource):
    @ingredient_ns.doc('get_one')
    @ingredient_ns.marshal_with(ingredient)
    def get(self, id: int):
        ''' Get a ingredient by ID '''
        return ingredient_service.get_one_by_id(id)

    @ingredient_ns.doc('update')
    @ingredient_ns.expect(ingredient)
    @ingredient_ns.marshal_with(ingredient)
    @ingredient_ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a ingredient by ID '''
        return ingredient_service.update(id, ingredient_ns.payload)

    @ingredient_ns.doc('delete')
    @ingredient_ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a ingredient by ID '''
        ingredient_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@ingredient_ns.route('/search/<string:name>')
@ingredient_ns.param('name', 'The ingredient name')
class IngredientByName(Resource):
    @ingredient_ns.doc('get_all_by_name')
    @ingredient_ns.marshal_list_with(ingredient)
    def get(self, name: str):
        ''' Get all ingredients by name '''
        return ingredient_service.get_all_by_name(name)


@ingredient_ns.route('/search/<int:id_recipe>')
@ingredient_ns.param('id_recipe', 'The recipe identifier')
class IngredientByIdRecipe(Resource):
    @ingredient_ns.doc('get_all_unrelated_to_recipe')
    @ingredient_ns.marshal_list_with(ingredient)
    def get(self, id_recipe: int):
        ''' Get all ingredients unrelated to a recipe by its ID '''
        return ingredient_service.get_all_unrelated_to_recipe(id_recipe)
