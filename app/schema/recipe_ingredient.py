from flask_restx.fields import Integer, Nested
from typing import NotRequired, TypedDict

from app.extension import api

from .ingredient import IngredientSchema, ingredient_schema
from .recipe import RecipeSchema, recipe_schema


class RecipeIngredientSchema(TypedDict):
    id_recipe: int
    recipe: NotRequired[RecipeSchema]
    id_ingredient: int
    ingredient: NotRequired[IngredientSchema]
    weight: int


recipe_ingredient_schema = api.model('RecipeIngredient', RecipeIngredientSchema(
    id_recipe=Integer(title='Recipe ID', required=True),
    recipe=Nested(
        recipe_schema,
        title='Recipe',
        readonly=True
    ),
    id_ingredient=Integer(title='Ingredient ID', required=True),
    ingredient=Nested(
        ingredient_schema,
        title='Ingredient',
        readonly=True
    ),
    weight=Integer(
        title='Weight',
        required=True,
        min=1,
        max=10_000
    )
))
