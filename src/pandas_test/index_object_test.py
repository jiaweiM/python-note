import pandas as pd


def test_create():
    index = pd.Index(['e', 'd', 'a', 'b'])
    assert type(index) == pd.Index
    assert index.dtype == object
    assert 'd' in index


def test_name():
    index = pd.Index(['e', 'd', 'a', 'b'], name='something')
    assert index.name == 'something'


def test_metadata():
    ind = pd.Index([1, 2, 3])
    ind2 = ind.rename("apple")
    assert ind2.name == 'apple'
    ind.set_names(['apple'], inplace=True)
    assert ind.name == 'apple'
    ind.name = 'bob'
    assert ind.name == 'bob'


def test_level():
    idx = pd.MultiIndex.from_product(
        [range(3), ['one', 'two']], names=['first', 'second'])
    assert type(idx.levels[1]) == pd.Index
    assert idx.levels[1].name == 'second'
