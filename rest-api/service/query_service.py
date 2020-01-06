from typing import List

from orm.entities import Label


class IQueryService:
    def get_metadata(self, query):
        pass


class QueryService(IQueryService):
    def __init__(self, label_repository):
        self.repository = label_repository

    @staticmethod
    def extract_labels(query: str) -> List[str]:
        """
        Extract labels from query
        :param query: comma separated string
        :return: list of labels
        """
        query = query or ""
        return query.split(",")

    def get_metadata(self, query: str) -> dict:
        """
        Get metadata based on query
        :param query: comma separated string
        :return: dictionary with media metadata
        """
        labels = self.extract_labels(query)
        results = {"metadata": []}
        for label in labels:
            label: Label = self.repository.find_by_label_name(label)
            if label is None:
                continue
            for audio in label.audio_files:
                results["metadata"].append(
                    {
                        "id": audio.id,
                        "description": audio.description,
                        "labels": [l.label_name for l in audio.label_files],
                    }
                )

        return results
