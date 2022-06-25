from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipsInfoCollectorInterface(ABC):
    '''Starships Collector Interface'''

    @abstractmethod
    def find_starship(self, starship_id: int, time: str) -> List[Dict]:
        '''Must Implement'''
        raise Exception('Must implement find_starship method')
