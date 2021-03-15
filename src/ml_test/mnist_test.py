import tensorflow as tf
import matplotlib.pyplot as plt


def test_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    assert x_train.shape == (60000, 28, 28)
    assert y_train.shape == (60000,)

    assert x_test.shape == (10000, 28, 28)
    assert y_test.shape == (10000,)


def test_show_img():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    assert y_test[0] == 7
    plt.imshow(x_test[0])
    plt.show()
