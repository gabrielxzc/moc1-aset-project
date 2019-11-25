import unittest
import pandas as pd
import sys

sys.path.append("../../")
from dev.clink.experts.audio_expert import *


class TestAudioMethods(unittest.TestCase):
    def test_config(self):
        self.assertEqual(Config.sampling_rate, 44100)


if __name__ == "__main__":
    unittest.main()
