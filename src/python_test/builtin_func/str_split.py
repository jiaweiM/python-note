def test_split():
    """
    默认分隔符为空格
    """
    s = "a b c d"
    ss = s.split()
    assert ss == ['a', 'b', 'c', 'd']


def test_split_max():
    # 设置最多只拆分前两个单词
    s = "a b c d"
    ss = s.split(maxsplit=2)
    assert ss == ['a', 'b', 'c d']


def test_split_comma():
    s = 'a,b c,d'
    ss = s.split(',')
    assert ss == ['a', 'b c', 'd']
