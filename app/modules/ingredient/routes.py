from flask import request
from http import HTTPStatus
from flask_login import login_required

from app import operations as app_operations

from .import operations as ingredient_operations, ingredient
from .forms import CreateForm, UpdateForm


@ingredient.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    if app_operations.validate_form(form):
        ingredient = ingredient_operations.create(
            form.name.data, 
            form.brand.data, 
            form.supplier.data,
            form.value.data,
            form.weight.data,
            form.current_quantity.data, 
            form.minimum_quantity.data
        )
    return ingredient.to_dict(), HTTPStatus.CREATED


@ingredient.get('/all')
@login_required
def get_all():
    return [
        ingredient.to_dict() for ingredient
        in ingredient_operations.get_all()
    ]


@ingredient.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return [
        ingredient.to_dict() for ingredient
        in ingredient_operations.get_all_by_name(name)
    ]


@ingredient.get('/all-select-choices/<string:id_recipe>')
@login_required
def get_all_select_choices(id_recipe: int):
    related_ids = []
    return [
        {'id': id, 'name': name} for id, name
        in ingredient_operations.get_all_select_choices(related_ids)
    ]


@ingredient.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return ingredient_operations.get_one_by_id(id).to_dict()


@ingredient.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = UpdateForm(request.form)
    ingredient = ingredient_operations.get_one_by_id(id)
    if app_operations.validate_form(form):
        ingredient = ingredient_operations.update(ingredient, form)
    return ingredient.to_dict()


@ingredient.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    ingredient = ingredient_operations.get_one_by_id(id)
    ingredient_operations.delete(ingredient)
    return {'message': 'The ingredient was deleted.'}
