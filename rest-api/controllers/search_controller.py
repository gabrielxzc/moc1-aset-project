from flask_restful import Resource, reqparse

from ioc.container import Services
from service.query_service import IQueryService


class SearchController(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("query", required=True, type=str, location="args")
        self.query_service: IQueryService = Services.query_service()

    def get(self):
        # TODO: extract magic strings
        args = self.parser.parse_args()
        query = args["query"]

        metadata = self.query_service.get_metadata(query)

        return metadata
