from .swapi_api_consumer import SwapiApiConsumer


def test_swapi_api(requests_mock):
    '''Testing get_starship method'''

    requests_mock.get('https://swapi.dev/api/starships/',
                      status_code=200, json={'pilot': 'me'})

    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_starship(page=1)

    print(response)
