from dev.clink.converters.converter import Converter


class WavToSpectrogramConverter(Converter):

    def convert_wav(self, sound_path):
        image = self.audio_expert.read_as_melspectrogram(sound_path, trim_long_data=False)
        return self.image_expert.mono_to_color(image)
