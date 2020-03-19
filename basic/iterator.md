# Iterator

- [Iterator](#iterator)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [for 循环](#for-%e5%be%aa%e7%8e%af)
  - [自定义迭代器](#%e8%87%aa%e5%ae%9a%e4%b9%89%e8%bf%ad%e4%bb%a3%e5%99%a8)
    - [无限迭代](#%e6%97%a0%e9%99%90%e8%bf%ad%e4%bb%a3)

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

不同对迭代器，一般在 for 循环中使用，即：

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
