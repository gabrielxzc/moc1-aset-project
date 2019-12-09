from typing import List


class IMediaRepository:
    def get_by_label(self, labels: List[str]) -> dict:
        pass

    def get_by_id(self, id: int) -> dict:
        pass


class MediaRepository(IMediaRepository):
    def get_by_label(self, labels: List[str]) -> dict:
        """
        TODO: connect to database
        :param labels:
        :return:
        """
        return {"metadata": [
            {
                "id": 1,
                "name": "bird sounds",
                "description": "",
                "labels": ["bird"]
            }
        ]}

    def get_by_id(self, id: int) -> dict:
        return {
            "id": id,
            "name": "bird sounds",
            "description": "",
            "path": "",
            "labels": ["bird"]
        }
