import pytest

'''
序列：列表、元组、字符串
具有切片运算
'''


def test_demo_1():
    shoplist = ['applet', 'mango', 'carrot', 'banana']
    name = 'swaroop'

    # Indexing or 'subscription' operation
    print('Item 0 is', shoplist[0])
    print('Item 1 is', shoplist[1])
    print('Item 2 is', shoplist[2])
    print('Item 3 is', shoplist[3])
    print('Item -1 is', shoplist[-1])
    print('Item -2 is', shoplist[-2])
    print('Character 0 is', name[0])

    # Slicing on a list
    print('Item 1 to 3 is', shoplist[1:3])
    print('Item 2 to end is', shoplist[2:])
    print('Item 1 to -1 is', shoplist[1:-1])
    print('Item start to end is', shoplist[:])

    # slicing on a string
    print('characters 1 to 3 is', name[1:3])
    print('characters 2 to end is', name[2:])
    print('characters 1 to -1 is', name[1:-1])
    print('characters start to end is', name[:])


def test_gen():
    symbols = '$¢£¥€¤'
    t = tuple(ord(symbol) for symbol in symbols)
    assert t == (36, 162, 163, 165, 8364, 164)

    import array
    a = array.array('I', (ord(symbol) for symbol in symbols))
    assert a == array.array("I", [36, 162, 163, 165, 8364, 164])


def test_unpack():
    p = divmod(20, 8)
    assert p == (2, 4)

    t = (20, 8)
    assert (2, 4) == divmod(*t)


def test_nested_unpack():
    values = ('Lili', 'Shenzhen', 32, (4, 5))
    name, region, age, (x, y) = values
    assert (x, y) == (4, 5)


def test_slice_assign():
    l = list(range(10))
    assert l == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    l[2:5] = [20, 30]
    assert l == [0, 1, 20, 30, 5, 6, 7, 8, 9]

    del l[5:7]
    assert l == [0, 1, 20, 30, 5, 8, 9]

    l[3::2] = [11, 22]
    assert l == [0, 1, 20, 11, 5, 22, 9]

    with pytest.raises(TypeError):
        l[2:5] = 100

    l[2:5] = [100]
    assert l == [0, 1, 100, 22, 9]


def test_add():
    board = [['_'] * 3 for _ in range(3)]
    assert board == [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    board[1][2] = 'X'
    assert board == [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

    weird_board = [['_'] * 3] * 3
    assert weird_board == [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    weird_board[1][2] = 'O'
    assert weird_board == [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]


def test_sort():
    fruits = ['grape', 'raspberry', 'apple', 'banana']

    a = sorted(fruits)  # 默认排序，不跪改变原列表
    assert a == ['apple', 'banana', 'grape', 'raspberry']

    a = sorted(fruits, key=len)  # 按长度排序
    assert a == ['grape', 'apple', 'banana', 'raspberry']

    a = sorted(fruits, key=len, reverse=True)  # 按长度降序
    assert a == ['raspberry', 'banana', 'grape', 'apple']

    # 以上排序都不会修改原列表
    assert fruits == ['grape', 'raspberry', 'apple', 'banana']

    fruits.sort()  # list.sort() 为原位排序
    assert fruits == ['apple', 'banana', 'grape', 'raspberry']
