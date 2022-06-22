from .swapi_api_consumer import SwapiApiConsumer


def test_swapi_api():
    '''Testing get_starship method'''

    swapi_api_consumer = SwapiApiConsumer()

    req_url = 'https://swapi.dev/api/starships/'
    page = 1

    # requests_mock.get(req_url,
    #                   status_code=200, json={'pilot': 'me'})

    get_starship_response = swapi_api_consumer.get_starship(page=page)

    assert get_starship_response.request.method == 'GET'
    assert get_starship_response.request.url == req_url
    assert get_starship_response.request.params == {'page': page}

    assert get_starship_response.status_code == 200
    assert isinstance(get_starship_response.response['results'], list)
