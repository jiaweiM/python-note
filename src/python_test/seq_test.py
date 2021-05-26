def test_concatenate():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b
    assert c == [1, 2, 3, 4, 5, 6]
