from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    product_not_found,
)
from app.service import product_service
from app.schema import product_schema


ns = Namespace(
    'product',
    description='Product related operations',
    path='/product',
    validate=True
)


@ns.route('/')
class Product(Resource):
    @ns.doc('create')
    @ns.expect(product_schema)
    @ns.marshal_with(product_schema, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(HTTPStatus.NOT_FOUND, 'Collaborator or recipe not found')
    def post(self):
        ''' Create a new product '''
        return product_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(product_schema)
    def get(self):
        ''' Get all products '''
        return product_service.get_all()


@ns.route('/<int:id>')
@ns.param('id', 'The product identifier')
class ProductById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(product_schema)
    @ns.response(*product_not_found)
    def get(self, id):
        ''' Get a product by ID '''
        return product_service.get_one_by_id(id)

    @ns.doc('update')
    @ns.expect(product_schema)
    @ns.marshal_with(product_schema)
    @ns.response(*invalid_payload)
    @ns.response(HTTPStatus.NOT_FOUND, 'Collaborator, product or recipe not found')
    def put(self, id):
        ''' Update a product by ID '''
        return product_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    @ns.response(*product_not_found)
    def delete(self, id):
        ''' Delete a product by ID '''
        product_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/search/<int:id_sale>')
@ns.param('id_sale', 'The sale identifier')
class ProductByIdSale(Resource):
    @ns.doc('get_all_unrelated_to_sale')
    @ns.marshal_list_with(product_schema)
    def get(self, id_sale):
        ''' Get all products unrelated to a sale by its ID '''
        return product_service.get_all_unrelated_to_sale(id_sale)


@ns.route('/search/<string:name>')
@ns.param('name', 'The product name')
class ProductByName(Resource):
    @ns.doc('get_all_by_name')
    @ns.marshal_with(product_schema)
    def get(self, name):
        ''' Get all products by name '''
        return product_service.get_all_by_name(name)
