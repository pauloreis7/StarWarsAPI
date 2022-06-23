from fastapi import APIRouter, Request as FastApiResquest

starship_routes = APIRouter()


@starship_routes.get('/api/starships/list')
def get_starships_in_pagination(request: FastApiResquest):
    '''get_starships_in_pagination route'''

    return {"msg": "Hello World"}
