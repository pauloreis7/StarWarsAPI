from fastapi import APIRouter, Request as FastApiResquest

from src.validators.get_starships_in_pagination_validator import starships_in_pagination_validator

starship_routes = APIRouter()


@starship_routes.get('/api/starships/list')
def get_starships_in_pagination(request: FastApiResquest):
    '''get_starships_in_pagination route'''

    starships_in_pagination_validator(request)

    return {"msg": "Hello World"}
