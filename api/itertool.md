# itertools

- [itertools](#itertools)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [总结](#%e6%80%bb%e7%bb%93)
  - [函数](#%e5%87%bd%e6%95%b0)
    - [zip_longest](#ziplongest)

***

## 简介

`itertools` 模块包含许多方便函数编程的函数。

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

## 函数

### zip_longest

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
