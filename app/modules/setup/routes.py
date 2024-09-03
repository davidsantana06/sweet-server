from flask import request

from app.modules.category import operations as category_operations
from app.modules.common.facades import response
from app.modules.labor import operations as labor_operations
from app.modules.payment_method import operations as payment_method_operations
from app.modules.user import operations as user_operations

from . import operations as setup_operations, setup
from .typing import (
    DefaultLaborData,
    CategoryNames, PaymentMethodNames
)


@setup.post('/run')
def run():
    def create_default_categories(names: CategoryNames):
        for name in names:
            try:
                category_operations.get_one_by_name(name)
            except:
                category_operations.create(name)

    def create_default_labor(data: DefaultLaborData):
        try:
            labor_operations.get_one_by_id(1, except_default=False)
        except:
            labor_operations.create(
                data['person_name'],
                data['hourly_rate']
            )

    def create_default_payment_methods(names: PaymentMethodNames):
        for name in names:
            try:
                payment_method_operations.get_one_by_name(name)
            except:
                payment_method_operations.create(name)

    def create_default_user(name: str, password: str):
        try:
            user_operations.get_one_by_id(1)
        except:
            if name and password:
                user_operations.create(name, password)

    setup_data = setup_operations.get_data()
    create_default_categories(setup_data['category_names'])
    create_default_labor(setup_data['default_labor_data'])
    create_default_payment_methods(setup_data['payment_method_names'])
    create_default_user(
        request.form.get('name'),
        request.form.get('password')
    )
    return response.as_message('The setup was completed successfully.')
