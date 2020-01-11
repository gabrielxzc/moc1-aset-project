import sys
import numpy as np
from keras.models import load_model

from dev.clink.aspects.experts.audio_expert import Config
from dev.clink.experts.audio_expert import AudioExpert
from dev.clink.experts.image_expert import ImageExpert

from dev.clink.converters.wav_to_spectrogram_array import WavToSpectrogramConverter
from dev.clink.experts.data_expert import DataExpert
from dev.clink.preprocessors.windower import Windower

sys.path.append("../")


def tag_sound(sound_path, data_root='data', model_path='model/model.h5'):
    data_expert = DataExpert(data_root=data_root)
    windower = Windower(data_expert=data_expert, window_size=128, overlap=0.5)
    converter = WavToSpectrogramConverter(data_expert=data_expert,
                                          audio_expert=AudioExpert(Config()), image_expert=ImageExpert())
    image = converter.convert_wav(sound_path)
    windows = windower.to_windows_only_x([image])
    model = load_model(model_path)
    y = model.predict(windows)
    result = np.mean(y, axis=0)
    columns = data_expert.get_all_labels()

    indices = list(reversed(np.argsort(result)))
    winners = [indices[0]]
    p = 1
    while result[p - 1] / result[p] < result[p] / result[p + 1]:
        winners.append(indices[p])
        p += 1
    return columns[winners].values


if __name__ == "__main__":
    print(tag_sound('barking_sound.wav'))
