from flask_restx import Namespace, Resource

from app.exception import invalid_payload, user_not_found
from app.schema import user_schema
from app.service import user_service


ns = Namespace(
    'user',
    description='User related operations',
    path='/user',
    validate=True
)


@ns.route('/')
class User(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(user_schema)
    @ns.response(*user_not_found)
    def get(self):
        ''' Get the user '''
        return user_service.get_one()

    @ns.doc('update')
    @ns.expect(user_schema)
    @ns.marshal_with(user_schema)
    @ns.response(*invalid_payload)
    def put(self):
        ''' Update the user '''
        return user_service.update(ns.payload)
