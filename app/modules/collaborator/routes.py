from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response

from . import operations as collaborator_operations, collaborator
from .forms import CollaboratorForm


@collaborator.post('/create')
@login_required
def create():
    form = CollaboratorForm(request.form)
    collaborator = collaborator_operations.create(*form.data)
    return response.as_model(collaborator, HTTPStatus.CREATED)


@collaborator.get('/all')
@login_required
def get_all():
    return response.as_models(collaborator_operations.get_all())


@collaborator.get('/all/<string:person_name>')
@login_required
def get_all_by_person_name(person_name: str):
    return response.as_models(
        collaborator_operations.get_all_by_person_name(person_name)
    )


@collaborator.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return response.as_select_choices(
        collaborator_operations.get_all_select_choices()
    )


@collaborator.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return response.as_model(
        collaborator_operations.get_one_by_id(id)
    )


@collaborator.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = CollaboratorForm(request.form)
    collaborator = collaborator_operations.get_one_by_id(id)
    collaborator = collaborator_operations.update(collaborator, form)
    return response.as_model(collaborator)


@collaborator.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    collaborator = collaborator_operations.get_one_by_id(id)
    collaborator_operations.delete(collaborator)
    return response.as_message('The collaborator was deleted.')
