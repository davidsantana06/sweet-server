from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    recipe_ingredient_already_exists,
    recipe_ingredient_not_found,
    recipe_material_already_exists,
    recipe_material_not_found,
    recipe_not_found
)
from app.service import recipe_service
from app.schema import recipe, recipe_ingredient, recipe_material


ns = Namespace(
    'recipe',
    description='Recipe related operations',
    path='/recipe',
    validate=True
)


@ns.route('/')
class Recipe(Resource):
    @ns.doc('create')
    @ns.expect(recipe)
    @ns.marshal_with(recipe, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new recipe '''
        return recipe_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(recipe)
    def get(self):
        ''' Get all recipes '''
        return recipe_service.get_all()


@ns.route('/ingredient')
@ns.response(*invalid_payload)
class RecipeIngredient(Resource):
    @ns.doc('create_ingredient_rel')
    @ns.expect(recipe_ingredient)
    @ns.marshal_with(recipe_ingredient, code=HTTPStatus.CREATED)
    @ns.response(HTTPStatus.NOT_FOUND, 'Recipe or ingredient not found')
    @ns.response(*recipe_ingredient_already_exists)
    def post(self):
        ''' Create a new recipe-ingredient relationship '''
        return recipe_service.create_ingredient_rel(ns.payload), HTTPStatus.CREATED

    @ns.doc('update_ingredient_rel')
    @ns.expect(recipe_ingredient)
    @ns.marshal_with(recipe_ingredient)
    @ns.response(*recipe_ingredient_not_found)
    def put(self):
        ''' Update a recipe-ingredient relationship '''
        return recipe_service.update_ingredient_rel(ns.payload)


@ns.route('/material')
@ns.response(*invalid_payload)
class RecipeMaterial(Resource):
    @ns.doc('create_material_rel')
    @ns.expect(recipe_material)
    @ns.marshal_with(recipe_material, code=HTTPStatus.CREATED)
    @ns.response(HTTPStatus.NOT_FOUND, 'Recipe or material not found')
    @ns.response(*recipe_material_already_exists)
    def post(self):
        ''' Create a new recipe-material relationship '''
        return recipe_service.create_material_rel(ns.payload), HTTPStatus.CREATED

    @ns.doc('update_material_rel')
    @ns.expect(recipe_material)
    @ns.marshal_with(recipe_material)
    @ns.response(*recipe_material_not_found)
    def put(self):
        ''' Update a recipe-material relationship '''
        return recipe_service.update_material_rel(ns.payload)


@ns.route('/<int:id>')
@ns.param('id', 'The recipe identifier')
@ns.response(*recipe_not_found)
class RecipeById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(recipe)
    def get(self, id: int):
        ''' Get a recipe by ID '''
        return recipe_service.get_one_by_id(id)

    @ns.doc('update')
    @ns.expect(recipe)
    @ns.marshal_with(recipe)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a recipe by ID '''
        return recipe_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a recipe by ID '''
        recipe_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/<int:id>/ingredient')
@ns.param('id', 'The recipe identifier')
class RecipeIngredientById(Resource):
    @ns.doc('get_all_ingredient_rels_by_id')
    @ns.marshal_list_with(recipe_ingredient)
    def get(self, id: int):
        ''' Get all recipe-ingredient relationships by recipe ID '''
        return recipe_service.get_all_ingredient_rels_by_id(id)


@ns.route('/<int:id>/ingredient/<int:id_ingredient>')
@ns.param('id', 'The recipe identifier')
@ns.param('id_ingredient', 'The ingredient identifier')
@ns.response(*recipe_ingredient_not_found)
class RecipeIngredientByIds(Resource):
    @ns.doc('get_one_ingredient_rel_by_ids')
    @ns.marshal_with(recipe_ingredient)
    def get(self, id: int, id_ingredient: int):
        ''' Get a recipe-ingredient relationship by (recipe) ID and ingredient ID '''
        return recipe_service.get_one_ingredient_rel_by_ids(id, id_ingredient)

    @ns.doc('delete_ingredient_rel')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int, id_ingredient: int):
        ''' Delete a recipe-ingredient relationship by (recipe) ID and ingredient ID '''
        recipe_service.delete_ingredient_rel(id, id_ingredient)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/<int:id>/material')
@ns.param('id', 'The recipe identifier')
class RecipeMaterialById(Resource):
    @ns.doc('get_all_material_rels_by_id')
    @ns.marshal_list_with(recipe_material)
    def get(self, id: int):
        ''' Get all recipe-material relationships by recipe ID '''
        return recipe_service.get_all_material_rels_by_id(id)


@ns.route('/<int:id>/material/<int:id_material>')
@ns.param('id', 'The recipe identifier')
@ns.param('id_material', 'The material identifier')
@ns.response(*recipe_material_not_found)
class RecipeMaterialByIds(Resource):
    @ns.doc('get_one_material_rel_by_ids')
    @ns.marshal_with(recipe_material)
    def get(self, id: int, id_material: int):
        ''' Get a recipe-material relationship by (recipe) ID and material ID '''
        return recipe_service.get_one_material_rel_by_ids(id, id_material)

    @ns.doc('delete_material_rel')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int, id_material: int):
        ''' Delete a recipe-material relationship by (recipe) ID and material ID '''
        recipe_service.delete_material_rel(id, id_material)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/search/<int:id_category>')
@ns.param('id_category', 'The category identifier')
class RecipeByCategory(Resource):
    @ns.doc('get_all_by_id_category')
    @ns.marshal_list_with(recipe)
    def get(self, id_category: int):
        ''' Get all recipes by category ID '''
        return recipe_service.get_all_by_id_category(id_category)


@ns.route('/search/<string:name>')
@ns.param('name', 'The recipe name')
class RecipeByName(Resource):
    @ns.doc('get_all_by_name')
    @ns.marshal_list_with(recipe)
    def get(self, name: str):
        ''' Get all recipes by name '''
        return recipe_service.get_all_by_name(name)
