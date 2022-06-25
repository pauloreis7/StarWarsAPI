from typing import Callable
from fastapi import Request as FastApiResquest


async def request_adapter(request: FastApiResquest, callback: Callable):
    '''
        Adapter to httpRequest
        @param - request: Http request Object with all properties
                 callback: Calback to process http request
        @return - Http Response to Request
    '''

    request_body = None

    try:
        request_body = await request.json()
    except:
        pass

    http_request = {
        'query_params': request.query_params,
        'path_params': request.scope['path_params'],
        'body': request_body
    }

    http_response = callback(http_request)

    return http_response
