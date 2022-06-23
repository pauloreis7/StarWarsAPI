from typing import Callable
from fastapi import Request as FastApiResquest


async def request_adapter(request: FastApiResquest, callback: Callable):
    '''FastApi Adapter'''

    request_body = None

    try:
        request_body = await request.json()
    except:
        pass

    http_request = {
        'query_params': request.query_params,
        'body': request_body
    }

    try:
        http_response = callback(http_request)

        return http_response
    except:
        print('An erro has occurred')
