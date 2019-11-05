import unittest
import pandas as pd

from dev.clink.experts.data_expert import df_to_labeled_sounds


class TestStringMethods(unittest.TestCase):
    def test_df_to_sound_labels(self):
        df = pd.DataFrame(columns=['fname', 'labels'],
                          data=[['sound1', 'label1'], ['sound2', 'label21,label22']])
        result = df_to_labeled_sounds(df)
        print(result)

        self.assertEqual(result.keys(), {'sound1', 'sound2'})
        self.assertEqual(result['sound1'], ['label1'])
        self.assertEqual(result['sound2'], ['label21', 'label22'])


if __name__ == '__main__':
    unittest.main()
