from collections import OrderedDict


def test_order():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['span'] = 3
    d['grok'] = 4
    assert list(d) == ['foo', 'bar', 'span', 'grok']
