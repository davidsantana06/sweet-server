from flask_restx import Namespace, Resource

from app.exception import invalid_payload, user_not_found
from app.service import user_service
from app.schema import user_schema


ns = Namespace(
    'user',
    description='User related operations',
    path='/user',
    validate=True
)
user = ns.model('User', user_schema)


@ns.route('/')
class User(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(user)
    @ns.response(*user_not_found)
    def get(self):
        ''' Get the user '''
        return user_service.get_one()

    @ns.doc('update')
    @ns.expect(user)
    @ns.marshal_with(user)
    @ns.response(*invalid_payload)
    def put(self):
        ''' Update the user '''
        return user_service.update(ns.payload)
