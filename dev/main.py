import os
import sys
import numpy as np
import pandas as pd

sys.path.append("../")

from dev.clink.converters.converter import Converter
from dev.clink.converters.fft_converter import FftConverter
from dev.clink.converters.wav_to_spectrogram_array import WavToSpectrogramConverter
from dev.clink.experts.data_expert import DataExpert
from dev.clink.models.cnn import CnnLearner
from dev.clink.models.lstm import LSTMLearner
from dev.clink.models.model import Model
from dev.clink.preprocessors.windower import Windower


def main(convert=True, converter_class=Converter, model_class=Model, train=True):
    data_expert = DataExpert(data_root='../data')
    windower = Windower(data_expert=data_expert, window_size=128, overlap=0.5)
    converter = converter_class(data_expert=data_expert)

    if convert:
        # create converted files at "image_path"
        converter.convert(convert_train_curated=True, convert_train_noisy=False, convert_test=False)

    # paths of converted files (images probably)
    image_path = converter.get_destination_root()

    train_arrays = data_expert.load_train_curated_arrays(image_path)
    train_labels = data_expert.load_train_curated_labels()
    x = train_arrays
    y = train_labels
    train_arrays, train_labels = windower.to_windows(train_arrays, train_labels)

    model = model_class(input_shape=train_arrays.shape[1:], output_shape=80)
    initial_weights = model.model.get_weights()
    if train:
        model.fit(train_arrays, train_labels, epochs=5)
        model.save_weights()
    else:
        model.load_weights()

    # uncomment next line if you have an eternity to spare
    k_fold_validation(model, windower, initial_weights, x, y)
    # [0.3342572062084257, 0.322840790842872, 0.3274555723518359, 0.3187491427848997, 0.32956557265422853]
    # 0.32657365696845236

    loss, acc = model.evaluate(train_arrays, train_labels)
    print(f'Train acc: {acc}')

    # windower.build_submission(model, converter.get_destination_root())


def k_fold_validation(model, windower, initial_weights, x, y, k=5):
    accuracies = []
    n = len(x) // k

    for i in range(k):
        start_index = n * i
        end_index = n * (i + 1)
        train_x = x[:start_index] + x[end_index:]
        train_y = y[:start_index] + y[end_index:]
        test_x = x[start_index:end_index]
        test_y = y[start_index:end_index]

        train_x, train_y = windower.to_windows(train_x, train_y)
        test_x, test_y = windower.to_windows(test_x, test_y)
        model.model.set_weights(initial_weights)
        model.fit(train_x, train_y)
        loss, acc = model.evaluate(test_x, test_y)
        accuracies.append(acc)
    print(accuracies)
    print(np.mean(accuracies))


# If you have cudnn enabled, you can monitor the gpu with
# watch -n 05 nvidia-smi
if __name__ == '__main__':
    main(convert=True, converter_class=WavToSpectrogramConverter,
         model_class=CnnLearner, train=False)
