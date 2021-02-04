def test_list():
    """
    对 tuple 和 sets 功能类似
    """
    l = [1, 3, 4, 5]
    assert all(l)

    l.append('')
    assert not all(l)

    # all values false
    l = [0, False]
    assert not all(l)

    # one false value
    l = [1, 3, 4, 0]
    assert not all(l)

    # one true value
    l = [0, False, 5]
    assert not all(l)

    # empty iterable
    assert all([])


def test_tuple():
    t = ('Tuple')
    assert all(t)
    t1 = ('Tuple', '')
    assert not all(t1)


# 只要不是 null，都是True
def test_string():
    s = "This is good"
    assert all(s)

    # 0 if False
    # '0' is True
    s = '000'
    assert all(s)

    s = ''
    assert all(s)


# 所有的键值都为 True，或者为 empty，才返回 True
def test_dict():
    s = {0: 'False', 1: 'False'}
    assert not all(s)

    s = {1: 'True', 2: 'True'}
    assert all(s)

    s = {1: 'True', False: 0}
    assert not all(s)

    s = {}
    assert all(s)

    # 0 is False
    # '0' is True
    s = {'0': 'True'}
    assert all(s)


def test_bool():
    assert all([True, 1, {3}])
    assert not all([True, 1, {}])
    assert any([True, 1, {}])
    assert all([])
    assert not any([])
