import pytest


def test_empty():
    """stop 值为0，返回空序列"""
    seq = list(range(0))
    assert len(seq) == 0


def test_stop():
    """[0,10)"""
    seq = list(range(10))
    assert len(seq) == 10
    assert seq == list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def test_start_stop():
    """[1,10)"""
    seq = list(range(1, 10))
    assert len(seq) == 9
    assert seq == list([1, 2, 3, 4, 5, 6, 7, 8, 9])


def test_step():
    seq = list(range(2, 14, 2))
    assert len(seq) == 6
    assert seq == list([2, 4, 6, 8, 10, 12])


def test_step_zero():
    with pytest.raises(ValueError):
        range(1, 10, 0)


def test_step_negative():
    seq = list(range(0, -10, -1))
    assert seq == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
