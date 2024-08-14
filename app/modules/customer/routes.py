from flask import request
from http import HTTPStatus
from flask_login import login_required

from app import operations as app_operations

from . import operations as customer_operations, customer
from .forms import CreateForm, UpdateForm


@customer.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    app_operations.validate_form(form)
    customer = customer_operations.create(
        form.name.data,
        form.phone.data,
        form.instagram.data,
        form.notes.data
    )
    return customer.to_dict(), HTTPStatus.CREATED


@customer.get('/all')
@login_required
def get_all():
    return [
        customer.to_dict() for customer
        in customer_operations.get_all()
    ]


@customer.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return [
        customer.to_dict() for customer
        in customer_operations.get_all_by_name(name)
    ]


@customer.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return [
        {'id': id, 'name': name} for id, name
        in customer_operations.get_all_select_choices()
    ]


@customer.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return customer_operations.get_one_by_id(id).to_dict()


@customer.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = UpdateForm(request.form)
    customer = customer_operations.get_one_by_id(id)
    app_operations.validate_form(form)
    customer = customer_operations.update(customer, form)
    return customer.to_dict()


@customer.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    customer = customer_operations.get_one_by_id(id)
    customer_operations.delete(customer)
    return {'message': 'The customer was deleted.'}
