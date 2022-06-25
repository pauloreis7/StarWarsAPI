from fastapi import APIRouter, Request as FastApiResquest
from fastapi.responses import JSONResponse

from src.validators.get_starships_in_pagination_validator import get_starships_in_pagination_validator
from src.validators.get_starship_info_validator import get_starship_info_validator
from src.presenters.errors.error_controller import handle_errors

from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starships_in_pagination_composer import get_starships_in_pagination_composer
from src.main.composers.get_starship_info_composer import get_starship_info_composer


starship_routes = APIRouter()


@starship_routes.get('/api/starships/list')
async def get_starships_in_pagination(request: FastApiResquest):
    '''get_starships_in_pagination route'''

    response = None
    get_starships_controller = get_starships_in_pagination_composer()

    try:
        get_starships_in_pagination_validator(request)

        response = await request_adapter(request, get_starships_controller.handle)
    except Exception as error:
        response = handle_errors(error)

    return JSONResponse(
        status_code=response['status_code'],
        content={'data': response['data']}
    )


@starship_routes.get('/api/starships/{starship_id}')
async def get_starship_info(request: FastApiResquest):
    '''get_starship_info route'''

    response = None
    get_starship_controller = get_starship_info_composer()

    try:
        get_starship_info_validator(request)

        response = await request_adapter(request, get_starship_controller.handle)
    except Exception as error:
        response = handle_errors(error)

    return JSONResponse(
        status_code=response['status_code'],
        content={'data': response['data']}
    )
