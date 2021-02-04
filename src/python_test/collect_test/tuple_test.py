import pytest


def test_modify():
    a_list = [1, 2]
    a_tuple = (1, 2)
    b_tuple = 3, 4
    a_list[1] = 3
    try:
        a_tuple[1] = 3
    except TypeError:
        print("cannot modify a tuple")


def test_swap():
    x, y = 1, 2
    x, y, = y, x
    assert x == 2
    assert y == 1


def test_unpacking():
    a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert a == 1
    assert b == 2
    assert d == 9
    assert c == [3, 4, 5, 6, 7, 8]


def test_unpack():
    p = (4, 5)
    x, y = p
    assert x == 4
    assert y == 5


def test_unpack_str():
    s = 'hello'
    a, b, c, d, e = s
    assert a == 'h'
    assert b == 'e'
    assert c == 'l'
    assert d == 'l'
    assert e == 'o'


def test_unpack_long():
    records = [('foo', 1, 2),
               ('bar', 'hello'),
               ('foo', 3, 4), ]


def test_ctr():
    # 我会推荐你总是使用括号,来指明元组的开始与结束
    # 尽管括号是一个可选选项。
    # 明了胜过晦涩，显式优于隐式。
    zoo = ('python', 'elephant', 'penguin')
    print('Number of animals in the zoo is', len(zoo))
    new_zoo = 'monkey', 'camel', zoo
    print('Number of cages in the new zoo is', len(new_zoo))
    print('All animals in new zoo are', new_zoo)
    print('Animals brought from old zoo are', new_zoo[2])
    print('Last animal brought from old zoo is', new_zoo[2][2])
    print('Number of animals in the new zoo is',
          len(new_zoo) - 1 + len(new_zoo[2]))


def test_ctr2():
    a = (1,)
    assert type(a) == tuple


def test_compare():
    a = (5, 6)
    b = (1, 4)
    assert (a > b == True)
