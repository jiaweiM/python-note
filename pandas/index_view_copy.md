# Returning view versus copy

- [Returning view versus copy](#returning-view-versus-copy)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [使用链式索引赋值失败](#%e4%bd%bf%e7%94%a8%e9%93%be%e5%bc%8f%e7%b4%a2%e5%bc%95%e8%b5%8b%e5%80%bc%e5%a4%b1%e8%b4%a5)
  - [执行顺序](#%e6%89%a7%e8%a1%8c%e9%a1%ba%e5%ba%8f)

***

## 简介

在 pandas 中设置对象值时需要注意避免链式索引（`chained indexing`）。例如：

```py
>>> dfmi = pd.DataFrame([list('abcd'),
   .....                 list('efgh'),
   .....                 list('ijkl'),
   .....                 list('mnop')],
   .....                 columns=pd.MultiIndex.from_product([['one', 'two'],
   .....                                                     ['first', 'second']]))

>>> dfmi
    one          two
  first second first second
0     a      b     c      d
1     e      f     g      h
2     i      j     k      l
3     m      n     o      p
```

对比下面两种访问方法：

方法一：

```py
>>> dfmi['one']['second']
0    b
1    f
2    j
3    n
Name: second, dtype: object
```

方法二：

```py
>>> dfmi.loc[:, ('one', 'second')]
0    b
1    f
2    j
3    n
Name: (one, second), dtype: object
```

两者生成的结果相同，那么使用哪一种？理解方法二优于方法一对于理解 pandas 操作很重要。

`dfmi['one']` 选择第一个 level 的 columns，返回单索引的 `DataFrame`。`dfmi_with_one['second']` 选择 index 为 `'second'` 的 `Series`。即方法一是两个操作串联起来，分步调用 `__getitem__`。

`df.loc[:, ('one', 'second')]` 内部则使用 tuple `(slice(None), ('one', 'second'))` 单次调用 `__getitem__`。该操作更快。

## 使用链式索引赋值失败

上一节仅仅是性能问题，但 pandas 有时为何给出 `SettingWithCopy` 警告？

使用链式索引赋值有时候结果无法预测。为了理解该内容，我们先看看 Python 解释器如何执行下列代码：

```py
dfmi.loc[:, ('one', 'second')] = value
# becomes
dfmi.loc.__setitem__((slice(None), ('one', 'second')), value)
```

而：

```py
dfmi['one']['second'] = value
# becomes
dfmi.__getitem__('one').__setitem__('second', value)
```

由于无法确定 `__getitem__` 返回视图还是副本（取决于数组的内存结构，pandas 无法保证），因此 `__setitem__` 可能修改 `dfmi`，也可能修改的是一个临时对象。所以才有 `SettingWithCopy` 警告。

有时候没有明显的链式索引 pandas 也抛出 `SettingWithCopy`，大多情况是 pandas 不确定其中是否有链式索引，例如：

```py
def do_something(df):
    foo = df[['bar', 'baz']]  # Is foo a view? A copy? Nobody knows!
    # ... many lines here ...
    # We don't know whether this will modify df or not!
    foo['quux'] = value
    return foo
```

## 执行顺序

使用链式索引时，索引的顺序和类型影响结果类型，到底是原对象切片还是切片副本。

pandas 的 `SettingWithCopyWarning` 警告该类型操作，很少故意赋值给切片副本，不小心赋值给切片副本会导致意外错误。

设置 pandas 对链式索引的信任程度，设置 `mode.chained_assignment` 为下列值之一：

- `warn`，默认值，输出 `SettingWithCopyWarning` 信息
- `raise`，抛出 `SettingWithCopyException`
- `None`，完全取消警告

```py
>>> dfb = pd.DataFrame({'a': ['one', 'one', 'two',
   .....                          'three', 'two', 'one', 'six'],
   .....                    'c': np.arange(7)})
   .....

# This will show the SettingWithCopyWarning
# but the frame values will be set
>>> dfb['c'][dfb['a'].str.startswith('o')] = 42
```

而下面会出错：

```py
>>> pd.set_option('mode.chained_assignment','warn')
>>> dfb[dfb['a'].str.startswith('o')]['c'] = 42
Traceback (most recent call last)
     ...
SettingWithCopyWarning:
     A value is trying to be set on a copy of a slice from a DataFrame.
     Try using .loc[row_index,col_indexer] = value instead
```

正确的访问方法：

```py
>>> dfc = pd.DataFrame({'A': ['aaa', 'bbb', 'ccc'], 'B': [1, 2, 3]})
>>> dfc.loc[0, 'A'] = 11
>>> dfc
     A  B
0   11  1
1  bbb  2
2  ccc  3
```

而下面的可能对，但结果无法保证：

```py
>>> dfc = dfc.copy()
>>> dfc['A'][0] = 111
>>> dfc
     A  B
0  111  1
1  bbb  2
2  ccc  3
```

而下面这种语法是错误的：

```py
>>> pd.set_option('mode.chained_assignment','raise')
>>> dfc.loc[0]['A'] = 1111
Traceback (most recent call last)
     ...
SettingWithCopyException:
     A value is trying to be set on a copy of a slice from a DataFrame.
     Try using .loc[row_index,col_indexer] = value instead
```
