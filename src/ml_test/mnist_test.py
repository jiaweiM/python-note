import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


def test_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    assert type(x_train) == np.ndarray
    assert x_train.shape == (60000, 28, 28)
    assert y_train.shape == (60000,)

    assert x_test.shape == (10000, 28, 28)
    assert y_test.shape == (10000,)

    # Preprocessing of MNIST
    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)

    # Casting to a float32 because of divide error when dividing by itself
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    # Normalizes data to a float32 type in the range of 0 to 1
    x_train /= 255
    x_test /= 255

    # Convert to categorical data 1 -> [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_train = tf.keras.utils.to_categorical(y_train, 10)
    y_test = tf.keras.utils.to_categorical(y_test, 10)


def test_show_img():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    assert y_test[0] == 7
    plt.imshow(x_test[0])
    plt.show()


def test_model():
    # Building a Deep learning model
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(input_shape=(784,)),
        tf.keras.layers.Dense(256, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(256, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation="softmax")
    ])
    # Compilation and overview of the model
    model.compile(
        optimizer="adam",
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    print(model.summary())
