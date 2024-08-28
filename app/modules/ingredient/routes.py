from flask import request
from http import HTTPStatus
from flask_login import login_required

from app import operations as app_operations
from app.facades import response
from app.modules.recipe import operations as recipe_operations

from .import operations as ingredient_operations, ingredient
from .forms import CreateForm, UpdateForm


@ingredient.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    app_operations.validate(form)
    ingredient = ingredient_operations.create(
        *app_operations.get_data(form)
    )
    return response.as_model(ingredient, HTTPStatus.CREATED)


@ingredient.get('/all')
@login_required
def get_all():
    return response.as_models(ingredient_operations.get_all())


@ingredient.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return response.as_models(
        ingredient_operations.get_all_by_name(name)
    )


@ingredient.get('/all-select-choices/<int:id_recipe>')
@login_required
def get_all_select_choices(id_recipe: int):
    related_ids = recipe_operations.get_all_ingredient_rel_related_ids_by_id(
        id_recipe
    )
    return response.as_select_choices(
        ingredient_operations.get_all_select_choices(related_ids)
    )


@ingredient.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return response.as_model(
        ingredient_operations.get_one_by_id(id)
    )


@ingredient.patch('/update/<int:id>')
@login_required
def update(id: int):
    ingredient = ingredient_operations.get_one_by_id(id)
    form = UpdateForm(request.form)
    app_operations.validate(form)
    ingredient = ingredient_operations.update(ingredient, form)
    return response.as_model(ingredient)


@ingredient.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    ingredient = ingredient_operations.get_one_by_id(id)
    ingredient_operations.delete(ingredient)
    return response.as_message('The ingredient was deleted.')
