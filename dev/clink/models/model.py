import numpy as np

from dev.clink.experts.data_expert import normalize


class Model:
    def __init__(self, input_shape, output_shape):
        self.model = None
        self.build_model(input_shape, output_shape)

    def fit(self, x, y, epochs=5, batch_size=None, validation_data=None):
        self.model.fit(x, y, epochs=epochs, batch_size=batch_size, validation_data=validation_data)

    def predict(self, x):
        if np.max(x) > 1:
            x = normalize(x)
        return self.model.predict(x)

    def build_model(self, input_shape, output_shape):
        raise NotImplementedError()
