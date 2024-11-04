from flask_restx.fields import Float, Integer, Nested, String
from typing import NotRequired, TypedDict

from app.extension import api

from .collaborator import CollaboratorSchema, collaborator
from .recipe import RecipeSchema, recipe


class ProductSchema(TypedDict):
    id: NotRequired[int]
    id_recipe: int
    recipe: NotRequired[RecipeSchema]
    id_collaborator: int
    collaborator: NotRequired[CollaboratorSchema]
    name: str
    loss_margin: float
    contribuition_margin: float
    monthly_fees_value: NotRequired[float]
    collaborator_value: NotRequired[float]
    cost_value: NotRequired[float]
    loss_value: NotRequired[float]
    contribuition_value: NotRequired[float]
    sell_value: NotRequired[float]


product_schema = ProductSchema(
    id=Integer(title='ID', readonly=True),
    id_recipe=Integer(title='Recipe ID', required=True),
    recipe=Nested(
        recipe,
        title='Recipe',
        readonly=True
    ),
    id_collaborator=Integer(title='Collaborator ID', required=True),
    collaborator=Nested(
        collaborator,
        title='Collaborator',
        readonly=True
    ),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100
    ),
    loss_margin=Float(
        title='Loss margin',
        description='0 (0%) to 1 (100%)',
        required=True,
        min=0,
        max=1
    ),
    contribuition_margin=Float(
        title='Contribuition margin',
        description='0 (0%) to 1 (100%)',
        required=True,
        min=0,
        max=1
    ),
    monthly_fees_value=Float(
        title='Monthly fees value',
        readonly=True
    ),
    collaborator_value=Float(
        title='Collaborator value',
        readonly=True
    ),
    cost_value=Float(
        title='Cost value',
        readonly=True
    ),
    loss_value=Float(
        title='Loss value',
        readonly=True
    ),
    contribuition_value=Float(
        title='Contribuition value',
        readonly=True
    ),
    sell_value=Float(
        title='Sell value',
        readonly=True
    )
)

product = api.model('Product', product_schema)
