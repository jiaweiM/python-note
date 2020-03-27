# Python Collection

- [Python Collection](#python-collection)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [List](#list)
    - [创建 List](#%e5%88%9b%e5%bb%ba-list)
    - [操作和函数](#%e6%93%8d%e4%bd%9c%e5%92%8c%e5%87%bd%e6%95%b0)
    - [List Comprehension](#list-comprehension)
  - [Tuple](#tuple)
    - [创建 tuple](#%e5%88%9b%e5%bb%ba-tuple)
    - [装箱和拆箱](#%e8%a3%85%e7%ae%b1%e5%92%8c%e6%8b%86%e7%ae%b1)
    - [作为 dict 的 key](#%e4%bd%9c%e4%b8%ba-dict-%e7%9a%84-key)
  - [Set](#set)
    - [创建 set](#%e5%88%9b%e5%bb%ba-set)
    - [set 操作](#set-%e6%93%8d%e4%bd%9c)
      - [对称差集](#%e5%af%b9%e7%a7%b0%e5%b7%ae%e9%9b%86)
    - [set 方法](#set-%e6%96%b9%e6%b3%95)
  - [Dictionary](#dictionary)
    - [创建 Dictionary](#%e5%88%9b%e5%bb%ba-dictionary)
    - [操作和方法](#%e6%93%8d%e4%bd%9c%e5%92%8c%e6%96%b9%e6%b3%95)
    - [方法](#%e6%96%b9%e6%b3%95)

***

## 简介

Python 内置集合类型包括：list, dict, set, tuple.

## List

List 为序列类型，可方便的执行添加、删除操作。List 为mutable 类型。

### 创建 List

创建类型相同的List

```py
l = [1, 2, 3, 4]
```

创建包含多种类型的List

```py
l2 = ["a string", 12]
```

其他创建list的方法

```py
list1 = list() # empty list
list2 = list([22, 31, 61])
list3 = list(["a", "b", "c"])
list5 = list("python") # Create a list with characters p, y, t, h, o, n
```

### 操作和函数

| 函数                              | 说明                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| list[-1]                          | 获得倒数第一个元素                                                                                           |
| a_list[1:3]                       | 子列表 [1:3)                                                                                                 |
| a_list[1:-1]                      | 子列表1 到末尾                                                                                               |
| a_list[:3]                        | [0, 3)                                                                                                       |
| a_list[3:]                        | [3, -1)                                                                                                      |
| a_list[:]                         | 全部， 复制列表                                                                                              |
| s1 + s2                           | Concatenates two sequences s1 ans s2                                                                         |
| s * n, n * s                      | n copies of sequence s concatenated                                                                          |
| a_list = a_list + [2.0, 3]        | + 号连接两个列表创建一个新的列表                                                                             |
| count(x: object): int             | Returns the number of times element x appears in the list                                                    |
| x in s                            | true if element x is in sequence s.                                                                          |
| x not in s                        | if element x is not in sequence s                                                                            |
| index(x: object): int             | Returns the index of the first occurrence of element x in the list                                           |
| append(x: object): None           | 添加 x 到列表末尾，返回 None                                                                                 |
| extend(l: list): None             | Appends all the elements in l to the list and returns None                                                   |
| insert(index: int, x:object):None | Inserts an element x at a given index. Note that the first element in the list has index 0 and retunrs None. |
| del a_list[1]                     | 删除 a_list 的第二个元素                                                                                     |
| remove(x:object):None             | Removes the first occurrence of element x from the list and returns None                                     |
| list.pop()                        | 删除并返回最后一个元素                                                                                       |
| list.pop(index)                   | 删除并返回指定位置的元素                                                                                     |
| list[index]=element               | 设定指定位置元素的                                                                                           |
| list[start:end]=b_list            | 设置list中start 到 end 的元素                                                                                |
| reverse():None                    | Reverse the list and returns None                                                                            |
| sort(): None                      | Sorts the elements in the list in ascending order and returns None.                                          |
| len(s)                            | Length of sequence s, i.e. the number of elements in s                                                       |
| min(s)                            | Smallest element in sequence s                                                                               |
| max(s)                            | Largest element in sequence s                                                                                |
| sum(s)                            | Sum of all numbers in sequence s                                                                             |
| for loop                          | Traverses elements from left to right in a for loop                                                          |
| all()                             | 列表所有项为 True                                                                                            |
| any()                             | 列表任意项为 True                                                                                            |
| enumerate                         | 同时返回元素的位置和值                                                                                       |
| list[::-1]                        | 列表倒序                                                                                                     |

### List Comprehension

以一种简洁的方式创建List，在方括号中包含创建元素的表达式。例：

```py
list1 = [ x for x in range(10)]  # list in range [0, 9]
list2 = [ x +1 for x in range(10)] # list in range [1, 10]
list3 = [x for x in range(10) if x %2 == 0] # [0, 2, 4, 6, 8]
list4 = [x*2 for x in range(10) if x % 2 == 0]  # [0, 4, 8, 12, 16]
```

## Tuple

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

### 创建 tuple

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

### 装箱和拆箱

装箱：使用多个变量，创建 Tuple.

拆箱：使用Tuple，给多个变量赋值，如

```py
v = ('a', 2, True)
(x, y, z) = v
a, b, c, = v # 也可以不带括号
```

基于该原理，可以很容易的值互换：

```py
a, b = b, a
```

如果有个变量带 * 号，则多余的值全部给该变量。

### 作为 dict 的 key

由于 tuple 是 hashable，所以可以将 tuple 作为 dict 的键。

```py
a_dict[key_a, key_b] = number

for key_a, key_b in a_dict:
  …
```

a_dict.items() 返回值为 tuple 集合，每个 tuple 包含 dict 的键值对。

## Set

set 是不包含重复值的无序集合。支持并集、交集、差集等集合操作。

### 创建 set

set 通过大括号创建，不同元素以逗号分隔，空 set 以 `set()` 创建。

```py
myset = {1, 2, 3}
```

### set 操作

set 由于元素是无序的，所以不能通过索引或 slicing 来访问。

| 集合操作 | 使用方法                                  |
| -------- | ----------------------------------------- |
| 并集     | 使用操作符 `|` 或者 `union()` 方法        |
| 交集     | 使用操作符 `&` 或者 `intersection()` 方法 |
| 差集     | 使用操作符 `-` 或者 `difference()` 方法   |

#### 对称差集

![difference](images/2019-09-05-13-16-38.png)

A 和 B 交集之外的内容。
使用 `^` 运算符或 `symmetric_difference()` 函数。

### set 方法

| 方法                              | 说明                                                                               |
| --------------------------------- | ---------------------------------------------------------------------------------- |
| set()                             | 创建一个空 set                                                                     |
| set(a_list)                       | 根据 list 元素创建 set                                                             |
| a_set.add(4)                      | 添加 4 到 a_set                                                                    |
| a_set.update(another_set)         | 将 another_set 中的元素全部添加到 a_set                                            |
| a_set.update(a_list)              | 同上                                                                               |
| a_set.discard(a_ele)              | 将 a_ele 元素从 a_set 中移除                                                       |
| a_set.remove(a_ele)               | remove 和 discard 的不同点是：如果set中不包含移除的元素，remove会抛出KeyError 异常 |
| a_set.pop()                       | 从 set 中移除一个元素，由于 set 是无序的，所以移除的元素随机                       |
| a_set.clear()                     | 移除所有元素，等同于 a_set=set(), 创建一个空 set, 覆盖a_set原来的值。              |
| 30  in a _set                     | 判断 30 是否在 a_set 中                                                            |
| a_set.union(b_set)                | 并集操作，返回一个新的集合                                                         |
| a_set.intersection(b_set)         | 交集操作                                                                           |
| a_set.difference(b_set)           | 差集操作                                                                           |
| a_set.symmetric_difference(b_set) | 只在一个 set 中出现的元素                                                          |
| a_set.issubset(b_set)             | a_set 是否是 b_set 的子集                                                          |
| b_set.issuperset(a_set)           | b_set 是否是 a_set 的超集                                                          |

## Dictionary

保存键值对的集合类型， mutable.

键必须可计算哈希值，值则可为任意类型。

### 创建 Dictionary

字典使用大括号 {} 创建，不同元素以逗号分开。

```py
friends = {
  'tom' : '111-222-333',
  'jerry': '666-33-111'
}
```

### 操作和方法

返回和指定键对应的值：

```py
dictionary_name['key']
```

如果对应键不存在，抛出 KeyError。

添加或修改值：

```py
dictionary_name['newkey'] = 'newvalue'
```

删除值：如果找到键，删除，如果没找到，抛出 KeyError

```py
del dictionary_name['key']
```

读取所有值：

```py
for key in a_dict:
  print(key, ":", a_dict[key])
```

### 方法

| 方法                | 说明                                                                                                                                      |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| len(a_dict)         | 返回字典包含键值对个数                                                                                                                    |
| a_key in a_dict     | a_dict 是否包含指定键                                                                                                                     |
| a_key not in a_dict | a_dict 是否不包含 a_key 键                                                                                                                |
| ==, !=              | 两个字典是否包含相同键值对                                                                                                                |
| popitem()           | Returns randomly select item from dictionary and also remove the selected item                                                            |
| clear()             | Delte everything from dictionary                                                                                                          |
| keys()              | Return keys in dictionary as tuples                                                                                                       |
| values()            | Return values in dictionary as tuples                                                                                                     |
| get(key)            | 返回和 key 对应的值，如果 key 不存在，返回 None                                                                                           |
| pop(key)            | Remove the item from the dictionary, if key is not found KeyError will be thrown.                                                         |
| copy()              | 完全复制                                                                                                                                  |
| update(a_iter)      | 将一个 dict 或 iterable 的内容全部添加到当前 dict中。对 iterable 且没有 keys() 方法的对象，以 tuple处理，将前两个元素作为键值对添加到dict |
| items()             | 返回包含键值对的 tuple 的list                                                                                                             |
| type(a_dict)        | 获得类型信息                                                                                                                              |
| cmp(a_dict, b_dict) | 对比两个字典的键和值                                                                                                                      |
| str(a_dict)         | 字符串                                                                                                                                    |
