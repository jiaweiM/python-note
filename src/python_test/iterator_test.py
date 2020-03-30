import pytest


def test_it():
    a_list = [4, 6, 8, 9]
    a_it = iter(a_list)  # 调用 a_list.__iter__()
    assert next(a_it) == 4  # 调用 a_list.__next__()
    assert next(a_it) == 6
    assert a_it.__next__() == 8
    assert a_it.__next__() == 9

    for a in a_it:
        print(a)

    with pytest.raises(StopIteration):
        next(a_it)


class PowTwo:
    """Class to implement on iterator of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


def test_for():
    a = PowTwo(3)
    for val in a:
        print(val)


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


def test_node():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
    # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)