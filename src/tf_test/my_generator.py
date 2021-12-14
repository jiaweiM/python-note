import numpy as np


def my_generator(my_array):
    i = 0
    while True:
        yield my_array[i:i + 2, :]  # output two elements at a time
        i += 1


test_array = np.array([[10.0, 2.0],
                       [15, 6.0],
                       [3.2, -1.5],
                       [-3, -2]], np.float32)
output = my_generator(test_array)
print(next(output))
