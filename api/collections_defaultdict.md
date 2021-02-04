# defaultdict

- [defaultdict](#defaultdict)
  - [简介](#简介)
    - [`__missing__(key)`](#__missing__key)
    - [`default_factory`](#default_factory)
  - [list as default_factory](#list-as-default_factory)
  - [int as default_factory](#int-as-default_factory)
  - [lambda as default_factory](#lambda-as-default_factory)
  - [set as default_factory](#set-as-default_factory)

***

## 简介

[`collections.defaultdict([default_factory[,...]])`](https://docs.python.org/3/library/collections.html#collections.defaultdict)

`defaultdict` 是内置 `dict` 的子类，覆盖了 `__missing__(key)` 方法，添加了一个可写入的实例变量，余下功能和 `dict` 完全一样。即 `defaultdict` 提供了设置默认值的方法。

第一个参数为 `default_factory` 属性值，默认为 `None`；余下参数和 `dict` 一样。

除了 `dict` 支持的标准方法，`defaultdict` 扩展方法：

### `__missing__(key)`

如果 `default_factory` 为 `None`，则调用该方法抛出 `KeyError`。

如果 `default_factory` 不为 `None`，不用参数调用返回默认值，该值和 `key` 作为一对键值对插入到字典，并返回该值。

如果调用 `default_factory` 时抛出异常，这个异常会传递给外层。

当对应的 key 没有找到，`__getitem__()` 调用 `__missing__(key)` 方法，并直接返回 `__missing__(key)` 返回的值或者抛出 `__missing__(key)` 抛出的异常。

`__missing__()` 不会被 `__getitem__()` 以外的方法调用。所以 `get()` 方法和常规的字典返回一样，默认返回 `None`，而不是使用 `default_factory`。

### `default_factory`

该属性由 `__missing__()` 使用。构造对象时由第一个参数提供，否则为 `None`。

## list as default_factory

使用 `list` 作为 `default_factory`，将`键-值`转换为`键-列表`字典。

```py
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)  # 必须通过 [] 访问
assert list(d) == ['yellow', 'blue', 'red']
assert d['yellow'] == [1, 3]
assert d['blue'] == [2, 4]
assert d['red'] == [1]
```

当第一次遇到某个 key，由于它不在 dict，所以其值使用 `default_factory` 自动生成，此处为空的 `list`。`list.append()` 添加值到新创建的 list。

当再次遇到某个 key，查询正常执行，返回 key 对应的 list，然后 `list.append()` 将另一个值添加到 list。该技术和 `dict.setdefault()`等效，而且更简单、高效。下面是等价的 `setdefault` 实现：

```py
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
assert list(d) == ['yellow', 'blue', 'red']
```

## int as default_factory

将 `default_factory` 设置为 `int` 可用于计数。

```py
>>> s = 'mississippi'
>>> d = defaultdict(int)
>>> for k in s:
    d[k] += 1
>>> sorted(d.items())
[('i', 4), ('m', 1), ('p', 2), ('s', 4)]
```

首次碰到某个字符串，由于 dict 中没有该值，由 `default_factory` 调用 `int()` 提供默认值，即默认0。`+=` 操作实现了所有计数。

## lambda as default_factory

上例返回 0 的`int()` 是常量函数的特例。

创建常量函数更快速、更灵活的方式是使用 lambda 函数。例如：

```py
def constant_factory(value):
    return lambda: value

d = defaultdict(constant_factory('<DAO>'))
assert d['a'] == "<DAO>"
```

## set as default_factory

```py
>>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
>>> d = defaultdict(set)
>>> for k, v in s:
      d[k].add(v)

>>> sorted(d.items())
[('blue', {2, 4}), ('red', {1, 3})]
```
