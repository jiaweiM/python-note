# defaultdict

- [defaultdict](#defaultdict)
  - [简介](#%e7%ae%80%e4%bb%8b)
    - [`__missing__(key)`](#missingkey)
    - [`default_factory`](#defaultfactory)
  - [list as default_factory](#list-as-defaultfactory)
  - [int as default_factory](#int-as-defaultfactory)

***

## 简介

`collections.defaultdict([default_factory[,...]])`

`defaultdict` 是内置 `dict` 的子类，覆盖了一个方法，添加了一个可写入实例变量，余下功能和 `dict` 完全一样。

第一个参数提供 `default_factory` 属性值，默认为 `None`，余下参数和 `dict` 一样。

除了 `dict` 支持的标准方法，`defaultdict` 扩展方法：

### `__missing__(key)`

如果 `default_factory` 为 `None`，则调用该方法抛出 `KeyError`。

如果 `default_factory` 不为 `None`，不用参数调用为 `key` 提供默认值，这个值和 `key` 作为一对键值对插入到字典，并作为本方法的返回值返回。

如果调用 `default_factory` 时抛出异常，这个异常会传递给外层。

当对应的 key 没有找到，`__getitem__()` 调用该方法，无论本方法返回了值还是抛出了异常，都会被 `__getitem__()` 直接返回或抛出。

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

当第一次遇到某个 key，由于它不在 dict，所以其值使用 `default_factory` 自动生成，此处为空的 `list`。`list.append()` 加值添加到新创建的 list。

当再次遇到某个 key，查询正常执行，返回 key 对应的 list，然后 `list.append()` 将另一个值添加到 list。该技术和 `dict.setdefault()`等效，而且更简单、更快。下面是等价的 `setdefault` 实现：

```py
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
assert list(d) == ['yellow', 'blue', 'red']
```

## int as default_factory

将 `default_factory` 设置为 `int` 可以用于计数。
