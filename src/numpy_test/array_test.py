import numpy as np


def test_dot():
    a = [[1, 0], [0, 1]]
    b = [[4, 1], [2, 2]]
    c = np.dot(a, b)
    np.testing.assert_array_equal(c, np.array([[4, 1], [2, 2]]))


def test_dot1():
    c = np.dot(4, 5)
    assert c == 20


def test_dot_d1():
    c = np.dot([1, 2], [3, 4])
    assert c == 11


def test_multiple():
    assert np.multiply(2.0, 4.0) == 8.0


def test_multiple_2():
    x1 = np.arange(9.0).reshape((3, 3))
    x2 = np.arange(3.0)
    c = np.multiply(x1, x2)
    np.testing.assert_array_equal(c, np.array([[0, 1, 4],
                                               [0, 4, 10],
                                               [0, 7, 16]]))


def test_linspace():
    array = np.linspace(1., 4., 6)
    print(array)
