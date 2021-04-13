import tensorflow as tf


# tf.concat
# tf.split
# tf.stack
# tf.unstack

def test_concat():
    t1 = [[1, 2, 3], [4, 5, 6]]
    t2 = [[7, 8, 9], [10, 11, 12]]
    v = tf.concat([t1, t2], 0)  # 沿着第一个维度合并，即最外层维度
    assert v.shape == (4, 3)
    tf.assert_equal(v, tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
