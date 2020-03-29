class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


def test_repr():
    p = Pair(3, 4)
    assert p.__repr__() == 'Pair(3, 4)'


def test_str():
    p = Pair(3, 4)
    assert str(p) == '(3, 4)'
