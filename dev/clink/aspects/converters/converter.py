import aspectlib

from dev.clink.experts.audio_expert import AudioExpert
from dev.clink.experts.data_expert import DataExpert
from dev.clink.experts.image_expert import ImageExpert

AUDIO_EXPERT = "audio_expert"
DATA_EXPERT = "data_expert"
IMAGE_EXPERT = "image_expert"


# @aspectlib.Aspect
def init(*args, **kwargs):
    print("Initializing new Converter ...")

    if AUDIO_EXPERT not in kwargs:
        print("Converter did not receive an audio expert. Creating a default one.")
        kwargs.update({AUDIO_EXPERT: AudioExpert()})

    if DATA_EXPERT not in kwargs:
        print("Converter did not receive a data expert. Creating a default one.")
        kwargs.update({DATA_EXPERT: DataExpert()})

    if IMAGE_EXPERT not in kwargs:
        print("Converter did not receive an image expert. Creating a default one.")
        kwargs.update({IMAGE_EXPERT: ImageExpert()})

    # yield aspectlib.Proceed(*args, **kwargs)

    print("Converter successfully initialized.")
