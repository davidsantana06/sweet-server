from flask import request
from http import HTTPStatus
from flask_login import login_required

from app import operations as app_operations
from app.modules.labor import operations as labor_operations
from app.modules.recipe import operations as recipe_operations

from . import operations as product_operations, product
from .forms import CreateForm, UpdateForm


@product.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    app_operations.validate_form(form)
    recipe_operations.get_one_by_id(form.id_recipe.data)
    labor_operations.get_one_by_id(form.id_labor.data)
    product = product_operations.create(
        form.id_recipe.data,
        form.id_labor.data,
        form.name.data,
        form.loss_margin.data,
        form.contribuition_margin.data
    )
    return product.to_dict(), HTTPStatus.CREATED


@product.get('/all')
@login_required
def get_all():
    return [
        product.to_dict() for product
        in product_operations.get_all()
    ]


@product.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return [
        product.to_dict() for product
        in product_operations.get_all_by_name(name)
    ]


@product.get('/all-select-choices/<int:sale_id>')
@login_required
def get_all_select_choices(sale_id: int):
    related_ids = []
    return [
        {'id': id, 'name': name} for id, name
        in product_operations.get_all_select_choices(related_ids)
    ]


@product.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    product = product_operations.get_one_by_id(id)
    return {
        **product.to_dict(),
        **{'recipe': product.recipe.to_dict()},
        **{'labor': product.labor.to_dict()}
    }


@product.patch('/update/<int:id>')
def update(id: int):
    form = UpdateForm(request.form)
    product = product_operations.get_one_by_id(id)
    app_operations.validate_form(form)
    recipe_operations.get_one_by_id(form.id_recipe.data)
    labor_operations.get_one_by_id(form.id_labor.data)
    product = product_operations.update(product, form)
    return product.to_dict()


@product.delete('/delete/<int:id>')
def delete(id: int):
    product = product_operations.get_one_by_id(id)
    product_operations.delete(product)
    return {'message': 'The product was deleted.'}
