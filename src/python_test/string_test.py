import pytest


def test_concanate():
    '''使用加号连接字符串，称为字符串拼接'''
    first_name = 'zhang'
    last_name = 'chen'
    full_name = first_name + " " + last_name
    assert full_name == 'zhang chen'


def test_rstrip():
    '''移除字符串后面的空白'''
    lang = ' python '
    assert lang.rstrip() == ' python'


def test_lstrip():
    '''移除字符串前面的空白'''
    lang = ' python '
    assert lang.lstrip() == 'python '


def test_strip():
    '''移除字符串前后的空白'''
    lang = ' python '
    assert lang.strip() == 'python'


def test_multi():
    a = 'm'
    b = a * 3
    assert b == 'mmm'


def test_array_opt():
    a = 'hello world'
    assert a[0] == 'h'
    assert a[2:5] == 'llo'
    assert a[-1] == 'd'
    assert a[6:] == 'world'
    assert a[-3:] == 'rld'
    assert a[:-3] == 'hello wo'


def test_format():
    age = 20
    name = 'Swaroop'
    print("{0} was {1} years old when he wrote this book".format(name, age))
    print("Why is {0} playing with that python?".format(name))


def test_format_2():
    # 对于浮点数 '0.333' 保留小数点后三位
    print("{0:.3f}".format(1.0 / 3))
    # 使用下划线填充文本，并保持文字处于中间位置
    # 使用（＾）　定义'__hello__' 字符串长度为11
    print('{0:_^11}'.format('hello'))
    # 基于关键词输出 'Swaroop wrote A Byte of Python'
    print('{name} wrote {book}'.format(
        name='Swaroop', book='A Byte of Python'))


'''创建字符串，可以用单引号，双引号，甚至三引号
三引号一般用于多行字符串和 docstrings.
'''


def test_create():
    my_str = 'Hello'
    print(my_str)
    my_str = "Hello"
    print(my_str)
    my_str = """Hello, welcome to
                the world of Python"""
    print(my_str)


def test_replace():
    oldstring = 'I like Python'
    newstring = oldstring.replace('like', 'love')
    print(oldstring)
    print(newstring)


def test_reverse():
    a = 'test'
    b = ''.join(reversed(a))
    assert b == 'tset'


def test_slice():
    '''
    使用 index 访问单个字符串
    使用 slicing 访问成片字符串
    如果超出范围，抛出 IndexError
    如果索引不为整数，抛出 TypeError
    '''
    str = 'programiz'
    print('str = ', str)

    # 第一个字符
    assert str[0] == 'p'

    # 最后一个字符
    assert str[-1] == 'z'

    # 2-5 字符
    assert str[1:5] == "rogr"

    # 6th-倒数第二
    assert str[5:-2] == 'am'

    with pytest.raises(IndexError):
        str[15]

    with pytest.raises(TypeError):
        str[1.5]


def test_upper_lower():
    '''大小写操作'''
    a = "lower"
    assert a.upper() == "LOWER"
    name = 'Zhang Chen'
    assert name.lower() == 'zhang chen'


def test_title():
    """title() 以首字母大写的方式显示每个单词"""
    name = "zhang chen"
    assert name.title() == 'Zhang Chen'


def test_modify():
    '''
    String 是 immutable的，所以不能修改，只能重复赋值.
    不能从 string 中删除字符，但可以删除整个字符串。
    '''
    my_str = 'programiz'

    with pytest.raises(TypeError):
        my_str[5] = 'a'

    # 不能从字符串中删除字符
    # 但是可以删除整个字符串
    del my_str
    with pytest.raises(NameError):
        print(my_str)


def test_capitalize():
    a = "python name"
    assert a.capitalize() == 'Python name'


def test_concat():
    str1 = 'Hello'
    str2 = 'World!'

    # using +
    assert str1 + str2 == "HelloWorld!"

    # using *
    assert str1 * 3 == "HelloHelloHello"


def test_iterate():
    count = 0
    for letter in 'Hello World':
        if letter == 'l':
            count += 1
    assert count == 3


def test_in():
    assert 'a' in 'program'
    assert 'at' in 'battle'
    assert 'file' not in 'windows'


def test_join():
    a = ':'
    b = a.join("Hello")
    assert b == 'H:e:l:l:o'


# -*- coding: utf-8 -*-

"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
objects, 待输出的对象
sep, 值之前的分隔符，默认为空格
end, 所有值输出后，默认添加的内容，默认为换行
file, 默认输出位置

input("") 命令行输入
"""


def test_string_format():
    x = 5
    y = 10
    print('The value of x is {} and y is {}'.format(x, y))


def test_string_format_order():
    print('I love {0} and {1}'.format('bread', 'butter'))
    # Output: I love bread and butter

    print('I love {1} and {0}'.format('bread', 'butter'))
    # Output: I love butter and bread


def test_string_format_keyword():
    print('Hello {name}, {greeting}'.format(
        greeting='Goodmorning', name='John'))


def test_string_format_printf():
    x = 12.3456789
    print('The value of x is %3.2f' % x)
    print('The value of x is %3.4f' % x)
