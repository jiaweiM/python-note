def test_list():
    '''空 list，或其中全是 0 或 False，返回 False'''
    lst = ['', 0, False, 0.0, None]
    assert not any(lst)

    l = [1, 3, 4, 0]
    assert any(l)

    l = [0, False]
    assert not any(l)

    l = [0, False, 5]
    assert any(l)

    assert not any([])


# 只有空 string 返回 False
def test_string():
    s = "This is good"
    assert any(s)

    # 0 is False
    # '0' is True
    s = '000'
    assert any(s)

    s = ''
    assert not any(s)


# 如果所有的键值为 False，则返回 False.
def test_dict():
    d = {0: 'False'}
    assert not any(d)

    d = {0: 'False', 1: 'True'}
    assert any(d)

    d = {0: 'False', False: 0}
    assert not any(d)

    assert not any({})

    # 0 is False
    # '0' is True
    d = {'0': 'False'}
    assert any(d)
