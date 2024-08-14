from flask import request

from app.modules.category import operations as category_operations
from app.modules.labor import operations as labor_operations
from app.modules.payment_method import operations as payment_method_operations
from app.modules.user import operations as user_operations

from . import operations as setup_operations, setup
from .typing import SetupData


@setup.post('/run')
def run():
    def create_default_categories(setup_data: SetupData):
        for name in setup_data['category_names']:
            try:
                category_operations.get_one_by_name(name)
            except:
                category_operations.create(name)

    def create_default_labors(setup_data: SetupData):
        try:
            labor_operations.get_one_by_id(1, except_default=False)
        except:
            default_labor_data = setup_data['default_labor_data']
            person_name = default_labor_data['person_name']
            hourly_rate = default_labor_data['hourly_rate']
            labor_operations.create(person_name, hourly_rate)

    def create_default_payment_methods(setup_data: SetupData):
        for name in setup_data['payment_method_names']:
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
    form = request.form
    create_default_categories(setup_data)
    create_default_labors(setup_data)
    create_default_payment_methods(setup_data)
    create_default_user(
        form['name'],
        form['password']
    )
    return {'message': 'The setup was completed successfully.'}
