# set

- [set](#set)
  - [简介](#简介)
  - [创建 set](#创建-set)
  - [set 操作](#set-操作)
    - [对称差集](#对称差集)
  - [set 方法](#set-方法)

## 简介

set 是不包含重复值的无序集合。支持并集、交集、差集等集合操作。

## 创建 set

set 通过大括号创建，不同元素以逗号分隔，空 set 以 `set()` 创建。

```py
myset = {1, 2, 3}
```

集合的本质是许多唯一对象的集合，因此可以用于去重：

```py
>>> l = ['spam', 'spam', 'eggs', 'spam']
>>> set(l)
{'eggs', 'spam'}
>>> list(set(l))
['eggs', 'spam']
```

## set 操作

set 由于元素是无序的，所以不能通过索引或 slicing 来访问。

| 集合操作 | 使用方法                                  |
| -------- | ----------------------------------------- |
| 并集     | 使用操作符 `|` 或者 `union()` 方法        |
| 交集     | 使用操作符 `&` 或者 `intersection()` 方法 |
| 差集     | 使用操作符 `-` 或者 `difference()` 方法   |

### 对称差集

![difference](images/2019-09-05-13-16-38.png)

A 和 B 交集之外的内容。
使用 `^` 运算符或 `symmetric_difference()` 函数。

## set 方法

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
