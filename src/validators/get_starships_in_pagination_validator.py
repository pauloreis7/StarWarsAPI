from cerberus import Validator


def starships_in_pagination_validator(request: any):
    '''starships pagination validator'''

    query_param_validator = Validator({
        'page': {'type': 'string', 'allowed': ['1', '2', '3', '4'], 'required': True}
    })

    response = query_param_validator.validate(request.query_params)

    if response is False:
        raise Exception(query_param_validator.errors)
