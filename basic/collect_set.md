# set

- [set](#set)
  - [简介](#简介)
  - [创建 set](#创建-set)
  - [集合操作](#集合操作)
    - [并集](#并集)
    - [交集](#交集)
    - [对称差集](#对称差集)
    - [isdisjoint](#isdisjoint)
    - [子集](#子集)
    - [超集](#超集)
  - [set 方法](#set-方法)
    - [集合长度](#集合长度)
    - [访问元素](#访问元素)
    - [添加元素](#添加元素)
    - [批量添加元素](#批量添加元素)
    - [删除元素](#删除元素)
    - [删除集合](#删除集合)
    - [复制集合](#复制集合)
  - [参考](#参考)

2021-10-08, 11:08
@author Jiawei Mao
***

## 简介

set 是不包含重复值的无序集合。支持并集、交集、差集等集合操作。

## 创建 set

创建集合的方式有两种：

- 使用 `set` 函数
- 使用集合字面量 `{}`

使用大括号创建，不同元素以逗号分隔。例如：

```py
myset = {1, 2, 3}
```

`set()` 可用于创建空集合，或者从其它集合对象常见 set：

```py
set() # 创建空集合
set([2, 2, 2, 1, 3, 3])
```

集合的本质是许多唯一对象的集合，因此可以用于去重：

```py
>>> l = ['spam', 'spam', 'eggs', 'spam']
>>> set(l)
{'eggs', 'spam'}
>>> list(set(l))
['eggs', 'spam']
```

## 集合操作

set 由于元素是无序的，所以不能通过索引或 slicing 来访问。

| 集合操作 | 操作符|方法 |
| --- | --- |---|
| 并集 | `|`|`union()`|
|原位并集|`|=`|`update()`|
| 交集 | `&`|`intersection()`|
|原位交集|`&=`|`intersection_update()`|
| 差集 |`-`|`difference()`|
|原位差集|`-=`|`difference_update()`|
|对称差集|`^`|`symmetric_difference()`|
|原位对称差集|`^=`|`symmetric_difference()`|

> 原位操作表示不创建新的集合，将操作结果保存在原集合。

### 并集

使用 `union()` 方法或 `|` 操作符计算并集。并集作为一个新的集合返回。例如：

```py
a = {1, 2, 3}
b = {2, 3, 4}
c = a.union(b)

assert c == {1, 2, 3, 4}
```

如果不需要返回一个新的集合，可以使用 `update()` 方法，即将 `b` 中的元素全部添加到 `a` 中。

### 交集

使用 `intersection()` 方法或者 `&` 操作符计算交集，交集作为一个新的集合返回。例如：

```py
a = {1, 2, 3}
b = {2, 3, 4}
c = a.intersection(b)
assert c == {2, 3}
```

如果不需要创建新的集合，可以使用 `intersection_update` 方法，例如:

```py
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
assert a == {2, 3}
```

### 对称差集

![difference](images/2019-09-05-13-16-38.png)

A 和 B 交集之外的内容。
使用 `^` 运算符或 `symmetric_difference()` 函数。

### isdisjoint

```py
isdisjoint(other)
```

如果和 `other` 集合没有交集，返回 `True`。例如：

```py
a = {1, 2, 3}
b = {3, 4, 5}
c = {4, 5, 6}
assert not a.isdisjoint(b)
assert a.isdisjoint(c)
```

### 子集

`issubset` 用于判断是否为其它集合的子集。

```py
issubset(other)
set <= other
```

`issubset` 等价于 `<=` 操作，即包含相等的情况。如果排除相等情况，可以用 `<` 操作符。例如：

```py
a = {1, 2, 3}
b = {1, 2, 3}
assert a.issubset(b)

assert not a < b
c = {1, 2, 3, 4}
assert a < c
```

### 超集

用 `issuperset(other)` 或 `>=` 操作符判断是否为其它集合的超集。例如：

```py
a = {1, 2, 3}
b = {1, 2}
assert a.issuperset(b)
```

和 `issubset` 一样，如果抛出等同的情况，可以用 `>` 操作符。

## set 方法

| 方法  | 说明  |
| --- | --- |
| `set()`| 创建一个空 set |
| `set(a_list)` | 根据 list 元素创建 set |
| `a_set.add(4)` | 添加 4 到 a_set  |
| `a_set.update(another_set)`  | 将 another_set 中的元素全部添加到 a_set  |
| `a_set.update(a_list)` | 同上  |
| `a_set.discard(a_ele)` | 将 `a_ele` 从 a_set 中移除|
| `a_set.remove(a_ele)` | 删除 `a_ele`，如果set中不包含 `a_ele` 则抛出 `KeyError`|
| `a_set.pop()`  | 从 set 中移除一个元素，由于 set 是无序的，所以移除的元素随机 |
| `a_set.clear()` | 移除所有元素 |
| `30  in a _set` | 判断 30 是否在 a_set 中        |
| `a_set.issubset(b_set)`  | a_set 是否是 b_set 的子集        |
| `b_set.issuperset(a_set)`  | b_set 是否是 a_set 的超集        |

### 集合长度

使用 `len()` 查看集合大小：

```py
a = {1, 2, 3, 4, 5}
assert len(a) == 5
```

### 访问元素

不能通过键或索引访问集合元素。可以通过 `for` 循环访问元素，或者通过 `in` 关键字查询集合是否包含指定元素。

for 循环访问：

```py
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```

查询是否包含指定元素：

```py
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```

### 添加元素

集合创建后，无法修改集合中的元素，但是可以添加和删除元素。

使用 `add()` 方法添加元素：

```py
s = {1, 2, 3}
s.add(4)
assert len(s) == 4
assert 4 in s
```

### 批量添加元素

使用 `update()` 方法批量添加元素。例如：

```py
a = {1, 2, 3}
b = {3, 4, 5, 6}
a.update(b)
assert a == {1, 2, 3, 4, 5, 6}
```

`update()` 函数可用于任意可迭代对象，包括集合和其它序列类型。

### 删除元素

删除元素的方法有 4 种：

- `remove(elem)`，如果集合中没有 `elem` 抛出 `KeyError`；
- `discard(elem)`，如果集合中存在 `elem`，删除该元素；
- `pop()` 从集合中移除任意一个元素；
- `clear()` 清空集合。

例如，`remove()` 在移除 4 时，由于集合中没有 4，抛出 `KeyError`：

```py
a = {1, 2, 3}
a.remove(2)
assert a == {1, 3}
with pytest.raises(KeyError):
    a.remove(4)  # 没有 4，所以抛出 KeyError
```

`discard()` 在不抛出异常：

```py
a = {1, 2, 3}
a.discard(2)
assert a == {1, 3}
a.discard(4)
assert a == {1, 3}
```

`pop()` 从集合中移除任意一个元素，如果集合为空，抛出 `KeyError`：

```py
a = {1, 2, 3}
x = a.pop() # 任意移除一个元素，并返回该值
assert x not in a # 此时 a 中已经没有 x
assert len(a) == 2
```

`clear()` 清空集合：

```py
a = {1, 2, 3}
a.clear()
assert len(a) == 0
```

### 删除集合

`del` 是删除对象的通用方法，可用于删除集合：

```py
a = {1, 2, 3}
del a
with pytest.raises(UnboundLocalError):
    print(a)
```

### 复制集合

`copy()` 方法返回集合的浅拷贝。

例如：

```py
a = {1, 2, 3}
b = a.copy()
assert b == {1, 2, 3}
```

## 参考

- https://www.w3schools.com/python/python_sets.asp
- Python for Data Analysis. Data Wrangling with Pandas, NumPy, and IPython, 2ed
