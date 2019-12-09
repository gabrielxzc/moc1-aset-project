import dependency_injector.containers as containers
import dependency_injector.providers as providers

from repository.disk_repository import DiskRepository
from repository.media_repository import MediaRepository
from service.download_service import DownloadService
from service.query_service import QueryService


class Services(containers.DeclarativeContainer):
    """list of services"""

    query_service = providers.Factory(
        QueryService,
        media_repository=MediaRepository()
    )

    download_service = providers.Factory(
        DownloadService,
        media_repository=MediaRepository(),
        disk_repository=DiskRepository()
    )
