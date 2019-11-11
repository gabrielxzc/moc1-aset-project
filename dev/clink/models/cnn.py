from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

from dev.clink.models.model import Model


class CnnLearner(Model):

    def build_model(self, input_shape, output_shape):
        self.model = Sequential()
        self.model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=input_shape))
        self.model.add(Conv2D(32, kernel_size=3, activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(output_shape, activation='softmax'))
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
