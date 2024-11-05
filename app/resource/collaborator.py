from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import collaborator_not_found, invalid_payload
from app.service import collaborator_service
from app.schema import collaborator_schema


ns = Namespace(
    'collaborator',
    description='Collaborator related operations',
    path='/collaborator',
    validate=True
)


@ns.route('/')
class Collaborator(Resource):
    @ns.doc('create')
    @ns.expect(collaborator_schema)
    @ns.marshal_with(collaborator_schema, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new collaborator '''
        return collaborator_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(collaborator_schema)
    def get(self):
        ''' Get all collaborators '''
        return collaborator_service.get_all()


@ns.route('/<int:id>')
@ns.param('id', 'The collaborator identifier')
@ns.response(*collaborator_not_found)
class CollaboratorById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(collaborator_schema)
    def get(self, id: int):
        ''' Get a collaborator by ID '''
        return collaborator_service.get_one_by_id(id, except_default=False)

    @ns.doc('update')
    @ns.expect(collaborator_schema)
    @ns.marshal_with(collaborator_schema)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a collaborator by ID '''
        return collaborator_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a collaborator by ID '''
        collaborator_service.delete(id)
        return '', HTTPStatus.NO_CONTENT


@ns.route('/search/<string:name>')
@ns.param('name', 'The collaborator name')
class CollaboratorByName(Resource):
    @ns.doc('get_all_by_name')
    @ns.marshal_list_with(collaborator_schema)
    def get(self, name: str):
        ''' Get all collaborators by name '''
        return collaborator_service.get_all_by_name(name)
