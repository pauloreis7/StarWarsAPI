from src.infra import SwapiApiConsumer
from .startships_list_colector import StarShipListColector


def test_list():
    api_consumer = SwapiApiConsumer()
    star_ship_list_colector = StarShipListColector(api_consumer)

    page = 1

    star_ship_list_colector.list(page)
