def test_bool():
    x = None
    assert x == None
    assert x is None


def test_false():
    assert not False
    assert not None
    assert not []
    assert not {}
    assert not ""
    assert not set()
    assert not 0
    assert not 0.0
