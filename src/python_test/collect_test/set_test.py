import pytest
from unicodedata import name


def test():
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7, 8}

    assert len(a) == 5


def test_creat():
    # 相同类型
    my_set = {1, 2, 3}

    # 混合类型
    my_set = {1.0, 'Hello', (1, 2, 3)}
    print(my_set)


def test_add():
    s = set()
    s.add(1)
    s.add(2)
    s.add(2)
    assert len(s) == 2
    assert 2 in s
    assert 3 not in s


def test_add2():
    s = {1, 2, 3}
    s.add(4)
    assert len(s) == 4
    assert 4 in s


def test_copy():
    a = {1, 2, 3}
    b = a.copy()
    assert b == {1, 2, 3}


def test_ctr():
    myset = {1, 2, 3}

    print(myset)


def test_union():
    a = {1, 2, 3}
    b = {2, 3, 4}
    c = a.union(b)

    assert c == {1, 2, 3, 4}


def test_intersection():
    a = {1, 2, 3}
    b = {2, 3, 4}
    c = a.intersection(b)
    assert c == {2, 3}


def test_intersection_update():
    a = {1, 2, 3}
    b = {2, 3, 4}
    a.intersection_update(b)
    assert a == {2, 3}


def test_isdisjoint():
    a = {1, 2, 3}
    b = {3, 4, 5}
    c = {4, 5, 6}
    assert not a.isdisjoint(b)
    assert a.isdisjoint(c)


def test_subset():
    a = {1, 2, 3}
    b = {1, 2, 3}
    assert a.issubset(b)

    assert not a < b
    c = {1, 2, 3, 4}
    assert a < c


def test_superset():
    a = {1, 2, 3}
    b = {1, 2}
    assert a.issuperset(b)


def test_comps():
    s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}  # 把编码 32~255 之间的字符名字里有 “SIGN” 单词挑出来
    print(s)


def test_update():
    a = {1, 2, 3}
    b = {3, 4, 5, 6}
    a.update(b)
    assert a == {1, 2, 3, 4, 5, 6}


def test_remove():
    a = {1, 2, 3}
    a.remove(2)
    assert a == {1, 3}
    with pytest.raises(KeyError):
        a.remove(4)  # 没有 4，所以抛出 KeyError


def test_discard():
    a = {1, 2, 3}
    a.discard(2)
    assert a == {1, 3}
    a.discard(4)
    assert a == {1, 3}


def test_pop():
    a = {1, 2, 3}
    x = a.pop()
    assert x not in a
    assert len(a) == 2


def test_clear():
    a = {1, 2, 3}
    a.clear()
    assert len(a) == 0


def test_del():
    a = {1, 2, 3}
    del a
    with pytest.raises(UnboundLocalError):
        print(a)
