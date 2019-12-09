import base64
from typing import Any

from repository.media_repository import IMediaRepository


class IDownloadService:
    def get_base64_content(self, id: int) -> str:
        pass


class DownloadService(IDownloadService):
    def __init__(self, media_repository, disk_repository):
        self.media_repository: IMediaRepository = media_repository
        self.disk_repository: Any = disk_repository

    def get_base64_content(self, id: int) -> str:
        """
        Get base64 encoded media file
        :param id: id of the metadata
        :return: base64 string
        """
        metadata = self.media_repository.get_by_id(id)
        file: bytes = self.disk_repository.get_file(metadata["path"])
        encoded_bytes = base64.b64encode(file)
        return str(encoded_bytes, "utf-8")
