from fastapi import APIRouter, Request as FastApiResquest
from fastapi.responses import JSONResponse

from src.validators.get_starships_in_pagination_validator import starships_in_pagination_validator

from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starships_in_pagination_composer import get_starships_in_pagination_composer
from src.main.composers.get_starship_info_composer import get_starship_info_composer

starship_routes = APIRouter()


@starship_routes.get('/api/starships/list')
async def get_starships_in_pagination(request: FastApiResquest):
    '''get_starships_in_pagination route'''

    starships_in_pagination_validator(request)

    get_starships_controller = get_starships_in_pagination_composer()

    response = await request_adapter(request, get_starships_controller.handle)

    return JSONResponse(
        status_code=response['status_code'],
        content={'data': response['data']}
    )


@starship_routes.post('/api/starships/info')
async def get_starship_info(request: FastApiResquest):
    '''get_starship_info route'''

    get_starship_controller = get_starship_info_composer()

    response = await request_adapter(request, get_starship_controller.handle)

    return JSONResponse(
        status_code=response['status_code'],
        content={'data': response['data']}
    )
