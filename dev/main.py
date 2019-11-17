import os
import sys
import numpy as np
import pandas as pd

from dev.clink.converters.wav_to_spectrogram_array import WavToSpectrogramConverter
from dev.clink.experts.data_expert import DataExpert, normalize

from dev.clink.experts.image_expert import ImageExpert
from dev.clink.experts.storage_expert import load
from dev.clink.models.cnn import CnnLearner

sys.path.append("../")


# works only for images
def to_windows(data_expert, arrays, labels, window_size=128, overlap=0.5):
    labels = [data_expert.to_categorical(label) for label in labels]

    new_arrays = []
    new_labels = []
    for array, label in zip(arrays, labels):
        k = 0
        while window_size * (k + 1) <= array.shape[1]:
            new_arrays.append(array[:, window_size * k:window_size * (k + 1), :])
            new_labels.append(label)
            k += 1
        new_arrays.append(array[:, -window_size:, :])
        new_labels.append(label)
    new_arrays = np.array(new_arrays) / 255
    new_labels = np.array(new_labels) / 255
    return new_arrays, new_labels


def main(convert=True, converter_class=WavToSpectrogramConverter, model_class=CnnLearner):
    image_path = '../data/images'
    data_expert = DataExpert(data_root='../data', destination_root=image_path)

    if convert:
        # create converted files at "image_path"
        converter_class(data_expert=data_expert) \
            .convert(convert_train_curated=False, convert_train_noisy=True, convert_test=False)

    # paths of converted files (images probably)
    train_arrays_paths = [os.path.join(image_path, 'train_curated', name)
                          for name in data_expert.get_train_curated_wav_names()]

    train_arrays = [load(path) for path in train_arrays_paths]
    train_labels = [data_expert.get_labels(name) for name in data_expert.get_train_curated_wav_names()]

    train_arrays, train_labels = to_windows(data_expert, train_arrays, train_labels, window_size=128)

    model = model_class(input_shape=train_arrays.shape[1:], output_shape=80)

    model.fit(train_arrays, train_labels)

    # test_arrays_paths = [os.path.join(image_path, 'train_noisy', name)
    #                      for name in data_expert.get_train_noisy_wav_names()]
    # test_arrays = [load(path) for path in test_arrays_paths]
    # test_labels = [data_expert.get_labels(name) for name in data_expert.get_train_noisy_wav_names()]
    #
    # test_arrays, test_labels = to_windows(data_expert, test_arrays, test_labels, window_size=128)
    print(model.evaluate(train_arrays, train_labels))

    # maybe some processing before
    # data_expert.build_submission(prediction)


if __name__ == '__main__':
    main(convert=False, converter_class=WavToSpectrogramConverter, model_class=CnnLearner)
