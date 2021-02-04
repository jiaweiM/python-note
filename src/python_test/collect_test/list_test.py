import pytest


def test_raw():
    xs = [3, 1, 2]  # Create a list
    assert str(xs) == '[3, 1, 2]'
    assert xs[2] == 2
    # Negative indices count from the end of the list; prints "2"
    assert xs[-1] == 2
    xs[2] = 'foo'  # Lists can contain elements of different types
    assert xs[2] == 'foo'
    xs.append('bar')  # Add a new element to the end of the list
    assert xs == [3, 1, 'foo', 'bar']
    x = xs.pop()  # Remove and return the last element of the list
    assert x == 'bar'
    assert xs == [3, 1, 'foo']


def test_slice():
    '''
    通过 [start:end] 切片 list
    '''
    nums = list(range(5))  # range is a built-in function that creates a list of integers
    assert nums == [0, 1, 2, 3, 4]
    assert nums[2:4] == [2, 3]  # Get a slice from index 2 to 4
    assert nums[2:] == [2, 3, 4]
    # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
    assert nums[:2] == [0, 1]
    assert nums[:] == [0, 1, 2, 3, 4]  # Get a slice of the whole list
    print(nums[:-1])  # Slice indices can be negative; prints "[0, 1, 2, 3]"
    nums[2:4] = [8, 9]  # Assign a new sublist to a slice
    print(nums)  # Prints "[0, 1, 8, 9, 4]"

    my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
    # elements 3rd to 5th
    assert my_list[2:5] == ['o', 'g', 'r']

    # elements beginning to 4th
    assert my_list[:-5] == ['p', 'r', 'o', 'g']

    # elements 6th to end
    assert my_list[5:] == ['a', 'm', 'i', 'z']

    # elements beginning to end
    assert my_list[:] == ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']


def test_len():
    """
    获得列表的长度
    """
    animals = ['cat', 'dog', 'monkey']
    assert len(animals) == 3


def test_loop():
    animals = ['cat', 'dog', 'monkey']
    for animal in animals:
        print(animal)
        # Prints "cat", "dog", "monkey", each on its own line.


def test_demo_1():
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    assert len(shoplist) == 4

    print('These items are:', end=' ')
    for item in shoplist:
        print(item, end=' ')

    print('\nI also have to bur rice.')
    shoplist.append('rice')
    print('My shopping list is now', shoplist)

    print('I will sort my list now')
    shoplist.sort()
    print('Sorted shopping list is', shoplist)

    print('The first item I will buy is', shoplist[0])
    olditem = shoplist[0]
    del shoplist[0]
    print('I bought the', olditem)
    print('My shopping list is now', shoplist)


def test_demo_2():
    movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
    movies.insert(1, 1975)
    movies.insert(3, 1979)
    movies.insert(5, 1983)
    print(movies)


def test_ctr():
    '''定义 list.将元素放在 [] 中，以逗号分隔'''

    my_list = []

    # list of integers
    my_list = [1, 2, 3]

    # list with mixed datatypes
    my_list = [1, 'Hello', 3.4]

    # a list can even have another list as an item. This is called nested list.
    my_list = ["mouse", [8, 4, 6], ['a']]


'''
访问 List中 元素的方法有多种
1. 通过 List Index 访问
通过 [] 访问，从0开始。
超过范围，抛出 IndexError。
索引必须为整数，否则抛出 TypeError
Nested list 通过 nested indexing 访问
'''


def test_get_index():
    my_list = ['p', 'r', 'o', 'b', 'e']
    assert my_list[0] == 'p'
    assert my_list[2] == 'o'
    assert my_list[4] == 'e'

    with pytest.raises(TypeError):
        my_list[4.0]

    # Nested list
    n_list = ['Happy', [2, 0, 1, 5]]

    # nested indexing
    assert n_list[0][1] == 'a'
    assert n_list[1][3] == 5


def test_get_index_negative():
    '''-1 表示最后一个'''
    my_list = ['p', 'r', 'o', 'b', 'e']
    assert my_list[-1] == 'e'
    assert my_list[-5] == 'p'


'''
List are mutable, 即可以动态修改其值，不像 string 和 tuple，是不能修改的。
'''


def test_modify():
    odd = [2, 4, 6, 8]

    # 修改第1个值
    odd[0] = 1
    assert odd == [1, 4, 6, 8]

    # 修改 [2,4] 的值
    odd[1:4] = [3, 5, 7]
    assert odd == [1, 3, 5, 7]


def test_append_element():
    # animal list
    animal = ['cat', 'dog', 'rabbit']

    # an element is added
    animal.append('guinea pig')

    assert animal == ['cat', 'dog', 'rabbit', 'guinea pig']


def test_append_list():
    # animal list
    animal = ['cat', 'dog', 'rabbit']

    # another list of wild animals
    wild_animal = ['tiger', 'fox']

    # adding wild_animal list to animal list
    animal.append(wild_animal)

    assert animal == ['cat', 'dog', 'rabbit', ['tiger', 'fox']]


def test_comprehension():
    even_numbers = [x for x in range(5) if x % 2 == 0]
    assert even_numbers == [0, 2, 4]
    squares = [x * x for x in range(5)]
    assert squares == [0, 1, 4, 9, 16]


def test_comprehension_dict():
    square_dict = {x: x * x for x in range(5)}
    assert square_dict == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    square_set = {x * x for x in [1, -1]}
    assert square_set == {1}


def test_comprehension_pair():
    pairs = [(x, y) for x in range(10)
             for y in range(10)]


    '''
    The extend() extends the list by adding all items of a list (passed as an argument) to the end.
    将 tuple 或 set 作为参数：
    
    list.extend(list(tuple_type))
    or
    list.extend(tuple_type)
    
    修改原始 list，不返回任何值
    '''

    def test_extend_list():
        # language list
        language = ['French', 'English', 'German']

        # another list of language
        language1 = ['Spanish', 'Portuguese']

        language.extend(language1)

        assert language == ['French', 'English', 'German', 'Spanish', 'Portuguese']

    def test_extend_integer():
        x = [1, 2, 3]
        x.extend([4, 5, 6])
        assert x == [1, 2, 3, 4, 5, 6]

    def test_concatenate():
        x = [1, 2, 3]
        y = x + [4, 5, 6]
        assert y == [1, 2, 3, 4, 5, 6]

    def test_extend_tuple_set():
        # language list
        language = ['French', 'English', 'German']

        # language tuple
        language_tuple = ('Spanish', 'Portuguese')

        # language set
        language_set = {'Chinese', 'Japanese'}

        # appending element of language tuple
        language.extend(language_tuple)
        assert language == ['French', 'English', 'German', 'Spanish', 'Portuguese']

        # appending element of language set
        language.extend(language_set)
        assert len(language) == 7

    def test_append2():
        odd = [1, 3, 5]
        odd.append(7)
        assert odd == [1, 3, 5, 7]

        odd.extend([9, 11, 13])
        assert odd == [1, 3, 5, 7, 9, 11, 13]

    def test_plus():
        odd = [1, 3, 5]
        new_odd = odd + [9, 7, 5]
        assert new_odd == [1, 3, 5, 9, 7, 5]

        a = [1, 2]
        a += [3, 4]
        assert a == [1, 2, 3, 4]

    def test_multiply():
        assert ["re"] * 3 == ["re", "re", "re"]

    def test_insert():
        '''
        insert(index, element), 在指定位置插入元素，后面的元素依次后移
        [2:2], 通过这种空的 slice 可以一次插入多个元素
        '''
        odd = [1, 9]

        odd.insert(1, 3)
        assert odd == [1, 3, 9]

        odd[2:2] = [5, 7]
        assert odd == [1, 3, 5, 7, 9]

    def test_insert_tuple():
        mixed_list = [{1, 2}, [5, 6, 7]]

        number_tuple = (3, 4)
        mixed_list.insert(1, number_tuple)

        assert mixed_list == [{1, 2}, (3, 4), [5, 6, 7]]

    def test_del():
        '''
        通过 del 关键字删除 list的元素
        '''
        my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

        # 删除一个
        del my_list[2]
        assert ['p', 'r', 'b', 'l', 'e', 'm'] == my_list

        # 删除多个
        del my_list[1:5]
        assert ['p', 'm'] == my_list

        # 删除整个 list
        del my_list
        # assert my_list == None

    '''
    remove() 从 list 中删除指定值，不过只删除一个
    pop() 删除指定位置的值，如果不提供参数，返回并删除最后的值
    clear() 清空 list
    '''

    def test_remove():
        '''
        The remove() method searches for the given element in the list and removes the first matching element.
        list.remove(element)

        如果 list 中不存在 element，抛出 ValueError
        不返回任何值。
        '''
        my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
        my_list.remove('p')
        assert my_list == ['r', 'o', 'b', 'l', 'e', 'm']

        # animal list 包含重复值，只移除第一个
        animal = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

        # 'dog' element is removed
        animal.remove('dog')
        assert animal == ['cat', 'dog', 'guinea pig', 'dog']

        # 移除不存在的值
        with pytest.raises(ValueError):
            animal.remove('fish')

        val = my_list.pop(1)
        assert val == 'o'
        assert my_list == ['r', 'b', 'l', 'e', 'm']

        val = my_list.pop()
        assert val == 'm'
        assert my_list == ['r', 'b', 'l', 'e']

        my_list.clear()
        assert my_list == []

    def test_index():
        # vowels list
        vowels = ['a', 'e', 'i', 'o', 'i', 'u']

        # element 'e' is searched
        index = vowels.index('e')
        assert index == 1

        # element 'i' is searched
        index = vowels.index('i')
        assert index == 2

        assert vowels.index('o') == 3

        # 不存在，抛出 ValueError
        with pytest.raises(ValueError):
            vowels.index('p')

    '''
    在 list 中查找 tuple 或 list
    '''

    def test_index_tuple():
        # random list
        random = ['a', ('a', 'b'), [3, 4]]

        # element ('a', 'b') is searched
        index = random.index(('a', 'b'))
        assert index == 1

        # element [3, 4] is searched
        index = random.index([3, 4])
        assert index == 2

    def test_count():
        # vowels list
        vowels = ['a', 'e', 'i', 'o', 'i', 'u']

        # count element 'i'
        count = vowels.count('i')
        assert count == 2

        # count element 'p'
        count = vowels.count('p')
        assert count == 0

    def test_count_tuple():
        # random list
        random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

        # count element ('a', 'b')
        count = random.count(('a', 'b'))
        assert count == 2

        # count element [3, 4]
        count = random.count([3, 4])
        assert count == 1

    def test_pop():
        '''
        list.pop(index=-1)
        移除并返回指定位置的元素
        如果 index 不在 list 范围，抛出 IndexError
        index 默认为-1，即移除并返回最后一个元素。
        '''
        # programming language list
        language = ['Python', 'Java', 'C++', 'French', 'C']

        # Return value from pop()
        # When 3 is passed
        return_value = language.pop(3)
        assert return_value == 'French'
        assert language == ['Python', 'Java', 'C++', 'C']

        # programming language list
        language = ['Python', 'Java', 'C++', 'Ruby', 'C']
        assert language.pop() == 'C'
        assert language == ['Python', 'Java', 'C++', 'Ruby']

        assert language.pop(-1) == 'Ruby'
        assert language == ['Python', 'Java', 'C++']

        assert language.pop(-3) == 'Python'
        assert language == ['Java', 'C++']

    def test_reverse():
        # Operating System List
        os = ['Windows', 'macOS', 'Linux']
        # List Reverse
        os.reverse()
        assert os == ['Linux', 'macOS', 'Windows']

    '''
    通过 slice 也可以实现倒序操作
    '''

    def test_reverse_slicing():
        # Operating System List
        os = ['Windows', 'macOS', 'Linux']

        # Reversing a list
        # Syntax: reversed_list = os[start:stop:step]
        reversed_list = os[::-1]
        assert reversed_list == ['Linux', 'macOS', 'Windows']

    '''
    如果要倒着迭代 list 中的元素，使用
    reversed() 更好
    '''

    def test_reverse_reversed():
        # Operating System List
        os = ['Windows', 'macOS', 'Linux']

        # Printing Elements in Reversed Order
        for o in reversed(os):
            print(o)

    def test_sort():
        cars = ['bmw', 'audi', 'toyota', 'subaru']
        cars.sort()
        assert cars == ['audi', 'bmw', 'subaru', 'toyota']

        cars.sort(reverse=True)
        assert cars == ['toyota', 'subaru', 'bmw', 'audi']

    def test_sorted():
        '''sorted() 函数生成一个新的列表，不影响原列表'''
        cars = ['bmw', 'audi', 'toyota', 'subaru']

        sorted_cars = sorted(cars)
        assert sorted_cars == ['audi', 'bmw', 'subaru', 'toyota']

        sorted_cars = sorted(cars, reverse=True)
        assert sorted_cars == ['toyota', 'subaru', 'bmw', 'audi']

    def test_parse():
        squares = [value ** 2 for value in range(5)]
        assert squares == [0, 1, 4, 9, 16]

    def test_stack():
        stack = [3, 4, 5]
        stack.append(6)
        stack.append(7)
        assert stack.pop() == 7
        assert stack.pop() == 6
        assert stack.pop() == 5

    def test_unpack():
        x, y = [1, 2]
        assert x == 1
        assert y == 2

    def test_unpack2():
        _, y = [1, 2]
        assert y == 2
