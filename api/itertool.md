# itertools

- [itertools](#itertools)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [总结](#%e6%80%bb%e7%bb%93)
  - [zip_longest](#ziplongest)
  - [groupby](#groupby)

***

## 简介

`itertools` 模块实现了许多迭代器构造函数，标准化了一套快速的、内存高效的工具集。

## 总结

| 函数         | 功能                                               |
| ------------ | -------------------------------------------------- |
| count        | 从指定数开始，向上无穷迭代                         |
| cycle        | 循环迭代 iterable 对象                             |
| repeat       | 重复对象                                           |
| takewhile    | 从 iterable 提取满足 predicate 函数的元素          |
| chain        | 将多个 iterable 合并为一个                         |
| accumulate   | 进行累加操作，每次累加得到一个值，放在 iterable 中 |
| product      | 两个 iterable 对象，进行自由组合                   |
| permutations | itetable 里元素自由组合                            |

## zip_longest

`itertools.zip_longest(*iterables, fillvalue=None)`

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
