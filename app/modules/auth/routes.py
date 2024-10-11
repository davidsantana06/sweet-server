from flask import request
from http import HTTPStatus

from app.modules.common.facades import response
from app.modules.user import operations as user_operations

from . import operations as auth_operations, auth
from .forms import AuthForm


@auth.post('/login')
def login():
    if auth_operations.check_authentication():
        return response.as_message(
            'User is already logged in. No new login session can be created.',
            HTTPStatus.CONFLICT
        )
    form = AuthForm(request.form)
    user = user_operations.get_one_by(
        'nickname',
        form.nickname.data,
        except_super=False
    )
    expiration = auth_operations.login(user, form.password.data)
    return response.as_dict({
        'user': user.to_dict(),
        'expiration': expiration,
        'message': 'Authentication successful. User data have been stored in the session.'
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
