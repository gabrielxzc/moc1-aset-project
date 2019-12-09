import dependency_injector.containers as containers
import dependency_injector.providers as providers

from repository.media_repository import MediaRepository
from service.query_service import QueryService


class Services(containers.DeclarativeContainer):
    """list of services"""

    query_service = providers.Factory(
        QueryService,
        repository=MediaRepository()
    )