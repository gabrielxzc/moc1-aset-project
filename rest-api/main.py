from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from controllers.download_controller import DownloadController
from controllers.search_controller import SearchController
from controllers.tagger_controller import TaggerController

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(SearchController, "/search")
api.add_resource(DownloadController, "/download/<int:id>")
api.add_resource(TaggerController, "/tag")

if __name__ == "__main__":
    app.run(debug=True)
