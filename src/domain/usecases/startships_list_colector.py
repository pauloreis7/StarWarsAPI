from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipsListColectorInterface(ABC):
    '''Startships Collector Interface'''

    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        '''Must Implement'''
        raise Exception('Must implement list method')
