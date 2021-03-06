from typing import Dict, Tuple, Type
from collections import namedtuple
import requests
from requests import Request

from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from src.errors import HttpRequestError


class SwapiApiConsumer(SwapiApiConsumerInterface):
    '''Class to consume swapi api'''

    def __init__(self) -> None:
        self. get_starships_response = namedtuple(
            'get_starships', 'status_code request response'
        )
        self.get_starship_info_response = namedtuple(
            'get_starship_info', 'status_code request response'
        )

    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''
            request starship in pagination
            :param - page: navigation page int
            :return - Tuple with status_code, request and response
        '''

        req = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships/',
            params={'page': page}
        )
        prepared_req = req.prepare()

        response = self.__send_http_request(prepared_req)
        status_code = response.status_code

        if ((status_code >= 200) and (status_code <= 299)):
            return self.get_starships_response(
                status_code=status_code,
                request=req,
                response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()['detail'], status_code=status_code
            )

    def get_starship_info(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
        '''
            request starship infos
            :param - starship_id: starship id to request infos
            :return - Tuple with status_code, request and response
        '''

        req = requests.Request(
            method='GET',
            url=f'https://swapi.dev/api/starships/{starship_id}/',
        )

        prepared_req = req.prepare()

        response = self.__send_http_request(prepared_req)
        status_code = response.status_code

        if((status_code >= 200) and (status_code <= 299)):
            return self.get_starship_info_response(
                status_code=status_code,
                request=req,
                response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()['detail'], status_code=status_code
            )

    @classmethod
    def __send_http_request(cls, prepared_req: Type[Request]) -> any:
        '''
          Prepare a session and send http request
          :param - prepared_req: request object with all params
          :reponse - http response raw
        '''

        http_session = requests.Session()
        response = http_session.send(prepared_req)

        return response
