from itertools import zip_longest


def test_len3():
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']
    longest = range(5)
    zipped = zip_longest(numbers, letters, longest, fillvalue='?')
    l = list(zipped)
    assert len(l) == 5
    assert l[3] == ('?', '?', 3)
