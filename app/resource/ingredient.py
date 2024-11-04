from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import ingredient_not_found, invalid_payload
from app.service import ingredient_service
from app.schema import ingredient_schema


ns = Namespace(
    'ingredient',
    description='Ingredient related operations',
    path='/ingredient',
    validate=True
)
ingredient = ns.model('Ingredient', ingredient_schema)


@ns.route('/')
class Ingredient(Resource):
    @ns.doc('create')
    @ns.expect(ingredient)
    @ns.marshal_with(ingredient, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new ingredient '''
        return ingredient_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(ingredient)
    def get(self):
        ''' Get all ingredients '''
        return ingredient_service.get_all()


@ns.route('/<int:id>')
@ns.param('id', 'The ingredient identifier')
@ns.response(*ingredient_not_found)
class IngredientById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(ingredient)
    def get(self, id: int):
        ''' Get a ingredient by ID '''
        return ingredient_service.get_one_by_id(id)

    @ns.doc('update')
    @ns.expect(ingredient)
    @ns.marshal_with(ingredient)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a ingredient by ID '''
        return ingredient_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a ingredient by ID '''
        ingredient_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/search/<string:name>')
@ns.param('name', 'The ingredient name')
class IngredientByName(Resource):
    @ns.doc('get_all_by_name')
    @ns.marshal_list_with(ingredient)
    def get(self, name: str):
        ''' Get all ingredients by name '''
        return ingredient_service.get_all_by_name(name)


@ns.route('/search/<int:id_recipe>')
@ns.param('id_recipe', 'The recipe identifier')
class IngredientByIdRecipe(Resource):
    @ns.doc('get_all_unrelated_to_recipe')
    @ns.marshal_list_with(ingredient)
    def get(self, id_recipe: int):
        ''' Get all ingredients unrelated to a recipe by its ID '''
        return ingredient_service.get_all_unrelated_to_recipe(id_recipe)
