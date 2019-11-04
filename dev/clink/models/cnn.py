# THIS IS JUST UN EXAMPLE

import matplotlib.pyplot as plt
import numpy as np

from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten


def normalize(x):
    x -= np.min(x)
    x /= np.max(x)
    return x


class CnnLearner:
    def __init__(self, input_shape, output_shape):
        self.model = Sequential()
        self.model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=input_shape))
        self.model.add(Conv2D(32, kernel_size=3, activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(output_shape, activation='softmax'))
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def train(self, x, y, epochs=3, validation_data=None):
        if np.max(x) > 1:
            x = normalize(x)
        self.model.fit(x, y, validation_data=validation_data, epochs=epochs)

    def predict(self, x):
        return self.model.predict(x)


(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 28, 28, 1) / 255
X_test = X_test.reshape(10000, 28, 28, 1) / 255

# one-hot encode target column
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

learner = CnnLearner((28, 28, 1), 10)
learner.train(X_train, y_train)
print(learner.predict(X_test[:4]))
print(y_test[:4])
