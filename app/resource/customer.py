from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import customer_not_found, invalid_payload
from app.service import customer_service
from app.schema import customer_schema


customer_ns = Namespace(
    'customer',
    description='Customer related operations',
    path='/customer',
    validate=True
)
customer = customer_ns.model('Customer', customer_schema)


@customer_ns.route('/')
class Customer(Resource):
    @customer_ns.doc('create')
    @customer_ns.expect(customer)
    @customer_ns.marshal_with(customer, code=HTTPStatus.CREATED)
    @customer_ns.response(*invalid_payload)
    def post(self):
        ''' Create a new customer '''
        return customer_service.create(customer_ns.payload), HTTPStatus.CREATED

    @customer_ns.doc('get_all')
    @customer_ns.marshal_list_with(customer)
    def get(self):
        ''' Get all customers '''
        return customer_service.get_all()


@customer_ns.route('/<int:id>')
@customer_ns.param('id', 'The customer identifier')
@customer_ns.response(*customer_not_found)
class CustomerById(Resource):
    @customer_ns.doc('get_one')
    @customer_ns.marshal_with(customer)
    def get(self, id: int):
        ''' Get a customer by ID '''
        return customer_service.get_one_by_id(id)

    @customer_ns.doc('update')
    @customer_ns.expect(customer)
    @customer_ns.marshal_with(customer)
    @customer_ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a customer by ID '''
        return customer_service.update(id, customer_ns.payload)

    @customer_ns.doc('delete')
    @customer_ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a customer by ID '''
        customer_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@customer_ns.route('/search/<string:name>')
@customer_ns.param('name', 'The customer name')
class CustomerByName(Resource):
    @customer_ns.doc('get_all_by_name')
    @customer_ns.marshal_list_with(customer)
    def get(self, name: str):
        ''' Get all customers by name '''
        return customer_service.get_all_by_name(name)
