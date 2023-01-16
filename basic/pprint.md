# pprint

- [pprint](#pprint)
  - [简介](#简介)
  - [Printing](#printing)
  - [Formatting](#formatting)
  - [自定义类](#自定义类)
  - [递归](#递归)
  - [嵌套限制](#嵌套限制)
  - [设置输出宽度](#设置输出宽度)
  - [参考](#参考)

***

## 简介

`pprint` (pretty printer) 用于生成数据结构的美观视图，功能与 `print` 类似。

## Printing

使用 `pprint` 模块的最简单方式：直接调用其 `pprint()` 函数。

`pprint()` 格式化对象，并将其作为参数传入数据流，默认为 `sys.stdout`。

```python
from pprint import pprint

data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't''u', 'v', 'x', 'y', 'z']),
]

print('PRINT:')
print(data)
print()
print("PPRINT:")
pprint(data)
```

```txt
PRINT:
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}), (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}), (3, ['m', 'n']), (4, ['o', 'p', 'q']), (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]

PPRINT:
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']),
 (4, ['o', 'p', 'q']),
 (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]
```

## Formatting

生成数据结构的格式化表示，但不直接写入流（例如，写入日志），可以使用 `pformat()` 函数。

```python
import logging
from pprint import pformat

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s'
)

logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())
```

```txt
DEBUG    Logging pformatted data
DEBUG    [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
DEBUG     (2,
DEBUG      {'e': 'E',
DEBUG       'f': 'F',
DEBUG       'g': 'G',
DEBUG       'h': 'H',
DEBUG       'i': 'I',
DEBUG       'j': 'J',
DEBUG       'k': 'K',
DEBUG       'l': 'L'}),
DEBUG     (3, ['m', 'n']),
DEBUG     (4, ['o', 'p', 'q']),
DEBUG     (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]
```

## 自定义类

`pprint()` 内部使用 `PrettyPrinter` 类格式化对象，该类支持自定义类，只需要实现 `__repr__()` 方法。

```python
class node:
    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents

    def __repr__(self):
        return ('node(' + repr(self.name) + ', ' +
                repr(self.contents) + ')')

trees = [
    node('node-1'),
    node('node-2', [node('node-2-1')]),
    node('node-3', [node('node-3-1')])
]
pprint(trees)
```

```txt
[node('node-1', []),
 node('node-2', [node('node-2-1', [])]),
 node('node-3', [node('node-3-1', [])])]
```

可以看到，`PrettyPrinter` 自动处理了上面的嵌套结构。

## 递归

对递归数据结构，`pprint` 以格式 `<Recursion on typename with id=number>` 引用递归对象。例如：

```python
local_data = ['a', 'b', 1, 2]
local_data.append(local_data)

print('id(local_data) =>', id(local_data))
pprint(local_data)
```

```txt
id(local_data) => 2192471192576
['a', 'b', 1, 2, <Recursion on list with id=2192471192576>]
```

## 嵌套限制

对非常深的数据结构，可以使用 `depth` 设置对嵌套数据结构的递归深度，输出中未包含的级别用省略号表示：

```python
pprint(data, depth=1) # 深度 1，下一级 tuple 内容全部用省略号
pprint(data, depth=2)
```

```txt
[(...), (...), (...), (...), (...)]
[(1, {...}), (2, {...}), (3, [...]), (4, [...]), (5, [...])]
```

## 设置输出宽度

格式化文本的默认宽度为 80，可以使用 `width` 参数调整宽度：

```python
for width in [80, 5]:
    print('WIDTH =', width)
    pprint(data, width=width)
    print()
```

```txt
WIDTH = 80
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']),
 (4, ['o', 'p', 'q']),
 (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]

WIDTH = 5
[(1,
  {'a': 'A',
   'b': 'B',
   'c': 'C',
   'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3,
  ['m',
   'n']),
 (4,
  ['o',
   'p',
   'q']),
 (5,
  ['r',
   's',
   'tu',
   'v',
   'x',
   'y',
   'z'])]
```

`compact` 参数表示在每一行尽可能容纳更多数据：

```python
print('DEFAULT:')
pprint(data, compact=False)
print('\nCOMPACT:')
pprint(data, compact=True)
```

```txt
DEFAULT:
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']),
 (4, ['o', 'p', 'q']),
 (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]

COMPACT:
[(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'}),
 (3, ['m', 'n']), (4, ['o', 'p', 'q']),
 (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]
```

## 参考

- https://docs.python.org/3/library/pprint.html