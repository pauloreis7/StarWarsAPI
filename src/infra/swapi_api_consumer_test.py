from .swapi_api_consumer import SwapiApiConsumer


def test_swapi_api_consumer():
    '''Testing get_starship method'''

    swapi_api_consumer = SwapiApiConsumer()

    response = swapi_api_consumer.get_starship(page=1)

    print(response)
