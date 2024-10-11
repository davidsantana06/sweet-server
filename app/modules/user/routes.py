from flask import request
from flask_login import login_required
from http import HTTPStatus

from app.modules.common.facades import response

from . import operations as user_operations, user
from .decorators import access_required
from .forms import UserForm


@user.post('/create')
@login_required
@access_required(is_super=True)
def create():
    form = UserForm(request.form)
    user = user_operations.create(*form.data)
    return response.as_model(user, HTTPStatus.CREATED)


@user.get('/all')
@login_required
@access_required(is_super=True)
def get_all():
    return response.as_models(user_operations.get_all())


@user.get('/all/<string:name>')
@login_required
@access_required(is_super=True)
def get_all_by_name(name: str):
    return response.as_models(
        user_operations.get_all_by_name(name)
    )


@user.get('/one/<int:id>')
@login_required
@access_required(is_super=True, is_self=True)
def get_one_by_id(id: int):
    return response.as_model(
        user_operations.get_one_by('id', id, except_super=False)
    )


@user.patch('/update/<int:id>')
@login_required
@access_required(is_super=True, is_self=True)
def update(id: int):
    form = UserForm(request.form)
    user = user_operations.get_one_by('id', id, except_super=False)
    user = user_operations.update(user, form)
    return response.as_model(user)


@user.delete('/delete/<int:id>')
@login_required
@access_required(is_super=True)
def delete(id: int):
    user = user_operations.get_one_by('id', id)
    user_operations.delete(user)
    return response.as_message('The user was deleted.')
