from pathlib import Path
import pandas as pd


def df_to_labeled_sounds(df):
    result = dict()
    for index, row in df.iterrows():
        sound = row.fname
        labels = [label.strip() for label in row['labels'].split(',')]
        result[sound] = labels
    return result


class DataExpert:
    def __init__(self, data_root='data', destination_root='data/images'):
        self.sounds_root = Path(data_root) / 'sounds'

        self.train_curated_root = self.sounds_root / 'train_curated'
        self.train_curated_df = pd.read_csv(self.sounds_root / 'train_curated.csv')

        self.train_noisy_root = self.sounds_root / 'train_noisy'
        self.train_noisy_df = pd.read_csv(self.sounds_root / 'train_noisy.csv')

        self.test_root = self.sounds_root / 'test'

        self.submission_df = pd.read_csv(self.sounds_root / 'sample_submission.csv')

        self.destination_root = Path(destination_root)
        self.destination_train_curated = self.destination_root / 'train_curated'
        self.destination_train_noisy = self.destination_root / 'train_noisy'
        self.destination_test = self.destination_root / 'test'

        self.train_curated_sound_to_labels = df_to_labeled_sounds(self.train_curated_df)
        self.train_noisy_sound_to_labels = df_to_labeled_sounds(self.train_noisy_df)

        for folder in [self.destination_root, self.destination_train_curated,
                       self.destination_train_noisy, self.destination_test]:
            Path(folder).mkdir(parents=True, exist_ok=True)

    def get_labels(self, sound_name):
        if sound_name in self.train_curated_sound_to_labels.keys():
            return self.train_curated_sound_to_labels[sound_name]
        if sound_name in self.train_noisy_sound_to_labels.keys():
            return self.train_noisy_sound_to_labels[sound_name]
        raise AttributeError(f'{sound_name} was not found. '
                             f'Please make sure you provide a file name, not a file path.')

    def build_submission(self, sounds_names_to_labels):
        pass
