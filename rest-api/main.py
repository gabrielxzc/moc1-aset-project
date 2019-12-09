from flask import Flask
from flask_restful import Api

from controllers.query_controller import QueryController

app = Flask(__name__)
api = Api(app)

api.add_resource(QueryController, '/')
if __name__ == '__main__':
    app.run(debug=True)
