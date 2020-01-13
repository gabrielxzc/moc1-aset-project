from flask_restful import Resource, request


class TaggerController(Resource):
    def post(self):
        print(request.data)

        tags = ['bark', 'chainsaw']

        return tags