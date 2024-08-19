from flask import request
from http import HTTPStatus
from flask_login import login_required

from app import operations as app_operations
from app.modules.category import operations as category_operations
from app.modules.ingredient import operations as ingredient_operations
from app.modules.material import operations as material_operations

from . import operations as recipe_operations, recipe
from .forms import (
    CreateForm, UpdateForm,
    CreateIngredientRelForm, UpdateIngredientRelForm,
    CreateMaterialRelForm, UpdateMaterialRelForm
)


@recipe.post('/create')
@login_required
def create():
    form = CreateForm(request.form)
    app_operations.validate_form(form)
    category_operations.get_one_by_id(form.id_category.data)
    recipe = recipe_operations.create(
        form.id_category.data,
        form.name.data,
        form.preparation_time.data,
        form.description.data
    )
    return recipe.to_dict(), HTTPStatus.CREATED


@recipe.post('/create-ingredient-rel/<int:id>')
def create_ingredient_rel(id: int):
    recipe_operations.get_one_by_id(id)
    form = CreateIngredientRelForm(request.form)
    app_operations.validate_form(form)
    ingredient_operations.get_one_by_id(form.id_ingredient.data)
    ingredient_rel = recipe_operations.create_ingredient_rel(
        id,
        form.id_ingredient.data,
        form.weight.data
    )
    return ingredient_rel.to_dict(), HTTPStatus.CREATED


@recipe.post('/create-material-rel/<int:id>')
def create_material_rel(id: int):
    recipe_operations.get_one_by_id(id)
    form = CreateMaterialRelForm(request.form)
    app_operations.validate_form(form)
    material_operations.get_one_by_id(form.id_material.data)
    material_rel = recipe_operations.create_material_rel(
        id,
        form.id_material.data,
        form.quantity.data
    )
    return material_rel.to_dict(), HTTPStatus.CREATED


@recipe.get('/all')
@login_required
def get_all():
    return [recipe.to_dict() for recipe in recipe_operations.get_all()]


@recipe.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return [
        recipe.to_dict() for recipe
        in recipe_operations.get_all_by_name(name)
    ]


@recipe.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return [
        {'id': id, 'name': name} for id, name
        in recipe_operations.get_all_select_choices()
    ]


@recipe.get('/all-ingredient-rels/<int:id>')
@login_required
def get_all_ingredient_rels(id: int):
    return [
        ingredient_rel.to_dict() for ingredient_rel
        in recipe_operations.get_all_ingredient_rels_by_id(id)
    ]


@recipe.get('/all-material-rels/<int:id>')
@login_required
def get_all_material_rels(id: int):
    return [
        material_rel.to_dict() for material_rel
        in recipe_operations.get_all_material_rels_by_id(id)
    ]


@recipe.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    recipe = recipe_operations.get_one_by_id(id)
    return {
        **recipe.to_dict(),
        **{'category': recipe.category.to_dict()},
        **{
            'ingredients': [
                ingredient_rel.ingredient.to_dict()
                for ingredient_rel in recipe.ingredient_rels
            ]
        },
        **{
            'materials': [
                material_rel.material.to_dict()
                for material_rel in recipe.material_rels
            ]
        }
    }


@recipe.patch('/update/<int:id>')
def update(id: int):
    recipe = recipe_operations.get_one_by_id(id)
    form = UpdateForm(request.form)
    app_operations.validate_form(form)
    recipe = recipe_operations.update(recipe, form)
    return recipe.to_dict()


@recipe.patch('/update-ingredient-rel/<int:id>/ingredient/<int:id_ingredient>')
def update_ingredient_rel(id: int, id_ingredient: int):
    ingredient_rel = recipe_operations.get_one_ingredient_rel_by_id_and_id_ingredient(
        id, id_ingredient
    )
    form = UpdateIngredientRelForm(request.form)
    app_operations.validate_form(form)
    ingredient_rel = recipe_operations.update_ingredient_rel(
        ingredient_rel, form
    )
    return ingredient_rel.to_dict()


@recipe.patch('/update-material-rel/<int:id>/material/<int:id_material>')
def update_material_rel(id: int, id_material: int):
    material_rel = recipe_operations.get_one_material_rel_by_id_and_id_material(
        id, id_material
    )
    form = UpdateMaterialRelForm(request.form)
    app_operations.validate_form(form)
    material_rel = recipe_operations.update_material_rel(
        material_rel, form
    )
    return material_rel.to_dict()


@recipe.delete('/delete/<int:id>')
def delete(id: int):
    recipe = recipe_operations.get_one_by_id(id)
    recipe_operations.delete(recipe)
    return {'message': 'The recipe was deleted.'}


@recipe.delete('/delete-ingredient-rel/<int:id>/ingredient/<int:id_ingredient>')
def delete_ingredient_rel(id: int, id_ingredient: int):
    ingredient_rel = recipe_operations.get_one_ingredient_rel_by_id_and_id_ingredient(
        id, id_ingredient
    )
    recipe_operations.delete_ingredient_rel(ingredient_rel)
    return {'message': 'The ingredient rel was deleted.'}


@recipe.delete('/delete-material-rel/<int:id>/material/<int:id_material>')
def delete_material_rel(id: int, id_material: int):
    material_rel = recipe_operations.get_one_material_rel_by_id_and_id_material(
        id, id_material
    )
    recipe_operations.delete_material_rel(material_rel)
    return {'message': 'The material rel was deleted.'}
