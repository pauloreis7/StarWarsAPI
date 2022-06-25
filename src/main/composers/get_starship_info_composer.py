from src.presenters.controllers.starships_info_collector_controller import StarshipsInfoCollectorController
from src.data.usecases.starships_info_collector import StarshipsInfoCollector
from src.infra.swapi_api_consumer import SwapiApiConsumer


def get_starship_info_composer():
    '''Get starships info composer'''

    infra = SwapiApiConsumer()
    usecase = StarshipsInfoCollector(infra)
    controller = StarshipsInfoCollectorController(usecase)

    return controller
