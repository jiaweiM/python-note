import numpy as np


def test():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.reshape(a, 6)
    assert b == np.array([1, 2, 3, 4, 5, 6])


def test_order_f():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.reshape(a, 6, order='F')
    assert b == np.array([1, 4, 2, 5, 3, 6])


def test_auto():
    a = np.array([[1, 2, 3], [4, 5, 6]])