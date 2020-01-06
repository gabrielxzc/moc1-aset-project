import dependency_injector.containers as containers
import dependency_injector.providers as providers

from repository.disk_repository import DiskRepository
from repository.labels_repository import LabelRepository
from repository.uploaded_audio_file_repository import UploadedAudioFileRepository

from service.download_service import DownloadService
from service.query_service import QueryService


class Services(containers.DeclarativeContainer):
    """list of services"""

    query_service = providers.Factory(QueryService, label_repository=LabelRepository())

    download_service = providers.Factory(
        DownloadService,
        audio_file_repository=UploadedAudioFileRepository(),
        disk_repository=DiskRepository(),
    )
