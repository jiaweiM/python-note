
def test_zip():
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']
    zipped = zip(numbers, letters)
    zips = list(zipped)
    assert zips[0] == (1, 'a')
    assert zips[1] == (2, 'b')
    assert zips[2] == (3, 'c')


def test_zip_set():
    s1 = {2, 3, 1}
    s2 = {'b', 'a', 'c'}
    l1 = list(zip(s1, s2))
    print(l1)


def test_no_argument():
    zipped = zip()
    l = list(zipped)
    assert l == []


def test_one_argument():
    a = [1, 2, 3]
    zipped = zip(a)
    l = list(zipped)
    assert l[0] == (1,)
    assert l[1] == (2,)
    assert l[2] == (3,)


def test_unequal_len():
    l = list(zip(range(3), range(100)))
    assert len(l) == 3
    assert l[0] == (0, 0)
    assert l[1] == (1, 1)
    assert l[2] == (2, 2)


def test_unzip():
    pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    numbers, letters = zip(*pairs)
    assert numbers == (1, 2, 3, 4)
    assert letters == ('a', 'b', 'c', 'd')
