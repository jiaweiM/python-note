import numpy as np


def test_dtype():
    a = np.array([2, 3, 4], dtype=np.uint32)
    b = np.array([5, 6, 7], dtype=np.uint32)
    c_unsigned32 = a - b
    print(c_unsigned32)
