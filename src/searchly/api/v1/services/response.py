from flask import jsonify

from src.searchly.helper import cache


def make(error=None, message=None, response=None, code=200, cached=False, method=None, key=None):
    """
    API response generator function.
    :param error: True if the response has to be flagged as an error, False otherwise.
    :param message: Error message string formatted. Only being used when [error == True]
    :param response: JSON response dictionary formatted. Only being used when [error == False]
    :param code: Response code.
    :param cached: True if the response is from the cache, False otherwise.
    :param method: Cache method.
    :param key: Cache key.
    :return: JSON response.
    """
    if cached:
        assert type(response) is dict
        response_dict = jsonify(response)
        response_dict.headers['X-Cache'] = 'HIT'
    else:
        assert error is not None
        response_dict = dict(error=error)
        if error:
            assert type(message) is str
            response_dict['message'] = message
        else:
            assert type(response) is dict
            response_dict['response'] = response
        if method is not None and key is not None:
            cache.refresh(method, key, response_dict)
        response_dict = jsonify(response_dict)
        response_dict.headers['X-Cache'] = 'MISS'
    return response_dict, code


def get(attribute_name, json_response, default=None):
    """
    Get an attribute from a dictionary given its key name.
    :param attribute_name: Attribute name.
    :param json_response: Dictionary where the attribute should be.
    :param default: Value that has to be returned if the attribute is not there.
    :return: Attribute value.
    """
    return default if not json_response or attribute_name not in json_response else json_response[attribute_name]
