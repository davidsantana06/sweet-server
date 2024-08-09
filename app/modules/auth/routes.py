from flask import request
from http import HTTPStatus

from app import operations as app_operations
from app.modules.user import operations as user_operations

from . import operations as auth_operations, auth
from .forms import LoginForm


@auth.post('/login')
def login():
    response = {
        'message': 'User is already logged in. No new login session can be created.',
    }, HTTPStatus.CONFLICT
    if not auth_operations.check_authentication():
        form = LoginForm(request.form)
        if app_operations.validate_form(form):
            user = user_operations.get_one_by_id(1)
            if auth_operations.check_credentials(user, form.password.data):
                auth_operations.login(user)
                response = {
                    'user': user.to_dict(),
                    'message': \
                        'Authentication successful. ' + \
                        'User credentials have been stored in the session.'
                }, HTTPStatus.OK
    return response


@auth.delete('/logout')
def logout():
    message = 'User is not logged in. No credentials were removed from the session.'
    if auth_operations.check_authentication():
        auth_operations.logout()
        message = 'User credentials have been successfully removed from the session.'
    return {'message': message}
