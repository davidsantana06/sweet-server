from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response

from . import operations as category_operations, category
from .forms import CategoryForm


@category.post('/create')
@login_required
def create():
    form = CategoryForm(request.form)
    category = category_operations.create(*form.data)
    return response.as_model(category, HTTPStatus.CREATED)


@category.get('/all')
@login_required
def get_all():
    return response.as_models(category_operations.get_all())


@category.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return response.as_models(
        category_operations.get_all_by_name(name)
    )


@category.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return response.as_select_choices(
        category_operations.get_all_select_choices()
    )


@category.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return response.as_model(
        category_operations.get_one_by('id', id)
    )


@category.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = CategoryForm(request.form)
    category = category_operations.get_one_by('id', id)
    category = category_operations.update(category, form)
    return response.as_model(category)


@category.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    category = category_operations.get_one_by('id', id)
    category_operations.delete(category)
    return response.as_message('The customer was deleted.')
