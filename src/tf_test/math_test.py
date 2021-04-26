import numpy as np
import tensorflow as tf


def test_log():
    x = tf.constant([0, 0.5, 1, 5])
    y = tf.math.log(x)
    print(y)


def test_reduce_sum():
    # x 的 shape 为 （2, 3）
    x = tf.constant([[1, 1, 1], [1, 1, 1]])

    # 不指定 axis，计算所有元素加和
    v = tf.reduce_sum(x).numpy()
    assert v == 6

    # 指定 axis=0，[1, 1, 1] + [1, 1, 1] = [2, 2, 2]
    v = tf.reduce_sum(x, 0).numpy()
    assert np.array_equal(v, np.array([2, 2, 2]))

    # 指定 axis=1, [1, 1] + [1, 1] + [1, 1] = [3, 3]
    v = tf.reduce_sum(x, 1).numpy()
    assert np.array_equal(v, np.array([3, 3]))

    # 保留维度
    v = tf.reduce_sum(x, 1, keepdims=True).numpy()
    assert np.array_equal(v, np.array([[3], [3]]))

    # 从两个维度同时 reduce
    # [1,1,1]+[1,1,1]=[2,2,2]
    # 2+2+2=6
    v = tf.reduce_sum(x, [0, 1]).numpy()
    assert v == 6
