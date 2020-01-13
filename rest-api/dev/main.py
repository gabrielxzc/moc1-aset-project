import sys

import numpy as np

from dev.clink.experts.storage_expert import save_object, load
from dev.clink.models.cnn_on_steroids import ChadCnnLearner

sys.path.append("../")

from dev.clink.converters.converter import Converter
from dev.clink.converters.wav_to_spectrogram_array import WavToSpectrogramConverter
from dev.clink.experts.data_expert import DataExpert
from dev.clink.models.model import Model
from dev.clink.preprocessors.windower import Windower


def main(convert=True, converter_class=Converter, model_class=Model, train=True, model_name='ResNet50'):
    data_expert = DataExpert(data_root="../data")
    windower = Windower(data_expert=data_expert, window_size=128, overlap=0.5)
    converter = converter_class(data_expert=data_expert)

    if convert:
        # create converted files at "image_path"
        converter.convert(
            convert_train_curated=True, convert_train_noisy=False, convert_test=False
        )

    # paths of converted files (images probably)
    image_path = converter.get_destination_root()

    x = data_expert.load_train_curated_arrays(image_path)
    y = data_expert.load_train_curated_labels()
    data = list(zip(x, y))
    np.random.shuffle(data)
    x, y = list(zip(*data))

    train_arrays = []
    test_arrays = []
    train_labels = []
    test_labels = []

    scores = np.random.uniform(size=len(x))
    train_percent = 0.8
    for i, score in enumerate(scores):
        if score <= train_percent:
            train_arrays.append(x[i])
            train_labels.append(y[i])
        else:
            test_arrays.append(x[i])
            test_labels.append(y[i])

    # train_arrays = np.array(train_arrays)
    # test_arrays = np.array(test_arrays)

    train_arrays, train_labels = windower.to_windows(train_arrays, train_labels)
    test_arrays, test_labels = windower.to_windows(test_arrays, test_labels)

    model = model_class(input_shape=train_arrays.shape[1:], output_shape=80, model_name=model_name)
    # initial_weights = model.model.get_weights()
    if train:
        history = model.fit(train_arrays, train_labels, epochs=5, validation_data=(test_arrays, test_labels))
        save_object(f'history_{model_name}.pickle', history.history)
        model.save_weights(filepath=f'weights_{model_name}')
    else:
        model.load_weights()

    # uncomment next line if you have an eternity to spare
    # k_fold_validation(model, windower, initial_weights, x, y)
    # [0.3342572062084257, 0.322840790842872, 0.3274555723518359, 0.3187491427848997, 0.32956557265422853]
    # 0.32657365696845236

    loss, acc = model.evaluate(test_arrays, test_labels)
    print(f"Train acc: {acc}")

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


def analysis(model_name):
    import matplotlib.pyplot as plt
    history = load(f'history_{model_name}.pickle')
    plt.plot(history['acc'], label='acc')
    plt.plot(history['val_acc'], label='val_acc')
    plt.legend(loc='best')
    plt.show()


# 3040 MB
# 790,777,374 parameters

# If you have cudnn enabled, you can monitor the gpu with
# watch -n 0.5 nvidia-smi
if __name__ == "__main__":
    names = [
        'Xception', 'VGG16', 'VGG19', 'ResNet50', 'ResNet101', 'ResNet152', 'ResNet50V2', 'ResNet101V2', 'ResNet152V2',
        'InceptionV3', 'InceptionResNetV2', 'MobileNet', 'DenseNet121', 'DenseNet169', 'DenseNet201', 'NASNetLarge',
        'NASNetMobile', 'MobileNetV2']
    for name in names:
        main(convert=False, converter_class=WavToSpectrogramConverter,
             model_class=ChadCnnLearner, train=True, model_name=name)
    # main(convert=False, converter_class=WavToSpectrogramConverter,
    #      model_class=ChadCnnLearner, train=True, model_name='ResNet50')
    # analysis('ResNet50')
