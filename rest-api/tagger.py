from algorithm.submission_tagger import tag_sound

from base64 import b64encode, decodebytes

if __name__ == "__main__":
    filename = "0a9bebde.wav"

    encoded_string = b64encode(bytes(open(filename, "r").read(), "utf-8"))
    print(encoded_string)
    tmp_image = open("tmp_image.wav", "w")
    tmp_image.write(decodebytes(encoded_string))
    print(tag_sound("tmp_image.wav"))