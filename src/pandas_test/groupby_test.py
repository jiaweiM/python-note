import numpy as np
import pandas as pd


def test_group_type():
    df = pd.read_csv(r'src/pandas_test/data.csv')
    grouped = df.groupby("Gender")


def test_create_group():
    df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                       ('bird', 'Psittaciformes', 24.0),
                       ('mammal', 'Carnivora', 80.2),
                       ('mammal', 'Primates', np.nan),
                       ('mammal', 'Carnivora', 58)],
                      index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                      columns=('class', 'order', 'max_speed'))
    grouped = df.groupby('class')


def test_create_group2():
    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8),
                       'D': np.random.randn(8)})


def test_select():
    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                             'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8),
                       'D': np.random.randn(8)})
    grouped = df.groupby('A')
    group = grouped.get_group('bar')
    group.size
    print(type(group))
    assert group.size() == 3
    print(group)
