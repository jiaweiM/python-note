import pytest
from pytest import approx


def test_simple():
    assert 0.1 + 0.2 == approx(0.3)


def test_seq():
    assert (0.1 + 0.2, 0.2 + 0.4) == approx((0.3, 0.6))


def test_dict():
    assert {'a': 0.1 + 0.2, 'b': 0.2 + 0.4} == approx({'a': 0.3, 'b': 0.6})


def test_precision():
    assert 1.0001 == approx(1, rel=1e-3)
    assert 1.0001 == approx(1, abs=1e-3)
    assert 1 + 1e-8 == approx(1, rel=1e-6, abs=1e-12)
