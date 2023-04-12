# 选择

- [选择](#选择)
  - [选择单列](#选择单列)
    - [属性（column label）](#属性column-label)
    - [索引运算符](#索引运算符)

***

## 选择单列

### 属性（column label）

可以直接通过 column 的名称以属性的方式访问 column:

```py
>>> df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})
>>> df
   month  year  sale
0      1  2012    55
1      4  2014    40
2      7  2013    84
3     10  2014    31
>>> df.month
0     1
1     4
2     7
3    10
Name: month, dtype: int64
```

返回 `Series` 类型。


### 索引运算符

使用语法 `frame[colname]` 可以选择单列，使用该语法的优点是，名称中有空格也可以使用。该语法适用于所有情况，所以推荐使用。

```py
>>> df["month"]
0     1
1     4
2     7
3    10
Name: month, dtype: int64
```