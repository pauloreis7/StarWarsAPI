from typing import Dict
from src.domain.usecases.startships_list_colector import StarshipsListColectorInterface


class StartshipsListColectorController:
    ''' Controller to List Starships '''

    def __init__(self, starships_list_colector: StarshipsListColectorInterface) -> None:
        self.__use_case = starships_list_colector

    def handle(self, http_request: Dict) -> Dict:
        ''' Handler to list colector '''

        page = http_request['query_params']['page']

        startships_list = self.__use_case.list(page)

        response = {'status_code': 200, 'data': startships_list}

        return response
