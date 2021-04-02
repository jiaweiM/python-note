import numpy as np
import random
from keras.datasets import cifar10

def test_config():
    print(np.__config__.show())


def test():
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
