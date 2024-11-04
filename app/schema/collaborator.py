from flask_restx.fields import Float, Integer, String
from typing import NotRequired, TypedDict

from app.extension import api


class CollaboratorSchema(TypedDict):
    id: NotRequired[int]
    name: str
    hourly_rate: float
    notes: str


collaborator_schema = CollaboratorSchema(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=100
    ),
    hourly_rate=Float(
        title='Hourly rate',
        required=True,
        min=0,
        max=10_000
    ),
    notes=String(
        title='Notes',
        required=True,
        max_length=1_000
    )
)

collaborator = api.model('Collaborator', collaborator_schema)
