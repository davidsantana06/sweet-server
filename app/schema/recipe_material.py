from flask_restx.fields import Integer, Nested
from typing import NotRequired, TypedDict

from app.extension import api

from .material import MaterialSchema, material
from .recipe import RecipeSchema, recipe


class RecipeMaterialSchema(TypedDict):
    id_recipe: int
    recipe: NotRequired[RecipeSchema]
    id_material: int
    material: NotRequired[MaterialSchema]
    quantity: int


recipe_material_schema = RecipeMaterialSchema(
    id_recipe=Integer(title='Recipe ID', required=True),
    recipe=Nested(
        recipe,
        title='Recipe',
        readonly=True
    ),
    id_material=Integer(title='Material ID', required=True),
    material=Nested(
        material,
        title='Material',
        readonly=True
    ),
    quantity=Integer(title='Quantity', required=True)
)

recipe_material = api.model('RecipeMaterial', recipe_material_schema)
