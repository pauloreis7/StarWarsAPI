from typing import Dict, Type

from src.domain.usecases.starships_info_collector import StarshipsInfoCollectorInterface
from src.presenters.interface.controllers import ControllersInterface


class StarshipsInfoCollectorController(ControllersInterface):
    ''' Controller to get starship info '''

    def __init__(self, starship_info_collector: Type[StarshipsInfoCollectorInterface]) -> None:
        self.__use_case = starship_info_collector

    def handle(self, http_request: Dict):
        ''' Handle to info colector controller '''

        starship_id = http_request['path_params']['starship_id']
        time = http_request['query_params']['time']

        starship_info = self.__use_case.find_starship(starship_id, time)

        response = {'status_code': 200, 'data': starship_info}

        return response
