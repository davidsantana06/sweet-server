from app.modules.common.facades import response
from . import operations as error_operations, error


@error.app_errorhandler(Exception)
def handle_exception(e: Exception):
    description, status = error_operations.get_details(e)
    return response.as_message(description, status)
