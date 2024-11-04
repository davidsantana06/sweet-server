from app.database import Customer, Customers
from app.exception import CustomerNotFound
from app.schema import CustomerSchema


def create(data: CustomerSchema) -> Customer:
    customer = Customer(**data)
    Customer.save(customer)
    return customer


def get_all() -> Customers:
    return Customer.find_all()


def get_all_by_name(name: str) -> Customers:
    return Customer.find_all_by_name(name)


def get_one_by_id(id: int) -> Customer:
    customer = Customer.find_first_by_id(id)
    if not customer: raise CustomerNotFound()
    return customer


def update(id: int, data: CustomerSchema) -> Customer:
    customer = get_one_by_id(id)
    customer.update(**data)
    Customer.save(customer)
    return customer


def delete(id: int) -> None:
    customer = get_one_by_id(id)
    Customer.delete(customer)
