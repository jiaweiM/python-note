def test_view():
    random_byte_array = bytearray('ABC', 'utf-8')
    mv = memoryview(random_byte_array)

    assert mv[0] == 65
    assert bytes(mv[0:2]) == b'AB'
    assert list(mv[0:3]) == [65, 66, 67]


def test_modify():
    random_byte_array = bytearray('ABC', 'utf-8')
    assert bytes(random_byte_array) == b'ABC'

    mv = memoryview(random_byte_array)
    mv[1] = 90  # 对应字母 Z
    assert bytes(random_byte_array) == b'AZC'
    print(bytes(random_byte_array))
