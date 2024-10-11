from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.collaborator import operations as collaborator_operations
from app.modules.common.facades import response
from app.modules.recipe import operations as recipe_operations

from . import operations as product_operations, product
from .forms import ProductForm


@product.post('/create')
@login_required
def create():
    form = ProductForm(request.form)
    recipe_operations.get_one_by_id(form.id_recipe.data)
    collaborator_operations.get_one_by_id(form.id_collaborator.data)
    product = product_operations.create(*form.data)
    return response.as_model(product, HTTPStatus.CREATED)


@product.get('/all')
@login_required
def get_all():
    return response.as_models(product_operations.get_all())


@product.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return response.as_models(
        product_operations.get_all_by_name(name)
    )


@product.get('/all-select-choices/<int:id_sale>')
@login_required
def get_all_select_choices(id_sale: int):
    related_ids = []
    return response.as_select_choices(
        product_operations.get_all_select_choices(related_ids)
    )


@product.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    product = product_operations.get_one_by_id(id)
    return response.as_dict({
        **product.to_dict(),
        **{'recipe': product.recipe.to_dict()},
        **{'collaborator': product.collaborator.to_dict()}
    })


@product.patch('/update/<int:id>')
def update(id: int):
    form = ProductForm(request.form)
    recipe_operations.get_one_by_id(form.id_recipe.data)
    collaborator_operations.get_one_by_id(form.id_collaborator.data)
    product = product_operations.get_one_by_id(id)
    product = product_operations.update(product, form)
    return response.as_model(product)


@product.delete('/delete/<int:id>')
def delete(id: int):
    product = product_operations.get_one_by_id(id)
    product_operations.delete(product)
    return response.as_message('The product was deleted.')
