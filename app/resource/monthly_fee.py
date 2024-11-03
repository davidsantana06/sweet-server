from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import invalid_payload, monthly_fee_not_found
from app.service import monthly_fee_service
from app.schema import monthly_fee_schema


monthly_fee_ns = Namespace(
    'monthly_fee',
    description='Monthly fee related operations',
    path='/monthly_fee',
    validate=True
)
monthly_fee = monthly_fee_ns.model('MonthlyFee', monthly_fee_schema)


@monthly_fee_ns.route('/')
class MonthlyFee(Resource):
    @monthly_fee_ns.doc('create')
    @monthly_fee_ns.expect(monthly_fee)
    @monthly_fee_ns.marshal_with(monthly_fee, code=HTTPStatus.CREATED)
    @monthly_fee_ns.response(*invalid_payload)
    def post(self):
        ''' Create a new monthly fee '''
        return monthly_fee_service.create(monthly_fee_ns.payload), HTTPStatus.CREATED

    @monthly_fee_ns.doc('get_all')
    @monthly_fee_ns.marshal_list_with(monthly_fee)
    def get(self):
        ''' Get all monthly fees '''
        return monthly_fee_service.get_all()


@monthly_fee_ns.route('/<int:id>')
@monthly_fee_ns.param('id', 'The monthly fee identifier')
@monthly_fee_ns.response(*monthly_fee_not_found)
class MonthlyFeeById(Resource):
    @monthly_fee_ns.doc('get_one')
    @monthly_fee_ns.marshal_with(monthly_fee)
    def get(self, id: int):
        ''' Get a monthly fee by ID '''
        return monthly_fee_service.get_one_by_id(id)

    @monthly_fee_ns.doc('update')
    @monthly_fee_ns.expect(monthly_fee)
    @monthly_fee_ns.marshal_with(monthly_fee)
    @monthly_fee_ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a monthly fee by ID '''
        return monthly_fee_service.update(id, monthly_fee_ns.payload)

    @monthly_fee_ns.doc('delete')
    @monthly_fee_ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a monthly fee by ID '''
        monthly_fee_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@monthly_fee_ns.route('/search/<string:name>')
@monthly_fee_ns.param('name', 'The monthly fee identifier')
class MonthlyFeeByName(Resource):
    @monthly_fee_ns.doc('get_all_by_name')
    @monthly_fee_ns.marshal_with(monthly_fee)
    def get(self, name: str):
        ''' Get all monthly fees by name '''
        return monthly_fee_service.get_all_by_name(name)
