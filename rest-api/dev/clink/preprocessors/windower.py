import numpy as np
from pandas import DataFrame


class Windower:
    def __init__(self, data_expert, window_size=128, overlap=0.5):
        assert 0 <= overlap < 1
        self.data_expert = data_expert
        self.window_size = window_size
        self.overlap = overlap

    # works only for images
    def to_windows(self, arrays, labels):
        labels = [self.data_expert.to_categorical(label) for label in labels]

        new_arrays = []
        new_labels = []
        for array, label in zip(arrays, labels):
            k = 0
            while self.window_size * (k + 1) <= array.shape[1]:
                new_arrays.append(
                    array[
                    :,
                    int(self.window_size * k): int(self.window_size * (k + 1)),
                    :,
                    ]
                )
                new_labels.append(label)
                k += 1 - self.overlap
            new_arrays.append(array[:, -self.window_size:, :])
            new_labels.append(label)
        new_arrays = np.array(new_arrays) / 255
        new_labels = np.array(new_labels) / 255
        return new_arrays, new_labels

    def to_windows_only_x(self, arrays):
        new_arrays = []
        for array in arrays:
            k = 0
            while self.window_size * (k + 1) <= array.shape[1]:
                new_arrays.append(
                    array[:, int(self.window_size * k): int(self.window_size * (k + 1)), :, ]
                )
                k += 1 - self.overlap
            new_arrays.append(array[:, -self.window_size:, :])
        new_arrays = np.array(new_arrays) / 255
        return new_arrays

    def build_submission(self, model, root_dir):
        names = self.data_expert.get_test_wav_names()
        x = self.data_expert.load_test_arrays(root_dir)
        result = []
        for name, array in zip(names, x):
            new_arrays = []
            k = 0
            while self.window_size * (k + 1) <= array.shape[1]:
                new_arrays.append(
                    array[
                    :,
                    int(self.window_size * k): int(self.window_size * (k + 1)),
                    :,
                    ]
                )
                k += 1 - self.overlap
            new_arrays = np.array(new_arrays)
            y = model.predict(new_arrays)
            result.append(np.mean(y, axis=0))
        result = np.array(result)
        names = np.expand_dims(np.array(names), axis=1)
        result = np.hstack((names, result))
        df = DataFrame(data=result, columns=self.data_expert.get_all_column_names())
        df.set_index("fname", inplace=True)
        df.to_csv("submission.csv")
