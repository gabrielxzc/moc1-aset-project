from tqdm import tqdm_notebook

from clink.experts.audio_expert import AudioExpert
from clink.experts.data_expert import DataExpert
from clink.experts.image_expert import ImageExpert
from clink.experts.storage_expert import save_object


class SpectrogramConverter:
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

    def convert_sound_to_image(self, sound_path):
        image = self.audio_expert.read_as_melspectrogram(sound_path, trim_long_data=False)
        return self.image_expert.mono_to_color(image)

    def convert_sounds_to_images(self, df, source):
        images = []
        for i, row in tqdm_notebook(df.iterrows()):
            print(i, df.shape[0])
            name = str(row.fname)
            x_color = self.convert_sound_to_image(source / name)
            images.append((name, x_color))
        return images

    @staticmethod
    def save_images(images, root):
        for (name, image) in images:
            save_object(root / name, image)

    def convert_all(self):
        train_curated = self.convert_sounds_to_images(self.data_expert.train_curated_df,
                                                      source=self.data_expert.train_curated_root)
        train_noisy = self.convert_sounds_to_images(self.data_expert.train_noisy_df,
                                                    source=self.data_expert.train_noisy_root)
        test = self.convert_sounds_to_images(self.data_expert.submission_df,
                                             source=self.data_expert.test_root)

        self.save_images(train_curated, self.data_expert.destination_train_curated)
        self.save_images(train_noisy, self.data_expert.destination_train_noisy)
        self.save_images(test, self.data_expert.destination_test)

        return train_curated, train_noisy, test
