from dev.clink.converters.converter import Converter


class WavToSampledArrayConverter(Converter):
    def convert_wav(self, sound_path):
        raise NotImplementedError()
