import aspectlib

from dev.clink.converters.converter import Converter

@aspectlib.Aspect(bind = True)
def log_call(cutpoint, *args, **kargs):
	with open("calls.txt", "a") as out_file:
		out_file.write(str(cutpoint.__name__) + "\n")
	yield

@aspectlib.Aspect()
def validate_extension(*args, **kargs):
	sound_path = kargs['sound_path']
	assert sound_path[-4:] == ".wav"
	yield

class WavToSpectrogramConverter(Converter):

    @log_call
    @validate_extension
    def convert_wav(self, sound_path):
        image = self.audio_expert.read_as_melspectrogram(sound_path, trim_long_data=False)
        return self.image_expert.mono_to_color(image)
