from flask import request
from http import HTTPStatus

from app import operations as app_operations
from app.facades import response
from app.modules.user import operations as user_operations

from . import operations as auth_operations, auth
from .forms import LoginForm


@auth.post('/login')
def login():
    if auth_operations.check_authentication():
        return response.as_message(
            'User is already logged in. No new login session can be created.',
            HTTPStatus.CONFLICT
        )
    form = LoginForm(request.form)
    app_operations.validate(form)
    user = user_operations.get_one_by_id(1)
    auth_operations.check_credentials(
        user, *app_operations.get_data(form)
    )
    auth_operations.login(user)
    return response.as_dict({
        'user': user.to_dict(),
        'message':
            'Authentication successful. ' +
            'User credentials have been stored in the session.'
    })


@auth.delete('/logout')
def logout():
    if not auth_operations.check_authentication():
        return response.as_message(
            'User is not logged in. No credentials were removed from the session.'
        )
    auth_operations.logout()
    return response.as_message(
        'User credentials have been successfully removed from the session.'
    )
