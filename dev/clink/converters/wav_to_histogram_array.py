from dev.clink.converters.converter import Converter


class WavToHistogramConverter(Converter):

    def convert_wav(self, sound_path):
        raise NotImplementedError()
