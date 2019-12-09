from typing import List


class QueryService:
    def __init__(self):
        pass  # inject repo

    @staticmethod
    def extract_labels(query: str) -> List[str]:
        """
        Extract labels from query
        :param query: comma separated string
        :return: list of labels
        """
        query = query or ""
        return query.split(",")
