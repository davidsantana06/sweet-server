from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response

from . import operations as labor_operations, labor
from .forms import CreateForm, UpdateForm


@labor.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    labor = labor_operations.create(*form.data)
    return response.as_model(labor, HTTPStatus.CREATED)


@labor.get('/all')
@login_required
def get_all():
    return response.as_models(labor_operations.get_all())


@labor.get('/all/<string:person_name>')
@login_required
def get_all_by_person_name(person_name: str):
    return response.as_models(
        labor_operations.get_all_by_person_name(person_name)
    )


@labor.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return response.as_select_choices(
        labor_operations.get_all_select_choices()
    )


@labor.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return response.as_model(
        labor_operations.get_one_by_id(id)
    )


@labor.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = UpdateForm(request.form)
    labor = labor_operations.get_one_by_id(id)
    labor = labor_operations.update(labor, form)
    return response.as_model(labor)


@labor.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    labor = labor_operations.get_one_by_id(id)
    labor_operations.delete(labor)
    return response.as_message('The labor was deleted.')
