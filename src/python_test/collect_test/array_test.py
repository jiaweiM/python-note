import array as arr


def test_ctr():
    a = arr.array('d', [1.1, 3.5, 4.5])
    assert a.typecode == 'd'
    print(a)
