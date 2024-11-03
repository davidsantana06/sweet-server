from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import invalid_payload, material_not_found
from app.service import material_service
from app.schema import material_schema


material_ns = Namespace(
    'material',
    description='Material related operations',
    path='/material',
    validate=True
)
material = material_ns.model('Material', material_schema)


@material_ns.route('/')
class Material(Resource):
    @material_ns.doc('create')
    @material_ns.expect(material)
    @material_ns.marshal_with(material, code=HTTPStatus.CREATED)
    @material_ns.response(*invalid_payload)
    def post(self):
        ''' Create a new material '''
        return material_service.create(material_ns.payload), HTTPStatus.CREATED

    @material_ns.doc('get_all')
    @material_ns.marshal_list_with(material)
    def get(self):
        ''' Get all materials '''
        return material_service.get_all()


@material_ns.route('/<int:id>')
@material_ns.param('id', 'The material identifier')
@material_ns.response(*material_not_found)
class MaterialById(Resource):
    @material_ns.doc('get_one')
    @material_ns.marshal_with(material)
    def get(self, id: int):
        ''' Get a material by ID '''
        return material_service.get_one_by_id(id)

    @material_ns.doc('update')
    @material_ns.expect(material)
    @material_ns.marshal_with(material)
    @material_ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a material by ID '''
        return material_service.update(id, material_ns.payload)

    @material_ns.doc('delete')
    @material_ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a material by ID '''
        material_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@material_ns.route('/search/<string:name>')
@material_ns.param('name', 'The material name')
class MaterialByName(Resource):
    @material_ns.doc('get_all_by_name')
    @material_ns.marshal_list_with(material)
    def get(self, name: str):
        ''' Get all materials by name '''
        return material_service.get_all_by_name(name)


@material_ns.route('/search/<int:id_recipe>')
@material_ns.param('id_recipe', 'The recipe identifier')
class MaterialByIdRecipe(Resource):
    @material_ns.doc('get_all_unrelated_to_recipe')
    @material_ns.marshal_list_with(material)
    def get(self, id_recipe: int):
        ''' Get all materials unrelated to a recipe by its ID '''
        return material_service.get_all_unrelated_to_recipe(id_recipe)
