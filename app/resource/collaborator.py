from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import collaborator_not_found, invalid_payload
from app.service import collaborator_service
from app.schema import collaborator_schema


collaborator_ns = Namespace(
    'collaborator',
    description='Collaborator related operations',
    path='/collaborator',
    validate=True
)
collaborator = collaborator_ns.model('Collaborator', collaborator_schema)


@collaborator_ns.route('/')
class Collaborator(Resource):
    @collaborator_ns.doc('create')
    @collaborator_ns.expect(collaborator)
    @collaborator_ns.marshal_with(collaborator, code=HTTPStatus.CREATED)
    @collaborator_ns.response(*invalid_payload)
    def post(self):
        ''' Create a new collaborator '''
        return collaborator_service.create(collaborator_ns.payload), HTTPStatus.CREATED

    @collaborator_ns.doc('get_all')
    @collaborator_ns.marshal_list_with(collaborator)
    def get(self):
        ''' Get all collaborators '''
        return collaborator_service.get_all()


@collaborator_ns.route('/<int:id>')
@collaborator_ns.param('id', 'The collaborator identifier')
@collaborator_ns.response(*collaborator_not_found)
class CollaboratorById(Resource):
    @collaborator_ns.doc('get_one')
    @collaborator_ns.marshal_with(collaborator)
    def get(self, id: int):
        ''' Get a collaborator by ID '''
        return collaborator_service.get_one_by_id(id, except_default=False)

    @collaborator_ns.doc('update')
    @collaborator_ns.expect(collaborator)
    @collaborator_ns.marshal_with(collaborator)
    @collaborator_ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a collaborator by ID '''
        return collaborator_service.update(id, collaborator_ns.payload)

    @collaborator_ns.doc('delete')
    @collaborator_ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a collaborator by ID '''
        collaborator_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@collaborator_ns.route('/search/<string:name>')
@collaborator_ns.param('name', 'The collaborator name')
class CollaboratorByName(Resource):
    @collaborator_ns.doc('get_all_by_name')
    @collaborator_ns.marshal_list_with(collaborator)
    def get(self, name: str):
        ''' Get all collaborators by name '''
        return collaborator_service.get_all_by_name(name)
