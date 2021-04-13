import keras
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten, Dropout
from keras.layers.core import Dense
from keras.datasets import mnist
from keras.optimizers import Adam
from keras.callbacks import TensorBoard


def lenet(input_shape, num_classes):
    model = Sequential()
    model.add(Conv2D(20, kernel_size=5, padding='same', input_shape=input_shape, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

