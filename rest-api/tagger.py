from algorithm.submission_tagger import tag_sound

from base64 import b64encode, decodebytes

if __name__ == "__main__":
    filename = "tmp_image.wav"

    # encoded_string = b64encode(open(filename, "r").read())
    # print(encoded_string)
    # tmp_image = open("tmp_image.wav", "w")
    # tmp_image.write(decodebytes(encoded_string))
    # tmp_image.close()
    print(tag_sound(filename))