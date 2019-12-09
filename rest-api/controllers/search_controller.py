from flask_restful import Resource, reqparse

from ioc.container import Services


class SearchController(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('query', required=True, type=str, location='args')
        self.query_service = Services.query_service()

    def get(self):
        # TODO: extract magic strings
        args = self.parser.parse_args()
        query = args['query']
        labels = self.query_service.extract_labels(query)

        return {'hello': labels}
