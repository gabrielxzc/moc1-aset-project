from keras.layers import Dense
from keras.layers import LSTM
from keras.models import Sequential

from dev.clink.models.model import Model


class LSTMLearner(Model):

    def build_model(self, input_shape, output_shape):
        self.model = Sequential()
        self.model.add(LSTM(units=4, activation='sigmoid', input_shape=input_shape))
        self.model.add(Dense(units=output_shape))
        self.model.compile(optimizer='adam', loss='categorical_crossentropy')
