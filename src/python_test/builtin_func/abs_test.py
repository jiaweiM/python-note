def test_num():
    integer = -20
    assert abs(integer) == 20

    floating = - 30.33
    assert abs(floating) == 30.33


# 返回的是复数的模
def test_complex():
    complex = (3 - 4j)
    assert abs(complex) == 5
