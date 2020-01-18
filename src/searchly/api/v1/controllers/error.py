from src.searchly.api.v1.services import response
from src.searchly.helper import log


def not_found(e):
    """
    Controller for not found scenarios [404].
    :param e: Exception raised due to the not found error.
    :return: JSON response.
    """
    log.error(f'Endpoint not found: [{e}]')
    return response.make(error=True, message='Not found.', code=404)


def method_not_allowed(e):
    """
    Controller for method not allowed scenarios [405].
    :param e: Exception raised due to the method not allowed error.
    :return: JSON response.
    """
    log.error(f'Method not allowed: [{e}]')
    return response.make(error=True, message='Method not allowed.', code=405)

