import tensorflow as tf


def test_stack():
    x = tf.constant([1, 4])
    y = tf.constant([2, 5])
    z = tf.constant([3, 6])
    v = tf.stack([x, y, z])
    tf.assert_equal(v, tf.constant([[1, 4], [2, 5], [3, 6]]))

    v1 = tf.stack([x, y, z], axis=1)
    tf.assert_equal(v1, tf.constant([[1, 2, 3], [4, 5, 6]]))
