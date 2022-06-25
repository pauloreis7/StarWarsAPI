from src.infra.tests.swapi_api_consumer import SwapiApiConsumerSpy
from src.data.usecases.starships_info_collector import StarshipsInfoCollector


def test_find_starship():
    '''Testing find_starship method'''

    api_consumer = SwapiApiConsumerSpy()
    starship_info_collector = StarshipsInfoCollector(api_consumer)

    starship_id = 9
    time = 4

    response = starship_info_collector.find_starship(starship_id, time)

    assert api_consumer.get_starship_info_attributes['starship_id'] == starship_id
    assert isinstance(response, dict)
    assert 'MGLT' in response
    assert 'distance_traveled' in response
