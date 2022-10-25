# itertools

- [itertools](#itertools)
  - [简介](#简介)
    - [组合迭代器](#组合迭代器)
  - [zip_longest](#zip_longest)
  - [groupby](#groupby)
  - [permutations](#permutations)
  - [参考](#参考)

2021-06-22, 09:52
***

## 简介

`itertools` 模块实现了许多迭代器构造函数，标准化了一套快速的、内存高效的工具集。

| 函数         | 功能                                               |
| ------------ | -------------------------------------------------- |
| count        | 从指定数开始，向上无穷迭代                         |
| cycle        | 循环迭代 iterable 对象                             |
| repeat       | 重复对象                                           |
| takewhile    | 从 iterable 提取满足 predicate 函数的元素          |
| chain        | 将多个 iterable 合并为一个                         |
| accumulate   | 进行累加操作，每次累加得到一个值，放在 iterable 中 |
| product      | 两个 iterable 对象，进行自由组合                   |

### 组合迭代器

|迭代器|参数|结果|
|---|---|---|
|`product()`|p, q, … [repeat=1]|笛卡尔乘积，等价于嵌套 for 循环，元素可以重复|
|`permutations()`|p[, r]|长度为 r 的 tuples，所有可能顺序组合，元素不重复|
|combinations()|p, r|长度为 r 的 tuples，按顺序排列，元素不重复|


## zip_longest

```py
itertools.zip_longest(*iterables, fillvalue=None)
```

将多个 iterables 对象聚合为一个迭代器，长度不足的用 `fillvalue` 补齐。

例如：

```py
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
l = list(zipped)
assert len(l) == 5
assert l[3] == ('?', '?', 3)
```

## groupby

`itertools.groupby(iterable, key=None)`

创建一个迭代器，该迭代器从 `iterable` 返回连续的 keys 和 groups。

`key` 参数提供一个函数，该函数从每个元素计算出一个 key 值。如果不指定 `key` 或者为 `None`，默认为 identity 函数，元素按原样返回。`iterable` 通常需要已按照 key 排序。

`groupby()` 扫描整个序列并查找连续相同值（或者根据指定 key 函数返回值相同）的元素序列，当 key 值改变就生成一个新的分组。每次迭代的时候，它返回一个值（分组）和一个迭代器对象，该迭代器对象的所有元素的 key 值和分组值相同。

对元素进行排序很重要，因为 `groupby()` 仅仅检查连续的元素，如果序列没有排序，分组函数难以得到想要的结果。

假设有如下序列：

```py
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
```

现在需要按 `date` 进行分组:

```py
from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
```

Out:

```cmd
07/01/2012
  {'address': '5412 N CLARK', 'date': '07/01/2012'}
  {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
07/02/2012
  {'address': '5800 E 58TH', 'date': '07/02/2012'}
  {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
  {'address': '1060 W ADDISON', 'date': '07/02/2012'}
07/03/2012
  {'address': '2122 N CLARK', 'date': '07/03/2012'}
07/04/2012
  {'address': '5148 N CLARK', 'date': '07/04/2012'}
  {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
```

如果是根据 `date` 字段将数据分组到一个大的数据结构中，并且可以随机访问，可以使用 `defaultdict()`：

```py
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
```

这样就可以访问每个 `date` 对应的元素：

```py
>>> for r in rows_by_date['07/01/2012']:
... print(r)
...
{'date': '07/01/2012', 'address': '5412 N CLARK'}
{'date': '07/01/2012', 'address': '4801 N BROADWAY'}
```

## permutations

Last updated: 2022-10-25, 10:19

```python
itertools.permutations(iterable, r=None)
```

返回 `iterable` 中元素的排列，长度为 `r`。

如果 `r` 未指定或为 `None`，则 `r` 默认为 `iterable` 的长度，生成所有可能的全长排列。

返回的排列 tuples 根据输入 `iterable` 按字典顺序生成。因此，如果输入的 `iterable` 已排序，则生成的组合 tuples 按排序后的顺序生成。

元素根据其位置而不是值来判断唯一性。因此，如果输入元素是唯一的，那么在每次排列中都不会有重复值。

该函数大致等价于：

```python
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```

`permutations()` 的代码也可以表示为 `product()` 的子序列，只需过滤掉包含重复元素的条目：

```python
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
```

返回 tuple 个数为 $n!/(n-r)!$，其中 $0\le r \le n$。

## 参考

- https://docs.python.org/3/library/itertools.html
