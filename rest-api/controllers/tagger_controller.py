import base64
from flask_restful import Resource, request
from algorithm.submission_tagger import tag_sound
from keras.models import load_model


class TaggerController(Resource):
    def post(self):
        file_str = request.get_json()["file"]
        decoded = base64.b64decode(file_str[file_str.index("base64") + 7:])
        tmp_image = open("tmp_image.wav", "wb")
        tmp_image.write(decoded)
        tmp_image.close()

        # load_model('model/model.h5')
        tags = tag_sound("tmp_image.wav")
        return tags.tolist()
