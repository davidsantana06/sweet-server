from flask_restx.fields import Integer, Nested
from typing import NotRequired, TypedDict

from app.extension import api

from .ingredient import IngredientSchema, ingredient
from .recipe import RecipeSchema, recipe


class RecipeIngredientSchema(TypedDict):
    id_recipe: int
    recipe: NotRequired[RecipeSchema]
    id_ingredient: int
    ingredient: NotRequired[IngredientSchema]
    weight: int


recipe_ingredient_schema = RecipeIngredientSchema(
    id_recipe=Integer(title='Recipe ID', required=True),
    recipe=Nested(
        recipe,
        title='Recipe',
        readonly=True
    ),
    id_ingredient=Integer(title='Ingredient ID', required=True),
    ingredient=Nested(
        ingredient,
        title='Ingredient',
        readonly=True
    ),
    weight=Integer(
        title='Weight', 
        required=True,
        min=1,
        max=10_000
    )
)

recipe_ingredient = api.model('RecipeIngredient', recipe_ingredient_schema)
