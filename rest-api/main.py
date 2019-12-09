from flask import Flask
from flask_restful import Api

from controllers.download_controller import DownloadController
from controllers.search_controller import SearchController

app = Flask(__name__)
api = Api(app)

api.add_resource(SearchController, "/search")
api.add_resource(DownloadController, "/download/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
