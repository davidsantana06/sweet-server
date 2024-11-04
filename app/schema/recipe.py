from flask_restx.fields import Float, Integer, Nested, String
from typing import NotRequired, TypedDict

from app.extension import api

from .category import CategorySchema, category


class RecipeSchema(TypedDict):
    id: NotRequired[int]
    id_category: int
    category: NotRequired[CategorySchema]
    name: str
    preparation_time: int
    preparation_time_in_hours: NotRequired[float]
    description: str
    ingredients_value: NotRequired[float]
    materials_value: NotRequired[float]


recipe_schema = RecipeSchema(
    id=Integer(title='ID', readonly=True),
    id_category=Integer(title='Category ID', required=True),
    category=Nested(
        category,
        title='Category',
        readonly=True
    ),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100
    ),
    preparation_time=Integer(
        title='Preparation time in minutes',
        required=True
    ),
    preparation_time_in_hours=Float(
        title='Preparation time in hours',
        readonly=True
    ),
    description=String(
        title='Description',
        required=True,
        max_length=1_000
    ),
    ingredients_value=Float(title='Ingredients value', readonly=True),
    materials_value=Float(title='Materials value', readonly=True)
)

recipe = api.model('Recipe', recipe_schema)
