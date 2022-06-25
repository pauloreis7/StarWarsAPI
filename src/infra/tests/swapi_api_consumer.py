from collections import namedtuple
from faker import Faker

fake = Faker()


def mock_starships():
    '''
        mock data for starships
        :return - dict with starships information
    '''

    return {
        "name": fake.name(),
        "model": fake.name(),
        "manufacturer": fake.name(),
        "cost_in_credits": fake.random_int(),
        "length": fake.random_int(),
        "max_atmosphering_speed": fake.random_int(),
        "hyperdrive_rating": fake.random_int(),
        "MGLT": fake.random_int(),
        "url": f"https://swapi.dev/api/starships/{fake.random_int()}/"
    }


class SwapiApiConsumerSpy:
    '''Spy to SwapiApiConsumer'''

    def __init__(self) -> None:
        self.get_starships_attributes = {}
        self.get_starship_info_attributes = {}
        self.get_starships_response = namedtuple(
            'get_starships', 'status_code request response'
        )
        self.get_starship_info_response = namedtuple(
            'get_starship_info', 'status_code request response'
        )

    def get_starships(self, page: int) -> any:
        '''mock to get_starships'''

        self.get_starships_attributes['page'] = page

        return self.get_starships_response(
            status_code=200,
            request=None,
            response={"results": [mock_starships(), mock_starships()]}
        )

    def get_starship_info(self, starship_id: int) -> any:
        '''mock to get_starship_info'''

        self.get_starship_info_attributes['starship_id'] = starship_id

        return self.get_starship_info_response(
            status_code=200,
            request=None,
            response=mock_starships()
        )
