from src.searchly.api.v1.services import response
from src.searchly.helper import log


def not_found(e):
    log.error(f'Endpoint not found: [{e}]')
    return response.make(error=True, message='Not found.', code=404)


def method_not_allowed(e):
    log.error(f'Method not allowed: [{e}]')
    return response.make(error=True, message='Method not allowed.', code=405)

