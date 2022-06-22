from typing import Type
from collections import namedtuple
import requests
from requests import Request


class SwapiApiConsumer:

    def __init__(self) -> None:
        self. get_starship_response = namedtuple(
            'GET_Starships', 'status_code request response')

    def get_starship(self, page: int) -> any:

        req = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships/',
            params={'page': page}
        )
        prepared_req = req.prepare()

        response = self.__send_http_request(prepared_req)

        return self.get_starship_response(
            status_code=response.status_code,
            request=req,
            response=response.json()
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
