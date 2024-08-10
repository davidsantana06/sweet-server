from werkzeug.exceptions import NotFound

from app.database import PaymentMethod
from app.typing import SelectChoices


def create(name: str) -> None:
    payment_method = PaymentMethod(name)
    PaymentMethod.save(payment_method)


def get_all_select_choices() -> SelectChoices:
    return PaymentMethod.find_all_select_choices()


def get_one_by_name(name: str) -> PaymentMethod:
    payment_method = PaymentMethod.find_first_by_name(name)
    if not payment_method:
        raise NotFound('The payment method was not found.')
    return payment_method
