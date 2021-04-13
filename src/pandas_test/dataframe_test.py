import random

import numpy as np
import pandas as pd


def test_create():
    dates = pd.date_range("20190101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    assert df.size == 24


def test_create_col3():
    df = pd.DataFrame({
        "Name": ["Braund, Mr. Owen Harris",
                 "Allen, Mr. William Henry",
                 "Bonnell, Miss. Elizabeth"],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"]
    })
    print(df)


def test_series_size():
    s = pd.Series({'a': 1, 'b': 2, 'c': 3})
    assert s.size == 3


def test_dataframe_size():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    assert df.size == 4


def test_shape():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    assert df.shape == (2, 2)
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4], "col3": [5, 6]})
    assert df.shape == (2, 3)


def test_sort_values():
    df = pd.DataFrame({
        'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
        'col2': [2, 1, 9, 8, 7, 4],
        'col3': [0, 1, 9, 4, 2, 3]
    })
    df1 = df.sort_values(by=['col1'])

    print(df)
    print(df1)


def test_map():
    def sub_str(file_name):
        id = file_name.rfind(".")
        if id > 0:
            return file_name[: id]
        else:
            return file_name

    df = pd.DataFrame(
        {
            'col1': ['File', "File.b", "File.c.d"],
            'col2': [2, 1, 9]
        }
    )
    df.loc[:, 'File'] = df.loc[:, 'col1'].map(sub_str)
    print(df.loc[:, 'File'])


def test_iter():
    df = pd.DataFrame({"col1": np.random.randn(3), "col2": np.random.randn(3)}, index=["a", "b", "c"])
    for col in df:
        print(col)


def test_demo():
    year_index = {'Year': [y for y in range(2010, 2031)],
                  'Random': [random.random() for _ in range(21)]}
    df = pd.DataFrame(year_index)
    print(df)


def test_add_column():
    df = pd.DataFrame({
        'a': [1, 2],
        'b': [3, 4]
    })
    df['c'] = df.apply(lambda row: row.a + row.b, axis=1)
    print(df)


def extract_city_name(df):
    """
    Chicago, IL -> Chicago for city_name column
    """
    df["city_name"] = df["city_and_code"].str.split(",").str.get(0)
    return df


def add_country_name(df, country_name=None):
    """
    Chicago -> Chicago-US for city_name column
    """
    col = "city_name"
    df["city_and_country"] = df[col] + country_name


def test_tablewise():
    df_p = pd.DataFrame({"city_and_code": ["Chicago, IL"]})
    add_country_name(extract_city_name(df_p), country_name="US")
    print(df_p)


def test_tablewise2():
    df_p = pd.DataFrame({"city_and_code": ["Chicago, IL"]})
    df_p.pipe(extract_city_name).pipe(add_country_name, country_name="US")
    print(df_p)
