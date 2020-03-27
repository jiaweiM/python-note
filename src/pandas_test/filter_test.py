import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal


def test_items():
    df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                      index=['mouse', 'rabbit'],
                      columns=['one', 'two', 'three'])
    df1 = df.filter(items=['one', 'three'])
    assert_frame_equal(df1, pd.DataFrame(np.array(([1, 3], [4, 6])),
                                         index=['mouse', 'rabbit'],
                                         columns=['one', 'three']))
