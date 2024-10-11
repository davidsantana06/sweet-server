from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response
from app.modules.recipe import operations as recipe_operations

from .import operations as material_operations, material
from .forms import MaterialForm


@material.post('/create')
@login_required
def create():
    form = MaterialForm(request.form)
    material = material_operations.create(*form.data)
    return response.as_model(material, HTTPStatus.CREATED)


@material.get('/all')
@login_required
def get_all():
    return response.as_models(material_operations.get_all())


@material.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return response.as_models(
        material_operations.get_all_by_name(name)
    )


@material.get('/all-select-choices/<int:id_recipe>')
@login_required
def get_all_select_choices(id_recipe: int):
    related_ids = recipe_operations.get_all_material_rel_related_ids_by_id(
        id_recipe
    )
    return response.as_select_choices(
        material_operations.get_all_select_choices(related_ids)
    )


@material.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return response.as_model(
        material_operations.get_one_by_id(id)
    )


@material.patch('/update/<int:id>')
@login_required
def update(id: int):
    form = MaterialForm(request.form)
    material = material_operations.get_one_by_id(id)
    material = material_operations.update(material, form)
    return response.as_model(material)


@material.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    material = material_operations.get_one_by_id(id)
    material_operations.delete(material)
    return response.as_message('The material was deleted.')
