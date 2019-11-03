import numpy as np


class ImageExpert:
    def __init__(self):
        pass

    @staticmethod
    def mono_to_color(x, mean=None, std=None, norm_max=None, norm_min=None, eps=1e-6):
        # Stack X as [X,X,X]
        x = np.stack([x, x, x], axis=-1)

        # Standardize
        mean = mean or x.mean()
        std = std or x.std()
        x_std = (x - mean) / (std + eps)
        _min, _max = x_std.min(), x_std.max()
        norm_max = norm_max or _max
        norm_min = norm_min or _min
        if (_max - _min) > eps:
            # Scale to [0, 255]
            v = x_std
            v[v < norm_min] = norm_min
            v[v > norm_max] = norm_max
            v = 255 * (v - norm_min) / (norm_max - norm_min)
            v = v.astype(np.uint8)
        else:
            # Just zero
            v = np.zeros_like(x_std, dtype=np.uint8)
        return v

    def array_to_image(self, np_array):
        raise NotImplementedError()

    def image_to_array(self, image):
        raise NotImplementedError()
