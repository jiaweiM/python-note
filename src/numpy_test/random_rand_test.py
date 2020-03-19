import numpy as np


def test_rand():
    values = np.random.rand(3, 2)
    assert values.shape == (3, 2)
    print(values)