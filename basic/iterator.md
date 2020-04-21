# Iterator

- [Iterator](#iterator)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [for 循环](#for-%e5%be%aa%e7%8e%af)
  - [自定义迭代器](#%e8%87%aa%e5%ae%9a%e4%b9%89%e8%bf%ad%e4%bb%a3%e5%99%a8)
    - [无限迭代](#%e6%97%a0%e9%99%90%e8%bf%ad%e4%bb%a3)
    - [生成器](#%e7%94%9f%e6%88%90%e5%99%a8)
  - [手动遍历迭代器](#%e6%89%8b%e5%8a%a8%e9%81%8d%e5%8e%86%e8%bf%ad%e4%bb%a3%e5%99%a8)
  - [代理迭代](#%e4%bb%a3%e7%90%86%e8%bf%ad%e4%bb%a3)
  - [反向迭代](#%e5%8f%8d%e5%90%91%e8%bf%ad%e4%bb%a3)
  - [带索引迭代](#%e5%b8%a6%e7%b4%a2%e5%bc%95%e8%bf%ad%e4%bb%a3)

2020-04-20, 21:58
***

## 简介

迭代器是对集合进行迭代的对象，在 Python 中应用十分广泛。

定义迭代器需要实现两个方法，`__iter__()` 和 `__next__()`。

大多数内置容器，如 `list`, `tuple`, `string` 等都实现了迭代器。例如：

```py
import pytest

def test_it():
    a_list = [4, 6, 8, 9]
    a_it = iter(a_list)
    assert next(a_it) == 4
    assert next(a_it) == 6
    assert a_it.__next__() == 8
    assert a_it.__next__() == 9

    with pytest.raises(StopIteration):
        next(a_it)
```

通过 `next()` 或者 `.__next__()` 都可以获得下一个元素，到末尾继续调用，会抛出 `StopIteration` 异常。

不过迭代器一般在 for 循环中使用：

```py
for element in my_list:
    print(element)
```

## for 循环

对任何可迭代的对象，都可以使用 for 循环枚举其元素，for 循环的内部实现：

```py
# create an iterator object from that iterable
iter_obj = iter(iterable)
# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
```

在 for 循环中，先通过 `iter()` 获得对象的迭代器，然后通过 `while` 语句迭代对象，直至结尾抛出异常，退出循环。

## 自定义迭代器

自定义迭代器很容易，只需要实现 `__iter__()` 和 `__next__()` 方法。

- `__iter__()` 方法返回迭代器对象本身
- `__next__()` 方法返回序列中下一个元素，到结尾抛出 `StopIteration`

如下实现了一个 2 的次方的迭代器：

```py
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
```

然后可以直接通过 for 循环获得值：

```py
a = PowTwo(3)
for val in a:
    print(val)
```

输出：

```cmd
1
2
4
8
```

### 无限迭代

无法迭代器没有提供终止条件，就会一直迭代下去，例如：

```py
class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
```

对这种无限迭代，只能靠自己手动终止。

迭代器的优点之一是节省资源。

### 生成器

在一个对象上实现迭代最简单的方式是使用生成器函数。例如，`Node` 表示树形数据结构，实现一个深度优先方式遍历树形节点的生成器。

```py
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
```

`depth_first()` 直观的展示了生成器的使用方式。它首先返回自身，然后迭代每个子节点，通过调用子节点的 `depth_first()` 方法返回对应元素。

## 手动遍历迭代器

不用 for 循环遍历迭代器。

为了手动遍历可迭代对象，使用 `next()` 函数并在代码中捕获 `StopIteration` 异常。例如，下面手动读取一个文件中的所有行：

```py
def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass
```

通常用 `StopIteration` 指示迭代的结尾。但也可以通过返回一个指定值来标记结尾，比如 `None` 。例如：

```py
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
```

## 代理迭代

你构建了一个自定义容器对象，里面包含有列表、元组或其它可迭代对象。 你想直接在这个新容器对象上执行迭代操作。

此时可以使用代理迭代，只需要定义一个 `__iter__()` 方法，将迭代操作代理到容器内部的对象上去。比如：

```py
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

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)
```

在上面代码中， `__iter__()` 方法只是简单的将迭代请求传递给内部的 `_children` 属性。

Python 的迭代器协议需要 `__iter__()` 方法返回一个实现了 `__next__()` 方法的迭代器对象。如果你只是迭代遍历其它容器的内容，则无需操心底层实现，只需要传递迭代请求即可。

这里的 `iter()` 函数的使用简化了代码， `iter(s)` 只是简单的通过调用 `s.__iter__()` 方法来返回对应的迭代器对象，就跟 `len(s)` 会调用 `s.__len__()` 原理是一样的。

## 反向迭代

使用内置函数 `reversed()` 实现反向迭代。

例如：

```py
>>> a = [1, 2, 3, 4]
>>> for x in reversed(a):
...     print(x)
...
4
3
2
1
```

反向迭代只能应用于序列，即实现 `__len__()` 和 `__getitem__()` 方法的对象，或实现 `__reversed__()` 的方法。

在自定义类上实现 `__reversed__()` 方法可以实现反向迭代，比如：

```py
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)
```

定义反向迭代器在需要反向迭代时，使代码更为高效，而不需要将数据填充到一个列表中，然后再反向迭代列表。

## 带索引迭代

内置的 `enumerate()` 函数提供带索引迭代功能：

```

```