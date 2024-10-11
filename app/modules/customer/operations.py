from werkzeug.exceptions import NotFound
from app.database import (
    Customer, Customers,
    SelectChoices
)
from .forms import CustomerForm


def create(name: str, phone: str, instagram: str, notes: str) -> Customer:
    customer = Customer(name, phone, instagram, notes)
    Customer.save(customer)
    return customer


def get_all() -> Customers:
    return Customer.find_all()


def get_all_by_name(name: str) -> Customers:
    return Customer.find_all_by_name(name)


def get_all_select_choices() -> SelectChoices:
    return Customer.find_all_select_choices()


def get_one_by_id(id: int) -> Customer:
    customer = Customer.find_first_by_id(id)
    if not customer:
        raise NotFound('The customer was not found.')
    return customer


def update(customer: Customer, form: CustomerForm) -> Customer:
    form.populate_obj(customer)
    Customer.save(customer)
    return customer


def delete(customer: Customer) -> None:
    Customer.delete(customer)
