from flask import request

from app.modules.category import operations as category_operations
from app.modules.collaborator import operations as collaborator_operations
from app.modules.common.facades import response
from app.modules.payment_method import operations as payment_method_operations
from app.modules.user import operations as user_operations
from app.modules.user.forms import UserForm

from . import operations as setup_operations, setup
from .typing import (
    DefaultCollaboratorData,
    CategoryNames, PaymentMethodNames
)


@setup.post('/run')
def run():
    def create_default_categories(names: CategoryNames):
        for name in names:
            try:
                category_operations.get_one_by('name', name)
            except:
                category_operations.create(name)

    def create_default_collaborator(data: DefaultCollaboratorData):
        try:
            collaborator_operations.get_one_by_id(1, except_default=False)
        except:
            collaborator_operations.create(
                data['name'],
                data['hourly_rate'],
                data['notes']
            )

    def create_default_payment_methods(names: PaymentMethodNames):
        for name in names:
            try:
                payment_method_operations.get_one_by('name', name)
            except:
                payment_method_operations.create(name)

    def create_super_user():
        try:
            user_operations.get_one_by('id', 1, except_super=False)
        except:
            form = UserForm(request.form)
            user_operations.create(*form.data)

    setup_data = setup_operations.get_data()
    create_default_categories(setup_data['category_names'])
    create_default_collaborator(setup_data['default_collaborator_data'])
    create_default_payment_methods(setup_data['payment_method_names'])
    create_super_user()
    return response.as_message('The setup was completed successfully.')
