"""
sorted 返回一个新的 list
"""


def test_int_list():
    x = [4, 1, 2, 3]
    y = sorted(x)
    assert y == [1, 2, 3, 4]
    assert x == [4, 1, 2, 3]


def test_reverse():
    x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # sort the list by absolute value from largest to smallest
    assert x == [-4, 3, -2, 1]


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


def test_custom_key():
    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return 'User({})'.format(self.user_id)

    users = [User(3), User(1), User(9)]
    sorted_users = sorted(users, key=lambda u: u.user_id)
    assert sorted_users[0].user_id == 1
    assert sorted_users[1].user_id == 3
    assert sorted_users[2].user_id == 9
