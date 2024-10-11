from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response

from .import operations as ingredient_operations, ingredient
from .forms import IngredientForm


@ingredient.post('/create')
@login_required
def create():
    form = IngredientForm(request.form)
    ingredient = ingredient_operations.create(*form.data)
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
    related_ids = []
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
    form = IngredientForm(request.form)
    ingredient = ingredient_operations.get_one_by_id(id)
    ingredient = ingredient_operations.update(ingredient, form)
    return response.as_model(ingredient)


@ingredient.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    ingredient = ingredient_operations.get_one_by_id(id)
    ingredient_operations.delete(ingredient)
    return response.as_message('The ingredient was deleted.')
