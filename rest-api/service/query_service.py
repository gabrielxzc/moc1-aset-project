from typing import List

from repository.media_repository import IMediaRepository


class IQueryService:
    def get_metadata(self, query):
        pass


class QueryService(IQueryService):
    def __init__(self, media_repository):
        self.repository: IMediaRepository = media_repository

    @staticmethod
    def extract_labels(query: str) -> List[str]:
        """
        Extract labels from query
        :param query: comma separated string
        :return: list of labels
        """
        query = query or ""
        return query.split(",")

    def get_metadata(self, query):
        """
        Get metadata based on query
        :param query: comma separated string
        :return: dictionary with media metadata
        """
        labels = self.extract_labels(query)
        return self.repository.get_by_label(labels)
