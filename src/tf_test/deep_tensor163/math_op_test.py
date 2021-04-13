import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def test_math():
    b = tf.fill([2, 2], 2.0)
    a = tf.ones([2, 2])
    tf.assert_equal(a + b, tf.constant([[3., 3.], [3., 3.]]))
    tf.assert_equal(a - b, tf.constant([[-1., -1.], [-1., -1.]]))
    tf.assert_equal(a * b, tf.constant([[2., 2.], [2., 2.]]))
    tf.assert_equal(a / b, tf.constant([[0.5, 0.5], [0.5, 0.5]]))

