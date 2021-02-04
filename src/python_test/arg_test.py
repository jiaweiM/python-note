def doubler(f):
    def g(x):
        return 2 * f(x)

    return g


def f1(x):
    return x + 1


def test_double():
    g = doubler(f1)
    assert g(3) == 8
    assert g(-1) == 0
