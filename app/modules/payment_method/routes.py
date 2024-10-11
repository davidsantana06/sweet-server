from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response

from . import operations as payment_method_operations, payment_method
from .forms import PaymentMethodForm


@payment_method.post('/create')
@login_required
def create():
    form = PaymentMethodForm(request.form)
    payment_method = payment_method_operations.create(*form.data)
    return response.as_model(payment_method, HTTPStatus.CREATED)


@payment_method.get('/all')
@login_required
def get_all():
    return response.as_models(payment_method_operations.get_all())


@payment_method.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return response.as_models(
        payment_method_operations.get_all_by_name(name)
    )


@payment_method.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return response.as_select_choices(
        payment_method_operations.get_all_select_choices()
    )


@payment_method.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return response.as_model(
        payment_method_operations.get_one_by('id', id)
    )


@payment_method.patch('/update/<int:id>')
def update(id: int):
    form = PaymentMethodForm(request.form)
    payment_method = payment_method_operations.get_one_by('id', id)
    payment_method = payment_method_operations.update(
        payment_method,
        form
    )
    return response.as_model(payment_method)


@payment_method.delete('/delete/<int:id>')
def delete(id: int):
    payment_method = payment_method_operations.get_one_by('id', id)
    payment_method_operations.delete(payment_method)
    return response.as_message('The payment method was deleted.')
