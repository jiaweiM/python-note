import pytest


def test_raise_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_excep_info():
    with pytest.raises(RuntimeError) as expInfo:
        def f():
            f()

        f()
    assert "maximum recursion" in str(expInfo.value)


def f():
    raise SystemExit(1)


def test_mytest():
    '''抛出指定错误'''
    with pytest.raises(SystemExit):
        f()
