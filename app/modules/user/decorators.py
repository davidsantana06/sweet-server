from functools import wraps
from types import FunctionType

from . import operations as user_operations


def access_required(is_super: bool = False, is_self: bool = False):
    def decorator(f: FunctionType):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            print('teste')
            user_operations.check_acess(
                is_super, is_self, kwargs.get('id')
            )
            return f(*args, **kwargs)
        return decorated_function
    return decorator
