from typing import List


class IMediaRepository:
    def get_by_label(self, labels: List[str]) -> dict:
        pass


class MediaRepository(IMediaRepository):
    def get_by_label(self, labels: List[str]) -> dict:
        """
        TODO: connect to database
        :param labels:
        :return:
        """
        return {"labels": labels}
