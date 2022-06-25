from cerberus import Validator

from src.errors import HttpUnprocessableEntityError


def get_starship_info_validator(request: any):
    '''starships info validator'''

    path_params = request.scope['path_params']

    query_param_validator = Validator({
        'time': {'type': 'string', 'required': True}
    })
    path_param_validator = Validator({
        'starship_id': {'type': 'string', 'required': True}
    })

    query_params_validation = query_param_validator.validate(
        request.query_params
    )
    path_params_validation = path_param_validator.validate(
        path_params
    )

    if query_params_validation is False:
        raise HttpUnprocessableEntityError(query_param_validator.errors)

    if path_params_validation is False:
        raise HttpUnprocessableEntityError(path_param_validator.errors)
