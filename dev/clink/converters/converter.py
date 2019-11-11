from tqdm import tqdm_notebook
from dev.clink.experts.audio_expert import AudioExpert
from dev.clink.experts.data_expert import DataExpert
from dev.clink.experts.image_expert import ImageExpert
from dev.clink.experts.storage_expert import save_object


class Converter:
    def __init__(self, data_expert=None, audio_expert=None, image_expert=None):
        if audio_expert is None:
            audio_expert = AudioExpert()
        if data_expert is None:
            data_expert = DataExpert()
        if image_expert is None:
            image_expert = ImageExpert()

        self.audio_expert = audio_expert
        self.data_expert = data_expert
        self.image_expert = image_expert

    def convert_wav(self, sound_path):
        raise NotImplementedError()

    def convert_multiple_wavs(self, df, source):
        images = []
        for i, row in tqdm_notebook(df.iterrows()):
            print(f'{i + 1} / {df.shape[0]}')
            name = str(row.fname)
            x_color = self.convert_wav(source / name)
            images.append((name, x_color))
        return images

    def convert(self, convert_train_curated=True, convert_train_noisy=False, convert_test=True):
        if convert_train_curated:
            train_curated = self.convert_multiple_wavs(self.data_expert.train_curated_df,
                                                       source=self.data_expert.train_curated_root)
            self.save_array_images(train_curated, self.data_expert.destination_train_curated)

        if convert_train_noisy:
            train_noisy = self.convert_multiple_wavs(self.data_expert.train_noisy_df,
                                                     source=self.data_expert.train_noisy_root)
            self.save_array_images(train_noisy, self.data_expert.destination_train_noisy)

        if convert_test:
            test = self.convert_multiple_wavs(self.data_expert.submission_df,
                                              source=self.data_expert.test_root)
            self.save_array_images(test, self.data_expert.destination_test)

    @staticmethod
    def save_array_images(images, root):
        for (name, image) in images:
            save_object(root / name, image)
