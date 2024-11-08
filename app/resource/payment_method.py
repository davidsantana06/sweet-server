from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import invalid_payload, payment_method_not_found
from app.schema import payment_method_schema
from app.service import payment_method_service


ns = Namespace(
    'payment_method',
    description='Payment method related operations',
    path='/payment-method',
    validate=True
)


@ns.route('/')
class PaymentMethod(Resource):
    @ns.doc('create')
    @ns.expect(payment_method_schema)
    @ns.marshal_with(payment_method_schema, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new payment method '''
        return payment_method_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(payment_method_schema)
    def get(self):
        ''' Get all payment methods '''
        return payment_method_service.get_all()


@ns.route('/<int:id>')
@ns.param('id', 'The payment method identifier')
@ns.response(*payment_method_not_found)
class PaymentMethodById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(payment_method_schema)
    def get(self, id: int):
        ''' Get a payment method by ID '''
        return payment_method_service.get_one_by('id', id)

    @ns.doc('update')
    @ns.expect(payment_method_schema)
    @ns.marshal_with(payment_method_schema)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a payment method by ID '''
        return payment_method_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a payment method by ID '''
        payment_method_service.delete(id)
        return '', HTTPStatus.NO_CONTENT
