from flask import request
from http import HTTPStatus
from flask_login import login_required

from app import operations as app_operations
from app.modules.recipe import operations as recipe_operations

from .import operations as material_operations, material
from .forms import CreateForm, UpdateForm


@material.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    app_operations.validate_form(form)
    material = material_operations.create(
        form.name.data, 
        form.brand.data, 
        form.supplier.data,
        form.value.data,
        form.current_quantity.data, 
        form.minimum_quantity.data
    )
    return material.to_dict(), HTTPStatus.CREATED


@material.get('/all')
@login_required
def get_all():
    return [
        material.to_dict() for material 
        in material_operations.get_all()
    ]


@material.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return [
        material.to_dict() for material 
        in material_operations.get_all_by_name(name)
    ]


@material.get('/all-select-choices/<int:id_recipe>')
@login_required
def get_all_select_choices(id_recipe: int):
    related_ids = recipe_operations.get_all_material_rel_related_ids_by_id(
        id_recipe
    )
    return [
        {'id': id, 'name': name} for id, name
        in material_operations.get_all_select_choices(related_ids)
    ]


@material.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    return material_operations.get_one_by_id(id).to_dict()


@material.patch('/update/<int:id>')
@login_required
def update(id: int):
    material = material_operations.get_one_by_id(id)
    form = UpdateForm(request.form)
    app_operations.validate_form(form)
    material = material_operations.update(material, form)
    return material.to_dict()


@material.delete('/delete/<int:id>')
@login_required
def delete(id: int):
    material = material_operations.get_one_by_id(id)
    material_operations.delete(material)
    return {'message': 'The material was deleted.'}
