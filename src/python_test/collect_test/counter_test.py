from collections import Counter


def test_count():
    c = Counter()  # a new, empty counter
    c = Counter('gallahad')  # a new counter from an iterable
    c = Counter({'red': 4, 'blue': 2})  # a new counter from a mapping
    c = Counter(cats=4, dogs=8)  # a new counter from keyword args


def test_zero():
    c = Counter(['eggs', 'ham'])
    assert c['bacon'] == 0


def test_elements():
    c = Counter(a=4, b=2, c=0, d=-2)
    assert sorted(c.elements()) == ['a', 'a', 'a', 'a', 'b', 'b']


def test_most_common():
    c = Counter('abracadabra')
    l = c.most_common(3)
    assert l == [('a', 5), ('b', 2), ('r', 2)]


def test_subtract():
    c = Counter(a=4, b=2, c=0, d=-2)
    d = Counter(a=1, b=2, c=3, d=4)
    c.subtract(d)
    assert c['a'] == 3
    assert c['b'] == 0
    assert c['c'] == -3
    assert c['d'] == -6


def test_common_usage():
    pass


def test_count_words():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    word_counts = Counter(words)
    # 出现频率最高的三个单词
    top3 = word_counts.most_common(3)
    assert top3 == [('eyes', 8), ('the', 5), ('look', 4)]


def test_add():
    c = Counter('abbb') + Counter('bcc')
    assert c == Counter({'b': 4, 'c': 2, 'a': 1})
