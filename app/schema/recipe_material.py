from flask_restx.fields import Integer, Nested
from typing import NotRequired, TypedDict

from app.extension import api

from .material import MaterialSchema, material_schema
from .recipe import RecipeSchema, recipe_schema


class RecipeMaterialSchema(TypedDict):
    id_recipe: int
    recipe: NotRequired[RecipeSchema]
    id_material: int
    material: NotRequired[MaterialSchema]
    quantity: int


recipe_material_schema = api.model('RecipeMaterial', RecipeMaterialSchema(
    id_recipe=Integer(title='Recipe ID', required=True),
    recipe=Nested(
        recipe_schema,
        title='Recipe',
        readonly=True
    ),
    id_material=Integer(title='Material ID', required=True),
    material=Nested(
        material_schema,
        title='Material',
        readonly=True
    ),
    quantity=Integer(
        title='Quantity',
        required=True,
        min=1,
        max=10_000
    )
))
