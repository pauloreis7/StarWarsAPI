from typing import Dict

from src.domain.usecases.starships_list_collector import StarshipsListCollectorInterface
from src.presenters.interface.controllers import ControllersInterface


class StarshipsListCollectorController(ControllersInterface):
    ''' Controller to List Starships '''

    def __init__(self, starships_list_collector: StarshipsListCollectorInterface) -> None:
        self.__use_case = starships_list_collector

    def handle(self, http_request: Dict) -> Dict:
        ''' Handler to list collector '''

        page = http_request['query_params']['page']

        starships_list = self.__use_case.list(page)

        response = {'status_code': 200, 'data': starships_list}

        return response
