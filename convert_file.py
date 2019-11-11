import _pickle as cPickle
import aspectlib

from dev.clink.converters.wav_to_spectrogram_array import WavToSpectrogramConverter

def f():
	converter = WavToSpectrogramConverter()
	spectogram = converter.convert_wav(sound_path = "data_preprocessing/data/train_curated/771f6c75.wav")

	with open("data_preprocessing/data/train_curated_spectograms/771f6c75.wav", "wb") as out_file:
		cPickle.dump(spectogram, out_file)
	
f()
