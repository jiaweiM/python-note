# dict

- [dict](#dict)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [创建字典](#%e5%88%9b%e5%bb%ba%e5%ad%97%e5%85%b8)
  - [操作](#%e6%93%8d%e4%bd%9c)
  - [方法](#%e6%96%b9%e6%b3%95)
  - [映射多个值](#%e6%98%a0%e5%b0%84%e5%a4%9a%e4%b8%aa%e5%80%bc)

***

## 简介

保存键值对的集合类型， mutable.

键必须可计算哈希值，值则可为任意类型。

## 创建字典

构造函数：

```py
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
```

使用可选的位置参数和可能为空的关键字参数初始化字典。

- 如果没有位置参数，将创建一个空字典。
- 如果给出一个位置参数并且是映射对象，将创建一个具有与映射对象相同键值对的字典。
- 如果位置参数不是映射对象，则必须是 `iterable` 对象，且该可迭代对象中的每一项必须是包含两个元素的可迭代对象。每一项的第一个为键，第二个为值。 如果一个键出现多次，该键的最后一个值将成为其在新字典中对应的值。
- 如果给出了关键字参数，则关键字参数及其值会被加入到基于位置参数创建的字典。如果要加入的键已存在，则来自关键字参数的值将覆盖来自位置参数的值。

下面以多种方式创建字典 `{"one": 1, "two": 2, "three": 3}`:

```py
>>> a = dict(one=1, two=2, three=3) # 关键字参数
>>> b = {'one': 1, 'two': 2, 'three': 3} # 直接创建
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) # 可迭代对象位置参数
>>> d = dict([('two', 2), ('one', 1), ('three', 3)]) # 可迭代对象位置参数
>>> e = dict({'three': 3, 'one': 1, 'two': 2}) # 映射对象位置参数
>>> a == b == c == d == e
True
```

大括号 {} 创建字段，不同元素以逗号分开。

```py
friends = {
  'tom' : '111-222-333',
  'jerry': '666-33-111'
}
```

## 操作

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

## 方法

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

## 映射多个值

字典一个键映射一个值，如果要映射多个值，就需要将多个值放到另外的容器，比如列表或者set中。例如：

```py
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}
```

选择使用列表还是集合取决于实际需求。如果想保持元素的插入顺序，就使用列表，如果要去掉重复元素，就使用集合。

也可以使用 `collections` 的 `defaultdict` 构造这样的词典。