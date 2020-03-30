def test_str():
    seq = 'Python'
    a = list(reversed(seq))
    assert a == ['n', 'o', 'h', 't', 'y', 'P']


def test_tuple():
    seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
    a = list(reversed(seq_tuple))
    assert a == ['n', 'o', 'h', 't', 'y', 'P']


class Vowerls:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)


def test_object():
    v = Vowerls()
    a = list(reversed(v))
    assert a == ['u', 'o', 'i', 'e', 'a']
