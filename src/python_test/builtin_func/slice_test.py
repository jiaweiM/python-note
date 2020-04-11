def test_slice():
    # (0, 1, 2)
    a = slice(3)
    assert a.start is None
    assert a.step is None
    assert a.stop == 3


def test_name():
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    assert items[a] == [2, 3]


def test_indices():
    s = 'HelloWorld'
    a = slice(5, 50, 2)
    b = a.indices(len(s))
    assert b == (5, 10, 2)
