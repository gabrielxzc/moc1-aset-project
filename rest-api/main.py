from flask import Flask
from flask_restful import Api

from controllers.search_controller import SearchController

app = Flask(__name__)
api = Api(app)

api.add_resource(SearchController, '/search')
if __name__ == '__main__':
    app.run(debug=True)
