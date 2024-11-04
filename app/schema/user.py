from flask_restx.fields import Integer, String
from typing import NotRequired, TypedDict


class UserSchema(TypedDict):
    id: NotRequired[int]
    name: str


user_schema = UserSchema(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=50
    )
)
