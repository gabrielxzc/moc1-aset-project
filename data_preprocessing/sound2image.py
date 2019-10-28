import numpy as np
import librosa
import librosa.display
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from pathlib import Path
import matplotlib.pyplot as plt
from tqdm import tqdm_notebook
import PIL
import pickle


def save(path, obj):
    with open(path, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load(path):
    with open(path, 'rb') as handle:
        return pickle.load(handle)


def read_audio(conf, pathname, trim_long_data):
    y, sr = librosa.load(pathname, sr=conf.sampling_rate)
    # trim silence
    if 0 < len(y):  # workaround: 0 length causes error
        y, _ = librosa.effects.trim(y)  # trim, top_db=default(60)
    # make it unified length to conf.samples
    if len(y) > conf.samples:  # long enough
        if trim_long_data:
            y = y[0:0 + conf.samples]
    else:  # pad blank
        padding = conf.samples - len(y)  # add padding at both ends
        offset = padding // 2
        y = np.pad(y, (offset, conf.samples - len(y) - offset), 'constant')
    return y


def audio_to_melspectrogram(conf, audio):
    spectrogram = librosa.feature.melspectrogram(audio,
                                                 sr=conf.sampling_rate,
                                                 n_mels=conf.n_mels,
                                                 hop_length=conf.hop_length,
                                                 n_fft=conf.n_fft,
                                                 fmin=conf.fmin,
                                                 fmax=conf.fmax)
    spectrogram = librosa.power_to_db(spectrogram)
    spectrogram = spectrogram.astype(np.float32)
    return spectrogram


def show_melspectrogram(conf, mels, title='Log-frequency power spectrogram'):
    librosa.display.specshow(mels, x_axis='time', y_axis='mel',
                             sr=conf.sampling_rate, hop_length=conf.hop_length,
                             fmin=conf.fmin, fmax=conf.fmax)
    plt.colorbar(format='%+2.0f dB')
    plt.title(title)
    plt.show()


class conf:
    # Preprocessing settings
    sampling_rate = 44100
    duration = 2
    hop_length = 347 * duration  # to make time steps 128
    fmin = 20
    fmax = sampling_rate // 2
    n_mels = 128
    n_fft = n_mels * 20
    samples = sampling_rate * duration


def mono_to_color(X, mean=None, std=None, norm_max=None, norm_min=None, eps=1e-6):
    # Stack X as [X,X,X]
    X = np.stack([X, X, X], axis=-1)

    # Standardize
    mean = mean or X.mean()
    std = std or X.std()
    Xstd = (X - mean) / (std + eps)
    _min, _max = Xstd.min(), Xstd.max()
    norm_max = norm_max or _max
    norm_min = norm_min or _min
    if (_max - _min) > eps:
        # Scale to [0, 255]
        V = Xstd
        V[V < norm_min] = norm_min
        V[V > norm_max] = norm_max
        V = 255 * (V - norm_min) / (norm_max - norm_min)
        V = V.astype(np.uint8)
    else:
        # Just zero
        V = np.zeros_like(Xstd, dtype=np.uint8)
    return V


def read_as_melspectrogram(conf, pathname, trim_long_data, debug_display=False):
    x = read_audio(conf, pathname, trim_long_data)
    mels = audio_to_melspectrogram(conf, x)
    if debug_display:
        # IPython.display.display(IPython.display.Audio(x, rate=conf.sampling_rate))
        show_melspectrogram(conf, mels)
    return mels


def convert_wav_to_image(df, source, img_dest):
    X = []
    for i, row in tqdm_notebook(df.iterrows()):
        print(i, df.shape[0])
        x = read_as_melspectrogram(conf, source / str(row.fname), trim_long_data=False)
        x_color = mono_to_color(x)
        save(img_dest / str(row.fname), x_color)
        # X.append(x_color)
    # save(img_dest / 'arrays.pickle', X)
    return X


def do_sound_to_image():
    """
    Requires 16 GB RAM.
    """
    DATA = Path('../data')
    CSV_TRN_CURATED = DATA / 'train_curated.csv'
    CSV_TRN_NOISY = DATA / 'train_noisy.csv'
    CSV_SUBMISSION = DATA / 'sample_submission.csv'
    TRN_CURATED = DATA / 'train_curated'
    TRN_NOISY = DATA / 'train_noisy'
    TEST = DATA / 'test'

    WORK = Path('../work')
    IMG_TRN_CURATED = WORK / 'image/trn_curated'
    IMG_TRN_NOISY = WORK / 'image/train_noisy'
    IMG_TEST = WORK / 'image/test'
    for folder in [WORK, IMG_TRN_CURATED, IMG_TRN_NOISY, IMG_TEST]:
        Path(folder).mkdir(exist_ok=True, parents=True)

    df = pd.read_csv(CSV_TRN_CURATED)
    df_noisy = pd.read_csv(CSV_TRN_NOISY)
    test_df = pd.read_csv(CSV_SUBMISSION)

    X_train = convert_wav_to_image(df, source=TRN_CURATED, img_dest=IMG_TRN_CURATED)
    # X_noisy = convert_wav_to_image(df_noisy, source=TRN_NOISY, img_dest=IMG_TRN_NOISY)
    X_test = convert_wav_to_image(test_df, source=TEST, img_dest=IMG_TEST)

    # save(WORK / 'test_arrays.pickle', X_test)


if __name__ == '__main__':
    import sys
    import time
    do_sound_to_image()
    # X_train, X_noisy, X_test = load('../work/arrays.pickle')
    # save('../work/curated_array.pickle', X_train)
    # save('../work/noisy_array.pickle', X_noisy)
    # save('../work/test_array.pickle', X_test)
