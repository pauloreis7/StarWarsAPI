from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.data.usecases.starships_list_collector import StarshipsListCollector
from src.presenters.controllers.starships_list_collector_controller import StarshipsListCollectorController


def get_starships_in_pagination_composer():
    '''get starships list composer'''

    infra = SwapiApiConsumer()
    use_case = StarshipsListCollector(infra)
    controller = StarshipsListCollectorController(use_case)

    return controller
