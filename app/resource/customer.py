from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import customer_not_found, invalid_payload
from app.service import customer_service
from app.schema import customer_schema


ns = Namespace(
    'customer',
    description='Customer related operations',
    path='/customer',
    validate=True
)


@ns.route('/')
class Customer(Resource):
    @ns.doc('create')
    @ns.expect(customer_schema)
    @ns.marshal_with(customer_schema, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new customer '''
        return customer_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(customer_schema)
    def get(self):
        ''' Get all customers '''
        return customer_service.get_all()


@ns.route('/<int:id>')
@ns.param('id', 'The customer identifier')
@ns.response(*customer_not_found)
class CustomerById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(customer_schema)
    def get(self, id: int):
        ''' Get a customer by ID '''
        return customer_service.get_one_by_id(id)

    @ns.doc('update')
    @ns.expect(customer_schema)
    @ns.marshal_with(customer_schema)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a customer by ID '''
        return customer_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a customer by ID '''
        customer_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/search/<string:name>')
@ns.param('name', 'The customer name')
class CustomerByName(Resource):
    @ns.doc('get_all_by_name')
    @ns.marshal_list_with(customer_schema)
    def get(self, name: str):
        ''' Get all customers by name '''
        return customer_service.get_all_by_name(name)
