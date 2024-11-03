from flask_restx import Namespace, Resource

from app.exception import invalid_payload, user_not_found
from app.service import user_service
from app.schema import user_schema


user_ns = Namespace(
    'user',
    description='User related operations',
    path='/user',
    validate=True
)
user = user_ns.model('User', user_schema)


@user_ns.route('/')
class User(Resource):
    @user_ns.doc('get_one')
    @user_ns.marshal_with(user)
    @user_ns.response(*user_not_found)
    def get(self):
        ''' Get the user '''
        return user_service.get_one()

    @user_ns.doc('update')
    @user_ns.expect(user)
    @user_ns.marshal_with(user)
    @user_ns.response(*invalid_payload)
    def put(self):
        ''' Update the user '''
        return user_service.update(user_ns.payload)
