from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response

from . import operations as monthly_fee_operations, monthly_fee
from .forms import MonthlyFeeForm


@monthly_fee.post('/create')
@login_required
def create():
    form = MonthlyFeeForm(request.form)
    monthly_fee = monthly_fee_operations.create(*form.data)
    return response.as_model(monthly_fee, HTTPStatus.CREATED)


@monthly_fee.get('/all')
@login_required
def get_all():
    return response.as_models(monthly_fee_operations.get_all())


@monthly_fee.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return response.as_models(
        monthly_fee_operations.get_all_by_name(name)
    )


@monthly_fee.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return response.as_model(
        monthly_fee_operations.get_one_by_id(id)
    )


@monthly_fee.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = MonthlyFeeForm(request.form)
    monthly_fee = monthly_fee_operations.get_one_by_id(id)
    monthly_fee = monthly_fee_operations.update(monthly_fee, form)
    return response.as_model(monthly_fee)


@monthly_fee.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    monthly_fee = monthly_fee_operations.get_one_by_id(id)
    monthly_fee_operations.delete(monthly_fee)
    return response.as_message('The monthly fee was deleted.')
