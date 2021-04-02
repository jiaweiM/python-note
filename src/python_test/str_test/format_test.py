import math
import datetime


def test():
    name = "Peter"
    age = 23

    assert "%s is %d years old" % (name, age) == "Peter is 23 years old"
    assert '{} is {} years old'.format(name, age) == "Peter is 23 years old"
    assert f'{name} is {age} years old' == "Peter is 23 years old"


def test_fstring():
    bags = 3
    apples_in_bag = 12
    assert f'There are total of {bags * apples_in_bag} apples' == "There are total of 36 apples"


def test_fstring_dict():
    user = {'name': 'Lilei', 'occupation': 'gardener'}
    assert f"{user['name']} is a {user['occupation']}" == "Lilei is a gardener"


def test_math():
    x = 0.8
    print(f"{math.cos(x) = }")
    print(f"{math.sin(x) = }")


def test_multiline():
    name = "Lilei"
    age = 32
    occupation = 'gardener'
    msg = (
        f'Name: {name}\n'
        f'Age: {age}\n'
        f'Occupation: {occupation}'
    )
    print(msg)


def my_max(x, y):
    return x if x > y else y


def test_fstring_func():
    a = 3
    b = 4
    print(f'Max of {a} and {b} is {my_max(a, b)}')


class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __repr__(self):
        return f"{self.name} is a {self.occupation}"


def test_fstring_obj():
    u = User('Lilei', 'gardener')
    print(f'{u}')


def test_fstring_escape():
    print(f"Python uses {{}} to evaluate a variables in f-strings")
    print(f'This was a \'great\' file')


def test_fstring_date():
    now = datetime.datetime.now()
    print(f'{now:%Y-%m-%d %H:%M}')


def test_fstring_float():
    val = 12.3
    print(f'{val:.2f}')
    print(f'{val:.5f}')


def test_fstring_width():
    for x in range(1, 11):
        print(f'{x:02} {x * x:3} {x * x * x:4}')


def test_fstring_justify():
    s1 = 'a'
    s2 = 'ab'
    s3 = 'abc'
    s4 = 'abcd'
    print(f'{s1:>10}')
    print(f'{s2:>10}')
    print(f'{s3:>10}')
    print(f'{s4:>10}')


def test_fstring_numeric():
    a = 300
    # hex
    print(f'{a:x}')
    # octal
    print(f'{a:o}')
    # scientific
    print(f'{a:e}')