import tensorflow as tf


def test_tile():
    a = tf.constant([[1, 2, 3], [4, 5, 6]], tf.int32)
    b = tf.constant([1, 2], tf.int32)

    v = tf.tile(a, b)
    tf.assert_equal(v, tf.constant([[1, 2, 3, 1, 2, 3], [4, 5, 6, 4, 5, 6]], tf.int32))

    c = tf.constant([2, 1], tf.int32)
    v = tf.tile(a, c)
    tf.assert_equal(v, tf.constant([[1, 2, 3], [4, 5, 6],
                                    [1, 2, 3], [4, 5, 6]]))

    d = tf.constant([2, 2], tf.int32)
    v = tf.tile(a, d)
    tf.assert_equal(v, tf.constant([[1, 2, 3, 1, 2, 3],
                                    [4, 5, 6, 4, 5, 6],
                                    [1, 2, 3, 1, 2, 3],
                                    [4, 5, 6, 4, 5, 6]]))

