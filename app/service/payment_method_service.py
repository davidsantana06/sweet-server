from typing import Dict, Literal, Union

from app.database import PaymentMethod, PaymentMethods
from app.exception import PaymentMethotNotFound


def create(data: Dict[str, object]) -> PaymentMethod:
    payment_method = PaymentMethod(**data)
    PaymentMethod.save(payment_method)
    return payment_method


def get_all() -> PaymentMethods:
    return PaymentMethod.find_all()


def get_one_by(
    field: Literal['id', 'name'],
    value: Union[int, str]
) -> PaymentMethod:
    function = getattr(PaymentMethod, f'find_first_by_{field}')
    payment_method = function(value)
    if not payment_method: raise PaymentMethotNotFound()
    return payment_method


def update(id: int, data: Dict[str, object]) -> PaymentMethod:
    payment_method = get_one_by('id', id)
    payment_method.update(**data)
    PaymentMethod.save(payment_method)
    return payment_method


def delete(id: int) -> None:
    payment_method = get_one_by('id', id)
    PaymentMethod.delete(payment_method)
