import numpy as np


def test_rand():
    values = np.random.rand(3, 2)
    assert values.shape == (3, 2)
    print(values)


def test_permutation():
    rng = np.random.default_rng()
    a1 = rng.permutation(10)
    print(a1)

    a2 = rng.permutation([1, 4, 9, 12, 15])
    print(a2)


def test_permutation_multiple():
    rng = np.random.default_rng()
    arr = np.arange(9).reshape((3, 3))
    print(arr)
    a3 = rng.permutation(arr)
    print(a3)


def test_permutation_multiple2():
    rng = np.random.default_rng()
    arr = np.arange(9).reshape((3, 3))
    print(arr)
    a3 = rng.permutation(arr, axis=1)
    print(a3)
