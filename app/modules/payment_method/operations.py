from app.database import PaymentMethod
from app.typing import SelectChoices


def create(name: str) -> None:
    payment_method = PaymentMethod(name)
    PaymentMethod.save(payment_method)


def get_all_select_choices() -> SelectChoices:
    return PaymentMethod.find_all_select_choices()


def get_one_by_name(name: str) -> PaymentMethod:
    return PaymentMethod.find_first_by_name(name)
