from typing import Type, List, Dict

from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from src.domain.usecases.starships_info_collector import StarshipsInfoCollectorInterface
from src.errors import HttpUnprocessableEntityError


class StarshipsInfoCollector(StarshipsInfoCollectorInterface):
    '''StarshipsInfoCollector usecase'''

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def find_starship(self, starship_id: int, time: str) -> List[Dict]:
        '''
            Find starship information and return it
            :param  - starship_id: Starship id 
                    - time: Time in hours
            :returns - Dictionary with starship information
        '''

        api_response = self.__api_consumer.get_starship_info(starship_id)
        mglt = api_response.response['MGLT']

        if mglt == 'unknown':
            raise HttpUnprocessableEntityError('Unprocessible Information for selected starship')

        distance_traveled = self.__calculate_distance_traveled_to_spaceship(
            mglt, time
        )
        formatted_response = self.__format_response(
            api_response.response,
            distance_traveled
        )

        return formatted_response

    @classmethod
    def __calculate_distance_traveled_to_spaceship(cls, mglt: str, time: str) -> int:
        '''
            Calculate distance traveled
            :param  - mglt: string with Maximum number of Megalights for this spaceship
                    - time: Time in hours
            :returns - distance traveled in megalights
        '''

        distance_traveled = int(mglt) * int(time)

        return distance_traveled

    @classmethod
    def __format_response(cls, starship_info: Dict, distance_traveled: int) -> Dict:
        '''
            Format response from api
            :params - starship_info: spaceship informations
                    - distance_traveled: the distance traveled calculation
            :returns - formated spaceship informations
        '''

        return {
            "starship": starship_info["name"],
            "model": starship_info["model"],
            "manufacturer": starship_info["manufacturer"],
            "max_atmosphering_speed": starship_info["max_atmosphering_speed"],
            "MGLT": starship_info["MGLT"],
            "distance_traveled": str(distance_traveled) + " ML"
        }
