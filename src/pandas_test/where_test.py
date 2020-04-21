import pandas as pd
import numpy as np


def test_series():
    s = pd.Series(range(5))
    s1 = s.where(s > 0)
    assert pd.isnull(s1.iloc[0])
    assert np.isnan(s1.iloc[0])
