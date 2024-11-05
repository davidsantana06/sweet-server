from flask_restx.fields import Integer, String
from typing import NotRequired, TypedDict

from app.extension import api


class CategorySchema(TypedDict):
    id: NotRequired[int]
    name: str


category_schema = api.model('Category', CategorySchema(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100
    )
))
