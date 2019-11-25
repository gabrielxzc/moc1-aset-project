from pathlib import Path

import aspectlib

from dev.clink.aspects.converters.converter import init
from dev.clink.experts.storage_expert import save_object
from dev.clink.converters.aspects import ensure_wav_extension


@aspectlib.Aspect(bind=True)
def log_call(cutpoint, *args, **kargs):
    with open("calls.txt", "a") as out_file:
        out_file.write(str(cutpoint.__name__) + "\n")
    yield


class Converter:
    @init
    def __init__(self, data_expert=None, audio_expert=None, image_expert=None):
        self.destination_root = Path(self.get_destination_root())
        self.destination_train_curated = self.destination_root / "train_curated"
        self.destination_train_noisy = self.destination_root / "train_noisy"
        self.destination_test = self.destination_root / "test"

        for folder in [
            self.destination_root,
            self.destination_train_curated,
            self.destination_train_noisy,
            self.destination_test,
        ]:
            Path(folder).mkdir(parents=True, exist_ok=True)

        self.audio_expert = audio_expert
        self.data_expert = data_expert
        self.image_expert = image_expert

    def convert_wav(self, sound_path):
        """
        :param sound_path: A path to a wav to process
        :return: A tensor of any shape.
        """
        raise NotImplementedError()

    def get_destination_root(self):
        """
        :return: A folder where the converted tensors will be stored.
        Preferably, all implementations should have different folders.
        Otherwise, overwriting will occur.
        """
        raise NotImplementedError()

    @log_call
    def convert_multiple_wavs(self, df, source):
        images = []
        for i, row in df.iterrows():
            print(f"{i + 1} / {df.shape[0]}")
            name = str(row.fname)
            x_color = self.convert_wav(source / name)
            images.append((name, x_color))
        return images

    def convert(
        self, convert_train_curated=True, convert_train_noisy=False, convert_test=True
    ):
        if convert_train_curated:
            # self.save_array_images(images = [('wqdq', 23), ('a.txt', 544), ('b.wav', 232)], root = Path("/home/cristi"))
            train_curated = self.convert_multiple_wavs(
                self.data_expert.train_curated_df,
                source=self.data_expert.train_curated_root,
            )
            self.save_array_images(train_curated, self.destination_train_curated)

        if convert_train_noisy:
            train_noisy = self.convert_multiple_wavs(
                self.data_expert.train_noisy_df,
                source=self.data_expert.train_noisy_root,
            )
            self.save_array_images(train_noisy, self.destination_train_noisy)

        if convert_test:
            test = self.convert_multiple_wavs(
                self.data_expert.submission_df, source=self.data_expert.test_root
            )
            self.save_array_images(test, self.destination_test)

    @staticmethod
    @ensure_wav_extension
    def save_array_images(images, root):
        for (name, image) in images:
            # print(name)
            save_object(root / name, image)
