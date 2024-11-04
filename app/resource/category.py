from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import category_not_found, invalid_payload
from app.service import category_service
from app.schema import category_schema


ns = Namespace(
    'category',
    description='Category related operations',
    path='/category',
    validate=True
)
category = ns.model('Category', category_schema)


@ns.route('/')
class Category(Resource):
    @ns.doc('create')
    @ns.expect(category)
    @ns.marshal_with(category, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new category '''
        return category_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(category)
    def get(self):
        ''' Get all categories '''
        return category_service.get_all()


@ns.route('/<int:id>')
@ns.param('id', 'The category identifier')
@ns.response(*category_not_found)
class CategoryById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(category)
    def get(self, id: int):
        ''' Get a category by ID '''
        return category_service.get_one_by('id', id)

    @ns.doc('update')
    @ns.expect(category)
    @ns.marshal_with(category)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a category by ID '''
        return category_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a category by ID '''
        category_service.delete(id)
        return '', HTTPStatus.NO_CONTENT
