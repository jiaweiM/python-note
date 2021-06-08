from collections import namedtuple


def test_simple():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, y=22)  # 可以使用位置参数或关键字参数
    assert p[0] + p[1] == 33

    x, y = p
    assert x == 11
    assert y == 22
