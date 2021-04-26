import tensorflow as tf
import numpy as np


def test_constant():
    a = tf.constant([1, 2, 3, 4, 5, 6])
    assert a.dtype == tf.int32
    a = tf.constant(np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64))
    assert a.dtype == tf.int64


def test_fill():
    t = tf.fill([2, 3], 9)
    tf.assert_equal(t, tf.constant([[9, 9, 9], [9, 9, 9]]))
    print(t)
