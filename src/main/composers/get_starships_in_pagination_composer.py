from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.data.usecases.startships_list_colector import StarshipsListColector
from src.presenters.controllers.startships_list_colector_controller import StartshipsListColectorController


def get_starships_in_pagination_composer():
    '''get starships list composer'''

    infra = SwapiApiConsumer()
    use_case = StarshipsListColector(infra)
    controller = StartshipsListColectorController(use_case)

    return controller
