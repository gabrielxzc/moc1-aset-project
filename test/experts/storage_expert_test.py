import unittest
import pandas as pd
import sys
import os

sys.path.append("../../")
from dev.clink.experts.storage_expert import *


class TestStringMethods(unittest.TestCase):
    def test_save_obj(self):
        data = {
            "a": [1, 2.0, 3, 4 + 6j],
            "b": ("character string", b"byte string"),
            "c": {None, True, False},
        }
        # self.assertEqual(os.listdir('../mocked_data'), [])
        save_object("../mocked_data/object.pickle", data)
        self.assertEqual(os.listdir("../mocked_data"), ["object.pickle"])

    def test_load_obj(self):
        data = {
            "a": [1, 2.0, 3, 4 + 6j],
            "b": ("character string", b"byte string"),
            "c": {None, True, False},
        }
        self.assertEqual(os.listdir("../mocked_data"), ["object.pickle"])
        self.assertEqual(load("../mocked_data/object.pickle"), data)


if __name__ == "__main__":
    unittest.main()
