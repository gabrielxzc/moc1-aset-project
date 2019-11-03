from clink.converters.spectrogram_converter import SpectrogramConverter
import numpy as np

from clink.experts.image_expert import ImageExpert

converter = SpectrogramConverter()
# converter.convert_all()

sound_path = 'data/sounds/train_curated/0a9bebde.wav'
image = converter.convert_sound_to_image(sound_path)

image = ImageExpert.array_to_image(image)
image.show()

