import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal


def test():
    movie = pd.read_csv('data/movie.csv', index_col='movie_title')
    # 挑选时长超多 2 小时的电影
    movie_2_hours = movie['duration'] > 120
    # 查看这些电影的个数，因为 True 等价为 1，所以可以通过该方式计算
    assert movie_2_hours.sum() == 1039


def test_items():
    df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                      index=['mouse', 'rabbit'],
                      columns=['one', 'two', 'three'])
    df1 = df.filter(items=['one', 'three'])
    assert_frame_equal(df1, pd.DataFrame(np.array(([1, 3], [4, 6])),
                                         index=['mouse', 'rabbit'],
                                         columns=['one', 'three']))
