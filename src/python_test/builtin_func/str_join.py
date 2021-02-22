def test_join():
    ss = ["a", 'b', 'c']
    s = ','.join(ss)
    assert s == 'a,b,c'
