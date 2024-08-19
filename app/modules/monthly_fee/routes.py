from flask import request
from http import HTTPStatus
from flask_login import login_required

from app import operations as app_operations

from . import operations as monthly_fee_operations, monthly_fee
from .forms import CreateForm, UpdateForm


@monthly_fee.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    app_operations.validate_form(form)
    monthly_fee = monthly_fee_operations.create(
        form.name.data,
        form.description.data,
        form.value.data
    )
    return monthly_fee.to_dict(), HTTPStatus.CREATED


@monthly_fee.get('/all')
@login_required
def get_all():
    return [
        monthly_fee.to_dict() for monthly_fee
        in monthly_fee_operations.get_all()
    ]


@monthly_fee.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return [
        monthly_fee.to_dict() for monthly_fee
        in monthly_fee_operations.get_all_by_name(name)
    ]


@monthly_fee.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return monthly_fee_operations.get_one_by_id(id).to_dict()


@monthly_fee.patch('/update/<int:id>')
@login_required
def update(id: int):
    monthly_fee = monthly_fee_operations.get_one_by_id(id)
    form = UpdateForm(request.form)
    app_operations.validate_form(form)
    monthly_fee = monthly_fee_operations.update(monthly_fee, form)
    return monthly_fee.to_dict()


@monthly_fee.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    monthly_fee = monthly_fee_operations.get_one_by_id(id)
    monthly_fee_operations.delete(monthly_fee)
    return {'message': 'The monthly fee was deleted.'}
