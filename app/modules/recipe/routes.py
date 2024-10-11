from flask import request
from http import HTTPStatus
from flask_login import login_required

from app.modules.common.facades import response
from app.modules.category import operations as category_operations
from app.modules.resource.modules.ingredient import operations as ingredient_operations
from app.modules.resource.modules.material import operations as material_operations

from . import operations as recipe_operations, recipe
from .forms import IngredientRelForm, MaterialRelForm, RecipeForm


@recipe.post('/create')
@login_required
def create():
    form = RecipeForm(request.form)
    category_operations.get_one_by('id', form.id_category.data)
    recipe = recipe_operations.create(*form.data)
    return response.as_model(recipe, HTTPStatus.CREATED)


@recipe.post('/create-ingredient-rel/<int:id>')
def create_ingredient_rel(id: int):
    form = IngredientRelForm(request.form)
    recipe_operations.get_one_by_id(id)
    ingredient_operations.get_one_by_id(form.id_ingredient.data)
    ingredient_rel = recipe_operations.create_ingredient_rel(
        id,
        *form.data
    )
    return response.as_model(ingredient_rel, HTTPStatus.CREATED)


@recipe.post('/create-material-rel/<int:id>')
def create_material_rel(id: int):
    form = MaterialRelForm(request.form)
    recipe_operations.get_one_by_id(id)
    material_operations.get_one_by_id(form.id_material.data)
    material_rel = recipe_operations.create_material_rel(
        id,
        *form.data
    )
    return response.as_model(material_rel, HTTPStatus.CREATED)


@recipe.get('/all')
@login_required
def get_all():
    return response.as_models(recipe_operations.get_all())


@recipe.get('/all/<string:name>')
@login_required
def get_all_by_name(name: str):
    return response.as_models(
        recipe_operations.get_all_by_name(name)
    )


@recipe.get('/all-select-choices')
@login_required
def get_all_select_choices():
    return response.as_select_choices(
        recipe_operations.get_all_select_choices()
    )


@recipe.get('/all-ingredient-rels/<int:id>')
@login_required
def get_all_ingredient_rels(id: int):
    return response.as_models(
        recipe_operations.get_all_ingredient_rels_by_id(id)
    )


@recipe.get('/all-material-rels/<int:id>')
@login_required
def get_all_material_rels(id: int):
    return response.as_models(
        recipe_operations.get_all_material_rels_by_id(id)
    )


@recipe.get('/one/<int:id>')
@login_required
def get_one_by_id(id: int):
    recipe = recipe_operations.get_one_by_id(id)
    return response.as_dict({
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
    })


@recipe.patch('/update/<int:id>')
def update(id: int):
    form = RecipeForm(request.form)
    category_operations.get_one_by('id', form.id_category.data)
    recipe = recipe_operations.get_one_by_id(id)
    recipe = recipe_operations.update(recipe, form)
    return response.as_model(recipe)


@recipe.patch('/update-ingredient-rel/<int:id>/ingredient/<int:id_ingredient>')
def update_ingredient_rel(id: int, id_ingredient: int):
    form = IngredientRelForm(request.form)
    ingredient_rel = recipe_operations.get_one_ingredient_rel_by_id_and_id_ingredient(
        id,
        id_ingredient
    )
    ingredient_rel = recipe_operations.update_ingredient_rel(
        ingredient_rel, form
    )
    return response.as_model(ingredient_rel)


@recipe.patch('/update-material-rel/<int:id>/material/<int:id_material>')
def update_material_rel(id: int, id_material: int):
    form = MaterialRelForm(request.form)
    material_rel = recipe_operations.get_one_material_rel_by_id_and_id_material(
        id,
        id_material
    )
    material_rel = recipe_operations.update_material_rel(
        material_rel, form
    )
    return response.as_model(material_rel)


@recipe.delete('/delete/<int:id>')
def delete(id: int):
    recipe = recipe_operations.get_one_by_id(id)
    recipe_operations.delete(recipe)
    return response.as_message('The recipe was deleted.')


@recipe.delete('/delete-ingredient-rel/<int:id>/ingredient/<int:id_ingredient>')
def delete_ingredient_rel(id: int, id_ingredient: int):
    ingredient_rel = recipe_operations.get_one_ingredient_rel_by_id_and_id_ingredient(
        id,
        id_ingredient
    )
    recipe_operations.delete_ingredient_rel(ingredient_rel)
    return response.as_message('The ingredient rel was deleted.')


@recipe.delete('/delete-material-rel/<int:id>/material/<int:id_material>')
def delete_material_rel(id: int, id_material: int):
    material_rel = recipe_operations.get_one_material_rel_by_id_and_id_material(
        id,
        id_material
    )
    recipe_operations.delete_material_rel(material_rel)
    return response.as_message('The material rel was deleted.')
