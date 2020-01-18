def make(error, message=None, response=None, code=200):
    """
    API response generator function.
    :param error: True if the response has to be flagged as an error, False otherwise.
    :param message: Error message string formatted. Only being used when [error == True]
    :param response: JSON response dictionary formatted. Only being used when [error == False]
    :param code: Response code.
    :return: JSON response.
    """
    response_dict = dict(error=error)
    if error:
        assert type(message) is str
        response_dict['message'] = message
    else:
        assert type(response) is dict
        response_dict['response'] = response
    return response_dict, code


def get(attribute_name, json_response, default=None):
    return default if not json_response or attribute_name not in json_response else json_response[attribute_name]
