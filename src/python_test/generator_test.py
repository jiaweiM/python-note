import pytest


def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1


def my_gen():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


def test_gen():
    a = my_gen()
    n = next(a)
    assert n == 1
    n = next(a)
    assert n == 2
    n = next(a)
    assert n == 3
    with pytest.raises(StopIteration):
        next(a)


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
