from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import invalid_payload, payment_method_not_found
from app.service import payment_method_service
from app.schema import payment_method_schema


payment_method_ns = Namespace(
    'payment_method',
    description='Payment method related operations',
    path='/payment-method',
    validate=True
)
payment_method = payment_method_ns.model(
    'PaymentMethod',
    payment_method_schema
)


@payment_method_ns.route('/')
class PaymentMethod(Resource):
    @payment_method_ns.doc('create')
    @payment_method_ns.expect(payment_method)
    @payment_method_ns.marshal_with(payment_method, code=HTTPStatus.CREATED)
    @payment_method_ns.response(*invalid_payload)
    def post(self):
        ''' Create a new payment method '''
        return payment_method_service.create(payment_method_ns.payload), HTTPStatus.CREATED

    @payment_method_ns.doc('get_all')
    @payment_method_ns.marshal_list_with(payment_method)
    def get(self):
        ''' Get all payment methods '''
        return payment_method_service.get_all()


@payment_method_ns.route('/<int:id>')
@payment_method_ns.param('id', 'The payment method identifier')
@payment_method_ns.response(*payment_method_not_found)
class PaymentMethodById(Resource):
    @payment_method_ns.doc('get_one')
    @payment_method_ns.marshal_with(payment_method)
    def get(self, id: int):
        ''' Get a payment method by ID '''
        return payment_method_service.get_one_by('id', id)

    @payment_method_ns.doc('update')
    @payment_method_ns.expect(payment_method)
    @payment_method_ns.marshal_with(payment_method)
    @payment_method_ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a payment method by ID '''
        return payment_method_service.update(id, payment_method_ns.payload)

    @payment_method_ns.doc('delete')
    @payment_method_ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a payment method by ID '''
        payment_method_service.delete(id)
        return '', HTTPStatus.NO_CONTENT
