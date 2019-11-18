import os
import numpy as np
import pandas as pd
from pathlib import Path


def normalize(x):
    x -= np.min(x)
    x /= np.max(x)
    return x


def df_to_labeled_sounds(df):
    result = dict()
    for index, row in df.iterrows():
        sound = row.fname
        labels = [label.strip() for label in row['labels'].split(',')]
        result[sound] = labels
    return result


class DataExpert:
    def __init__(self, data_root='data'):
        self.sounds_root = Path(data_root) / 'sounds'

        self.train_curated_root = self.sounds_root / 'train_curated'
        self.train_curated_df = pd.read_csv(self.sounds_root / 'train_curated.csv')

        self.train_noisy_root = self.sounds_root / 'train_noisy'
        self.train_noisy_df = pd.read_csv(self.sounds_root / 'train_noisy.csv')

        self.test_root = self.sounds_root / 'test'

        self.submission_df = pd.read_csv(self.sounds_root / 'sample_submission.csv')

        self.train_curated_sound_to_labels = df_to_labeled_sounds(self.train_curated_df)
        self.train_noisy_sound_to_labels = df_to_labeled_sounds(self.train_noisy_df)
        self.all_labels = self.get_all_labels()
        factorization = pd.factorize(self.all_labels)
        self.label_to_index = dict()
        self.index_to_label = dict()
        label_indices, label_names = factorization
        for label_index, label_name in zip(label_indices, label_names):
            self.label_to_index[label_name] = label_index
            self.index_to_label[label_index] = label_name

    def get_labels(self, sound_name):
        if sound_name in self.train_curated_sound_to_labels.keys():
            return self.train_curated_sound_to_labels[sound_name]
        if sound_name in self.train_noisy_sound_to_labels.keys():
            return self.train_noisy_sound_to_labels[sound_name]
        raise AttributeError(f'{sound_name} was not found. '
                             f'Please make sure you provide a file name, not a file path. '
                             f'You might get this error because you are trying to get the '
                             f'labels of a test wav.')

    def get_train_curated_wav_names(self):
        return list(sorted(os.listdir(self.train_curated_root)))

    def get_train_noisy_wav_names(self):
        return list(sorted(os.listdir(self.train_noisy_root)))

    def get_test_wav_names(self):
        return list(sorted(os.listdir(self.test_root)))

    def build_submission(self, model):
        """
        :param sounds_names_to_labels: A data frame like "dev/clink/submission.csv".
        """
        prediction = model.predict(self.get_test_wav_names())

    def get_all_labels(self):
        return self.submission_df.columns[1:]

    def to_categorical(self, labels):
        """
        Custom to_categorical to work for multi-class strings labels.
        :param labels: A list of strings.
        """
        output = np.zeros(shape=len(self.all_labels))
        for label in labels:
            index = self.label_to_index[label]
            output[index] = 1
        return output


if __name__ == '__main__':
    import pandas as pd

    data_expert = DataExpert(data_root='../../../data')
