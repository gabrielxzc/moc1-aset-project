from pathlib import Path
import pandas as pd


class DataExpert:
    def __init__(self, data_root='data', destination_root='data/images'):
        self.sounds_root = Path(data_root) / 'sounds'

        self.train_curated_root = self.sounds_root / 'train_curated'
        self.train_curated_df = pd.load_csv(self.sounds_root / 'train_curated.csv')

        self.train_noisy_root = self.sounds_root / 'train_noisy'
        self.train_noisy_df = pd.load_csv(self.sounds_root / 'train_noisy.csv')

        self.test_root = self.sounds_root / 'test'

        self.submission_df = pd.load_csv(self.sounds_root / 'sample_submission.csv')

        self.destination_root = Path(destination_root)
        self.destination_train_curated = self.destination_root / 'train_curated'
        self.destination_train_noisy = self.destination_root / 'train_noisy'
        self.destination_test = self.destination_root / 'test'
        for folder in [self.destination_root, self.destination_train_curated,
                       self.destination_train_noisy, self.destination_test]:
            Path(folder).mkdir(parents=True, exist_ok=True)
