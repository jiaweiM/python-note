import numpy as np


def test():
    x = np.array([1, 2, 2.5])
    y = x.astype(int)
    np.testing.assert_array_equal(y, [1, 2, 2])
