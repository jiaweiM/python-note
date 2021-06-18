import pytest
from unicodedata import name


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


def test_ctr():
    myset = {1, 2, 3}

    print(myset)


def test_union():
    a = {1, 2, 3}
    b = {2, 3, 4}
    c = a.union(b)

    print(c)
    print(a)
    print(b)


def test_comps():
    s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}  # 把编码 32~255 之间的字符名字里有 “SIGN” 单词挑出来
    print(s)
