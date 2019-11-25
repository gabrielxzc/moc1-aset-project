from dev.clink.converters.converter import Converter
from dev.clink.converters.aspects import *


class WavToSpectrogramConverter(Converter):
    def get_destination_root(self):
        return "../data/images"

    @log_call
    @validate_extension
    @validate_return_value
    def convert_wav(self, sound_path):
        image = self.audio_expert.read_as_melspectrogram(
            sound_path, trim_long_data=False
        )
        return self.image_expert.mono_to_color(image)
