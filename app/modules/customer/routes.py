from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response

from . import operations as customer_operations, customer
from .forms import CustomerForm


@customer.post('/create')
@login_required
def create():
    form = CustomerForm(request.form)
    customer = customer_operations.create(*form.data)
    return response.as_model(customer, HTTPStatus.CREATED)


@customer.get('/all')
@login_required
def get_all():
    return response.as_models(customer_operations.get_all())


@customer.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return response.as_models(
        customer_operations.get_all_by_name(name)
    )


@customer.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return response.as_select_choices(
        customer_operations.get_all_select_choices()
    )


@customer.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return response.as_model(
        customer_operations.get_one_by_id(id)
    )


@customer.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = CustomerForm(request.form)
    customer = customer_operations.get_one_by_id(id)
    customer = customer_operations.update(customer, form)
    return response.as_model(customer)


@customer.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    customer = customer_operations.get_one_by_id(id)
    customer_operations.delete(customer)
    return response.as_message('The customer was deleted.')
