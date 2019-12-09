from flask_restful import Resource

from ioc.container import Services
from service.download_service import IDownloadService


class DownloadController(Resource):
    def __init__(self):
        self.download_service: IDownloadService = Services.download_service()

    def get(self, id: int):
        base64_string = self.download_service.get_base64_content(id)

        return {"base64": base64_string}
