import keras
from keras import models
from keras import layers
from keras import optimizers
from keras.utils import np_utils
from keras.datasets import cifar10
import keras_applications
from dev.clink.models.model import Model

# DO NOT REMOVE UNUSED IMPORTS. THEY ARE NEEDED FOR eval(model_name)

from keras.applications.xception import Xception
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.mobilenet import MobileNet
from keras.applications.densenet import DenseNet121
from keras.applications.densenet import DenseNet169
from keras.applications.densenet import DenseNet201
from keras.applications.nasnet import NASNetLarge
from keras.applications.nasnet import NASNetMobile
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.applications.xception import Xception
from keras_applications.resnet import ResNet50
from keras_applications.resnet import ResNet101
from keras_applications.resnet import ResNet152
from keras_applications.resnet_v2 import ResNet50V2
from keras_applications.resnet_v2 import ResNet101V2
from keras_applications.resnet_v2 import ResNet152V2

# DO NOT REMOVE UNUSED IMPORTS. THEY ARE NEEDED FOR eval(model_name)


class ChadCnnLearner(Model):

    def build_model(self, input_shape, output_shape):
        params = {'weights': 'imagenet', 'include_top': False, 'input_shape': input_shape,
                  'backend': keras.backend, 'layers': keras.layers, 'models': keras.models, 'utils': keras.utils}

        conv_base = eval(self.model_name)(**params)
        model = models.Sequential()
        # model.add(layers.UpSampling2D((2, 2)))
        # model.add(layers.UpSampling2D((2, 2)))
        # model.add(layers.UpSampling2D((2, 2)))
        model.add(conv_base)
        model.add(layers.Flatten())

        # model.add(layers.BatchNormalization())
        # model.add(layers.Dense(128, activation='relu'))

        # model.add(layers.Dropout(0.5))
        # model.add(layers.BatchNormalization())
        # model.add(layers.Dense(64, activation='relu'))

        model.add(layers.BatchNormalization())
        model.add(layers.Dense(output_shape, activation='softmax'))

        model.compile(optimizer=optimizers.RMSprop(lr=2e-5), loss='categorical_crossentropy', metrics=['acc'])
        self.model = model


if __name__ == '__main__':
    params = {'weights': 'imagenet', 'include_top': False, 'input_shape': (32, 32, 3),
              'backend': keras.backend, 'layers': keras.layers, 'models': keras.models, 'utils': keras.utils}
    name = 'ResNet50'
    model = eval(name)(**params)
    print(model)
