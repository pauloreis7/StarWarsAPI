from src.errors import HttpRequestError
from .swapi_api_consumer import SwapiApiConsumer


def test_get_starships(requests_mock):
    '''Testing get_starships method'''

    swapi_api_consumer = SwapiApiConsumer()

    req_url = 'https://swapi.dev/api/starships/'
    page = 1

    requests_mock.get(
        req_url,
        status_code=200,
        json={'results': [{}]}
    )

    get_starships_response = swapi_api_consumer.get_starships(page=page)

    assert get_starships_response.request.method == 'GET'
    assert get_starships_response.request.url == req_url
    assert get_starships_response.request.params == {'page': page}

    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response['results'], list)


def test_get_starships_http_error(requests_mock):
    '''Testing error in get_starships method'''

    swapi_api_consumer = SwapiApiConsumer()

    req_url = 'https://swapi.dev/api/starships/'
    page = 100

    requests_mock.get(
        req_url,
        status_code=404,
        json={'detail': 'error while getting data!'}
    )

    try:
        swapi_api_consumer.get_starships(page=page)

        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None


def test_get_starship_info(requests_mock):
    '''Testing test_get_starship_info method'''

    swapi_api_consumer = SwapiApiConsumer()

    starship_id = 9
    req_url = f'https://swapi.dev/api/starships/{starship_id}/'

    requests_mock.get(
        req_url,
        status_code=200,
        json={'name': 'some', 'model': 'modelA', 'MGLT': '123'}
    )

    get_starship_info_response = swapi_api_consumer.get_starship_info(
        starship_id=starship_id
    )

    assert get_starship_info_response.request.method == 'GET'
    assert get_starship_info_response.request.url == req_url

    assert get_starship_info_response.status_code == 200
    assert isinstance(get_starship_info_response.response, dict)
    assert 'MGLT' in get_starship_info_response.response


def test_get_starship_info_error(requests_mock):
    '''Testing error in test_get_starship_info method'''

    swapi_api_consumer = SwapiApiConsumer()

    starship_id = 1
    req_url = f'https://swapi.dev/api/starships/{starship_id}/'

    requests_mock.get(
        req_url,
        status_code=404,
        json={'detail': 'error while getting data!'}
    )

    try:
        swapi_api_consumer.get_starship_info(starship_id)

        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
