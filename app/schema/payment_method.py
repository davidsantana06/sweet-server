from flask_restx.fields import Integer, String
from typing import NotRequired, TypedDict


class PaymentMethodSchema(TypedDict):
    id: NotRequired[int]
    name: str
    sales_quantity: NotRequired[int]


payment_method_schema = PaymentMethodSchema(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=50
    ),
    sales_quantity=Integer(title='Sales quantity', readonly=True)
)
