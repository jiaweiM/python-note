import pytest
import pandas as pd

# def test_sum():
sf = pd.Series([1, 1, 2, 3, 3, 3])
grouped = sf.groupby(sf).filter(lambda x: x.sum() > 2)
print(grouped)
