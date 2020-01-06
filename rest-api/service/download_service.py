import base64

from repository.disk_repository import IDiskRepository


class IDownloadService:
    def get_base64_content(self, id: int) -> str:
        pass


class DownloadService(IDownloadService):
    def __init__(self, audio_file_repository, disk_repository: IDiskRepository):
        self.audio_file_repository = audio_file_repository
        self.disk_repository = disk_repository

    def get_base64_content(self, id: int) -> str:
        """
        Get base64 encoded media file
        :param id: id of the metadata
        :return: base64 string
        """
        metadata = self.audio_file_repository.find_by_id(id)
        if metadata is None:
            raise ValueError("Invalid id")

        file: bytes = self.disk_repository.get_file(metadata.filepath)
        encoded_bytes = base64.b64encode(file)
        return str(encoded_bytes, "utf-8")
