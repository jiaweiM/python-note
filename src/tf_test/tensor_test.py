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


def test_zeros():
    t = tf.zeros([3, 4], tf.int32)
    tf.assert_equal(t, tf.constant([[0, 0, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]], dtype=tf.int32))


def test_zeros_like():
    tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
    t = tf.zeros_like(tensor)
    tf.assert_equal(t, tf.constant([[0, 0, 0], [0, 0, 0]]))


def test_zeros_like_dtype():
    tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
    t = tf.zeros_like(tensor, dtype=tf.float32)
    tf.assert_equal(t, tf.constant([[0, 0, 0], [0, 0, 0]], tf.float32))


def test_zeros_array():
    t = tf.zeros_like([[1, 2, 3], [4, 5, 6]])
    tf.assert_equal(t, tf.constant([[0, 0, 0], [0, 0, 0]]))


def test_linspace():
    t = tf.linspace(10.0, 12.0, 3, name="linspace")
    tf.assert_equal(t, tf.constant([10., 11., 12.]))


def test_linspace_tensor():
    t = tf.linspace([0., 5.], [10., 40.], 5, axis=0)
    tf.assert_equal(t, tf.constant([[0., 5.],
                                    [2.5, 13.75],
                                    [5., 22.5],
                                    [7.5, 31.25],
                                    [10., 40.]]))


def test_linspace_axis1():
    t = tf.linspace([0., 5.], [10., 40.], 5, axis=-1)
    tf.assert_equal(t, tf.constant([[0., 2.5, 5., 7.5, 10.],
                                    [5., 13.75, 22.5, 31.25, 40.]]))


def test_range():
    t = tf.range(3, 18, 3)
    tf.assert_equal(t, tf.constant([3, 6, 9, 12, 15]))


def test_range_delta():
    t = tf.range(start=3, limit=1, delta=-0.5)
    tf.assert_equal(t, tf.constant([3., 2.5, 2., 1.5]))


def test_range_limit():
    t = tf.range(5)
    tf.assert_equal(t, tf.constant([0, 1, 2, 3, 4]))
