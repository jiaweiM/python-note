import pytest


def test_unpacking():
    a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert a == 1
    assert b == 2
    assert d == 9
    assert c == [3, 4, 5, 6, 7, 8]


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
