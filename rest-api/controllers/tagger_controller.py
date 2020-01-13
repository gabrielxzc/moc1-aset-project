from flask_restful import Resource, reqparse

from ioc.container import Services
from service.query_service import IQueryService


class TaggerController(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("file_str", required=True, type=str, location="args")

    def get(self):
        # TODO: extract magic strings
        args = self.parser.parse_args()
        query = args["file_str"]

        metadata = ['bark', 'chainsaw']

        return metadata
