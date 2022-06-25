from abc import ABC, abstractmethod
from typing import Dict, Tuple, Type
from requests import Request


class SwapiApiConsumerInterface(ABC):
    '''Api Consumer Interface'''

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''Must implement'''

        raise Exception('Must implement get_staships method')

    @abstractmethod
    def get_starship_info(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
        '''Must implement'''

        raise Exception('Must implement get_starship_info method')
