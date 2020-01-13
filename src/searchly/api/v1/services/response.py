def make(error, message=None, response=None):
    response_dict = dict(error=error)
    if error:
        assert type(message) is str
        response_dict['message'] = message
    else:
        assert type(response) is dict
        response_dict['response'] = response
    return response_dict, 200


def get(attribute_name, json_response, default=None):
    return default if not json_response or attribute_name not in json_response else json_response[attribute_name]
