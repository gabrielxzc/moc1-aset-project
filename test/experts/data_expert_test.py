import unittest
import pandas as pd
import sys
sys.path.append('../../')
from dev.clink.experts.data_expert import *


class TestStringMethods(unittest.TestCase):
    # def test_df_to_sound_labels(self):
    #     df = pd.DataFrame(columns=['fname', 'labels'],
    #                       data=[['sound1', 'label1'], ['sound2', 'label21,label22']])
    #     result = df_to_labeled_sounds(df)
    #     print(result)
    #
    #     self.assertEqual(result.keys(), {'sound1', 'sound2'})
    #     self.assertEqual(result['sound1'], ['label1'])
    #     self.assertEqual(result['sound2'], ['label21', 'label22'])

    def test_get_labels(self, sound_name = '00c7ff40.wav'):
        data_expert = DataExpert()
        self.assertEqual(data_expert.get_labels(sound_name), ['Stream'])

    # def test_get_labels(self, sound_name = '....'):
    #     data_expert = DataExpert()
    #     self.assertEqual(get_labels(sound_name), [....])
    #
    # def test_get_all_labels(self):
    #     submission_file = pd.read_csv('')
    #     self.assertEqual(data_expert.get_all_labels(), submission_file['labels'])
    #
    # def test_get_test_wav_names(self):
    #     data_expert = DataExpert()
    #     self.assertEqual(data_expert.get_test_wav_names(), os.listdir('../../../data/'))

if __name__ == '__main__':
    unittest.main()
