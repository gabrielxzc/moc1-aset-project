import numpy as np

from dev.clink.aspects.models.model import fit
from dev.clink.experts.data_expert import normalize


class Model:
    def __init__(self, input_shape, output_shape):
        self.model = None
        self.build_model(input_shape, output_shape)

    @fit
    def fit(self, x, y, epochs=5, batch_size=128, validation_data=None):
        self.model.fit(
            x, y, epochs=epochs, batch_size=batch_size, validation_data=validation_data
        )

    def evaluate(self, x, y):
        return self.model.evaluate(x, y)

    def predict(self, x):
        return self.model.predict(x)

    def save_weights(self, filepath="weights"):
        self.model.save_weights(filepath)

    def load_weights(self, filepath="weights"):
        self.model.load_weights(filepath)

    def build_model(self, input_shape, output_shape):
        """
        Add layers and compile.
        :param input_shape: Use the input shape for the first layer.
        :param output_shape: Use the output shape for the last layer.
        """
        raise NotImplementedError()
