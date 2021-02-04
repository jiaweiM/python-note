from functools import partial


def exp(base, power):
    return base ** power


def test_partial():
    two_to_the = partial(exp, 2)
    assert two_to_the(3) == 8


def test_partial2():
    square_of = partial(exp, power=2)
    assert square_of(3) == 9


def double(x):
    return 2 * x


def test_map():
    xs = [1, 2, 3, 4]
    twice_xs = [double(x) for x in xs]
    assert twice_xs == [2, 4, 6, 8]
    assert list(map(double, xs)) == [2, 4, 6, 8]  # same as above
    list_doubler = partial(map, double)  # function that doubles a list
    assert list(list_doubler(xs)) == [2, 4, 6, 8]
