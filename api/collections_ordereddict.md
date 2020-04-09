# collections.OrderedDict

- [collections.OrderedDict](#collectionsordereddict)
  - [简介](#%e7%ae%80%e4%bb%8b)
    - [popitem](#popitem)
    - [move_to_end](#movetoend)
    - [性质](#%e6%80%a7%e8%b4%a8)
  - [实例](#%e5%ae%9e%e4%be%8b)
    - [key 按照插入顺序存储](#key-%e6%8c%89%e7%85%a7%e6%8f%92%e5%85%a5%e9%a1%ba%e5%ba%8f%e5%ad%98%e5%82%a8)
    - [实现类似 functools.lru_cache()](#%e5%ae%9e%e7%8e%b0%e7%b1%bb%e4%bc%bc-functoolslrucache)

## 简介

`class collections.OrderedDict([items])`

`dict` 子类，添加了排序相关的方法，在迭代操作时保持元素被插入时的顺序。例如：

```py
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
```

### popitem

`popitem(last=True)`

`popitem()` 方法从有序字典中返回并删除一个 `(key, value)`。

- 如果 `last=True`，则按照 LIFO 顺序返回
- 否则按照 FIFO 顺序返回

### move_to_end

`move_to_end(key, last=True)`

将已有的 `key` 移到有序字典的末尾。

- 如果 `last=True`，将其移到最右
- 如果 `last=True`，将其移到最左
- 如果不存在 `key`，抛出 `KeyError`

例如：

```py
>>> d = OrderedDict.fromkeys('abcde')
>>> d.move_to_end('b')
>>> ''.join(d.keys())
'acdeb'
>>> d.move_to_end('b', last=False)
>>> ''.join(d.keys())
'bacde'
```

### 性质

除了映射方法，有序字典支持 `reversed()` 反向迭代。

equal 测试：

- `OrderedDict` 之间equal 测试顺序敏感，通过 `list(od1.items())==list(od2.items())` 实现。
- `OrderedDict` 和其它 `Mapping` 对象的 equal 测试顺序不敏感，和常规 dict 一样。

如果你想要构建一个将来需要序列化或编码成其它格式的映射时，`OrderedDict` 非常有用。

`OrderedDict` 内部维护着一个根据键插入顺序排序的双向链表。每次插入新元素，它会放到链表尾部，对于一个已存在的键重新赋值，不会改变键的顺序。

需要注意的是，一个 `OrderedDict` 的大小是一个普通字典的两倍，因为它内部维护着一个链表。所以如果你要构建一个需要大量 `OrderedDict` 实例的数据结构时，要仔细权衡使用 `OrderedDict` 带来的好处是否大过额外的内存消耗的影响。

## 实例

### key 按照插入顺序存储

通过扩展 `OrderedDict`，很容易让所有的 key 按照插入的顺序排序。如果插入一个已有的 entry，其位置被移到末尾：

```py
class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
```

### 实现类似 functools.lru_cache()

```py
class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
```
