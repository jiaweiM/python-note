def test_one_param():
    number_list = [1, 2]
    assert type(number_list) == list
    number_dict = {1: 'one', 2: 'two'}
    assert type(number_dict) == dict

    assert type([]) is list
    assert type(()) is tuple
    assert type({}) is dict

    class Foo:
        a = 0

    foo = Foo()
    assert type(foo) == Foo


def test_class():
    class Shape():
        pass

    class Circle(Shape):
        pass

    assert type(Shape()) == Shape
    assert not (type(Circle()) == Shape)
    assert isinstance(Circle(), Shape)
