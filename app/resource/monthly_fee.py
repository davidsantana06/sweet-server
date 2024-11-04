from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import invalid_payload, monthly_fee_not_found
from app.service import monthly_fee_service
from app.schema import monthly_fee_schema


ns = Namespace(
    'monthly_fee',
    description='Monthly fee related operations',
    path='/monthly_fee',
    validate=True
)
monthly_fee = ns.model('MonthlyFee', monthly_fee_schema)


@ns.route('/')
class MonthlyFee(Resource):
    @ns.doc('create')
    @ns.expect(monthly_fee)
    @ns.marshal_with(monthly_fee, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new monthly fee '''
        return monthly_fee_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(monthly_fee)
    def get(self):
        ''' Get all monthly fees '''
        return monthly_fee_service.get_all()


@ns.route('/<int:id>')
@ns.param('id', 'The monthly fee identifier')
@ns.response(*monthly_fee_not_found)
class MonthlyFeeById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(monthly_fee)
    def get(self, id: int):
        ''' Get a monthly fee by ID '''
        return monthly_fee_service.get_one_by_id(id)

    @ns.doc('update')
    @ns.expect(monthly_fee)
    @ns.marshal_with(monthly_fee)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a monthly fee by ID '''
        return monthly_fee_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a monthly fee by ID '''
        monthly_fee_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/search/<string:name>')
@ns.param('name', 'The monthly fee identifier')
class MonthlyFeeByName(Resource):
    @ns.doc('get_all_by_name')
    @ns.marshal_with(monthly_fee)
    def get(self, name: str):
        ''' Get all monthly fees by name '''
        return monthly_fee_service.get_all_by_name(name)
