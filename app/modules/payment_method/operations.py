from typing import Literal, Union
from werkzeug.exceptions import NotFound

from app.database import (
    PaymentMethod, PaymentMethods,
    SelectChoices
)

from .forms import PaymentMethodForm


def create(name: str) -> PaymentMethod:
    payment_method = PaymentMethod(name)
    PaymentMethod.save(payment_method)
    return payment_method


def get_all() -> PaymentMethods:
    return PaymentMethod.find_all()


def get_all_by_name(name: str) -> PaymentMethods:
    return PaymentMethod.find_all_by_name(name)


def get_all_select_choices() -> SelectChoices:
    return PaymentMethod.find_all_select_choices()


def get_one_by(
    field: Literal['id', 'name'],
    value: Union[int, str]
) -> PaymentMethod:
    function = {
        'id': PaymentMethod.find_first_by_id,
        'name': PaymentMethod.find_first_by_name
    }[field]
    payment_method = function(value)
    if not payment_method:
        raise NotFound('The payment method was not found.')
    return payment_method


def update(
    payment_method: PaymentMethod,
    form: PaymentMethodForm
) -> PaymentMethod:
    form.populate_obj(payment_method)
    PaymentMethod.save(payment_method)
    return payment_method


def delete(payment_method: PaymentMethod) -> None:
    PaymentMethod.delete(payment_method)
