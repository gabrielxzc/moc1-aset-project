import os
import shutil
import unittest
from pathlib import Path

from dev.clink.converters.wav_to_spectrogram_array import WavToSpectrogramConverter

os.chdir("../../")


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = WavToSpectrogramConverter()
        self.WAVS_DIR = "test/mocked_data/wavs"
        os.makedirs(self.WAVS_DIR, exist_ok=True)

    def test_config(self):
        self.converter.save_array_images(images=[('wqdq', 23), ('a.txt', 544), ('b.wav', 232)],
                                         root=Path(self.WAVS_DIR))

    def tearDown(self) -> None:
        shutil.rmtree(self.WAVS_DIR, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
