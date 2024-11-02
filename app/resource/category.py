from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import category_not_found, invalid_payload
from app.service import category_service
from app.schema import category_schema


category_ns = Namespace(
    'category',
    description='Category related operations',
    path='/category',
    validate=True
)
category = category_ns.model('Category', category_schema)


@category_ns.route('/')
class Category(Resource):
    @category_ns.doc('create')
    @category_ns.expect(category)
    @category_ns.marshal_with(category, code=HTTPStatus.CREATED)
    @category_ns.response(*invalid_payload)
    def post(self):
        ''' Create a new category '''
        return category_service.create(category_ns.payload), HTTPStatus.CREATED

    @category_ns.doc('get_all')
    @category_ns.marshal_list_with(category)
    def get(self):
        ''' Get all categories '''
        return category_service.get_all()


@category_ns.route('/<int:id>')
@category_ns.param('id', 'The category identifier')
@category_ns.response(*category_not_found)
class CategoryById(Resource):
    @category_ns.doc('get_one')
    @category_ns.marshal_with(category)
    def get(self, id: int):
        ''' Get a category by ID '''
        return category_service.get_one_by('id', id)

    @category_ns.doc('update')
    @category_ns.expect(category)
    @category_ns.marshal_with(category)
    @category_ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a category by ID '''
        return category_service.update(id, category_ns.payload)

    @category_ns.doc('delete')
    @category_ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a category by ID '''
        category_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@category_ns.route('/search/<string:name>')
@category_ns.param('name', 'The category name')
class CategoryByName(Resource):
    @category_ns.doc('get_all_by_name')
    @category_ns.marshal_list_with(category)
    def get(self, name: str):
        ''' Get all categories by name '''
        return category_service.get_all_by_name(name)
