# Tuple

- [Tuple](#tuple)
  - [简介](#简介)
  - [创建 tuple](#创建-tuple)
  - [访问值](#访问值)
  - [作为 dict 的 key](#作为-dict-的-key)

2020-04-21, 11:32
***

## 简介

Python Tuple 和 list 十分类似，但是不能修改。tuple 是不可变的 list。

所以，使用 tuple 更安全，因此，建议能使用 tuple 的地方，应该尽量使用 tuple。

- Tuple 比 list快，如果不修改内容，使用 Tuple 更好；
- Tuple 可以作为字典的 key值，因为它不可修改，List 则不可以。

尝试修改 Tuple 的值抛出 TypeError.

Tuple 不可变，所以它没有 list 的任何修改内容的方法，如 append(), extend(), insert(), remove() 和 pop()。这些方法Tuple 都没有。

all(), any(), enumerate(), max(), min(), sorted(), len(), tuple() 等内置函数可用于 Tuple。

| 方法                     | 说明                                      |
| ------------------------ | ----------------------------------------- |
| a_tuple[1:3]             | 将 a_tuple 的[1,3) 元素创建一个新的 tuple |
| a_tuple.index('example') |                                           |
| "z" in a_tuple, not in   |                                           |

## 创建 tuple

以圆括号创建，元素之间以逗号分隔。如下：

```py
t1 = () # 创建空的 tuple
t2 = (50, ) # 创建一个元素的 tuple，必须包含括号
t2 = (11, 22, 33)
t3 = tuple([1, 2, 3, 4, 5, ]) # tuple from array
t4 = tuple("abc")  # tuple from string
t5 = 1, 2, 3 # 可以不带括号
```

Tuple 可以和List 相互转换，`tuple()` 函数将 list 转换为 tuple, `list()` 函数将 tuple 转换为 list.

max, min, len, sum 可以在 tuples 中使用。

## 访问值


## 作为 dict 的 key

由于 tuple 是 hashable，所以可以将 tuple 作为 dict 的键。

```py
a_dict[key_a, key_b] = number

for key_a, key_b in a_dict:
  …
```

a_dict.items() 返回值为 tuple 集合，每个 tuple 包含 dict 的键值对。
