def square(x):
    return x ** 2


def test_map():
    val = map(square, [1, 2, 3])
    assert list(val) == [1, 4, 9]


def plus(a, b):
    return a + b


def test_map_2():
    val = map(plus, [1, 2, 3], [4, 5, 6])
    assert list(val) == [5, 7, 9]


def multiply(x, y): return x * y


def test_multiple_argument():
    products = list(map(multiply, [1, 2], [4, 5]))
    assert products == [4, 10]
