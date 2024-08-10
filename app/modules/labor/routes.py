from flask import request
from http import HTTPStatus
from flask_login import login_required

from app import operations as app_operations

from . import operations as labor_operations, labor
from .forms import CreateForm, UpdateForm


@labor.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    form.hourly_rate.data = float(form.hourly_rate.data)
    if app_operations.validate_form(form):
        labor = labor_operations.create(
            form.person_name.data,
            form.hourly_rate.data
        )
    return labor.to_dict(), HTTPStatus.CREATED


@labor.get('/all')
@login_required
def get_all():
    return [
        labor.to_dict() for labor
        in labor_operations.get_all()
    ]


@labor.get('all/<string:person_name>')
@login_required
def get_all_by_person_name(person_name: str):
    return [
        labor.to_dict() for labor
        in labor_operations.get_all_by_person_name(person_name)
    ]


@labor.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return [
        {'id': id, 'name': name} for id, name
        in labor_operations.get_all_select_choices()
    ]


@labor.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return labor_operations.get_one_by_id(id).to_dict()


@labor.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = UpdateForm(request.form)
    labor = labor_operations.get_one_by_id(id)
    if app_operations.validate_form(form):
        labor = labor_operations.update(labor, form)
    return labor.to_dict()


@labor.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    labor = labor_operations.get_one_by_id(id)
    labor_operations.delete(labor)
    return {'message': 'The labor was deleted.'}
