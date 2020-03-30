# list 有 sort() 方法，效果和 sorted() 类似，差别是，不返回值，而是排序原始 list
# 元音字母排序


def test_list():
    # vowels list
    py_list = ['e', 'a', 'u', 'o', 'i']
    sorted_list = sorted(py_list)
    assert sorted_list == ['a', 'e', 'i', 'o', 'u']


# 字符串的字母排序
def test_string():
    # string
    py_string = 'Python'
    assert sorted(py_string) == ['P', 'h', 'n', 'o', 't', 'y']


# tuple 排序
def test_tuple():
    # vowels tuple
    py_tuple = ('e', 'a', 'u', 'o', 'i')
    assert sorted(py_tuple) == ['a', 'e', 'i', 'o', 'u']


# 降序排序
def test_descending():
    # set
    py_set = {'e', 'a', 'u', 'o', 'i'}
    assert sorted(py_set, reverse=True) == ['u', 'o', 'i', 'e', 'a']

    # dictionary
    py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
    assert sorted(py_dict, reverse=True) == ['u', 'o', 'i', 'e', 'a']

    # frozen set
    py_f_set = frozenset(('e', 'a', 'u', 'o', 'i'))
    assert sorted(py_f_set, reverse=True) == ['u', 'o', 'i', 'e', 'a']


# take second element for sort
def take_second(elem):
    return elem[1]


# 自定义排序
def test_custom():
    # random list
    random = [(2, 2), (3, 4), (4, 1), (1, 3)]

    # sort list with key
    sorted_list = sorted(random, key=take_second)

    assert sorted_list == [(4, 1), (2, 2), (1, 3), (3, 4)]
