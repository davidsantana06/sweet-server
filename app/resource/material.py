from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import invalid_payload, material_not_found
from app.service import material_service
from app.schema import material_schema


ns = Namespace(
    'material',
    description='Material related operations',
    path='/material',
    validate=True
)


@ns.route('/')
class Material(Resource):
    @ns.doc('create')
    @ns.expect(material_schema)
    @ns.marshal_with(material_schema, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new material '''
        return material_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(material_schema)
    def get(self):
        ''' Get all materials '''
        return material_service.get_all()


@ns.route('/<int:id>')
@ns.param('id', 'The material identifier')
@ns.response(*material_not_found)
class MaterialById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(material_schema)
    def get(self, id: int):
        ''' Get a material by ID '''
        return material_service.get_one_by_id(id)

    @ns.doc('update')
    @ns.expect(material_schema)
    @ns.marshal_with(material_schema)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a material by ID '''
        return material_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a material by ID '''
        material_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/search/<int:id_recipe>')
@ns.param('id_recipe', 'The recipe identifier')
class MaterialByIdRecipe(Resource):
    @ns.doc('get_all_unrelated_to_recipe')
    @ns.marshal_list_with(material_schema)
    def get(self, id_recipe: int):
        ''' Get all materials unrelated to a recipe by its ID '''
        return material_service.get_all_unrelated_to_recipe(id_recipe)
    

@ns.route('/search/<string:name>')
@ns.param('name', 'The material name')
class MaterialByName(Resource):
    @ns.doc('get_all_by_name')
    @ns.marshal_list_with(material_schema)
    def get(self, name: str):
        ''' Get all materials by name '''
        return material_service.get_all_by_name(name)
