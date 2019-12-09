from flask_restful import Resource


class QueryController(Resource):
    def get(self):
        return {'hello': 'world'}
