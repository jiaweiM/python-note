import pandas as pd
import pytest
import numpy as np


@pytest.fixture
def simple_frame():
    df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
    return df


def test_func(simple_frame):
    new_frame = simple_frame.apply(np.sqrt)
    print(new_frame)
