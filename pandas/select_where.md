# where()

- [where()](#where)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [实例](#%e5%ae%9e%e4%be%8b)
    - [默认替换值为 nan](#%e9%bb%98%e8%ae%a4%e6%9b%bf%e6%8d%a2%e5%80%bc%e4%b8%ba-nan)
    - [](#)

***

## 简介

使用布尔向量从 `Series` 中选择一般返回数据的子集。为了保证选择结果和原数据具有相同的 shape，可以使用 `Series` 和 `DataFrame` 的 `where` 方法。

where 方法签名：

```py
Series.where(self,cond,other=nan,inplace=False,axis=None,level=None,errors='raise',try_cast=False)
```

对`cond` 为 False 的数值，用 `other` 替换其值。

参数：

1. `cond`

类型：bool 类型的 Series/DataFrame，或 `callable`。

如果 `cond` 为 True，保留原值，否则以 `other` 替换。如果 `cond` 为 `callable`，则根据 Series/DataFrame 的当前值进行计算，返回值必须为 boolean 类型的 `Series`/`DataFrame` 或数组。`callable` 不能修改输入的 Series/DataFrame。

2. `other`

类型：scalar, Series/DataFrame, or callable

对 `cond` 为 False 的数据，以 `other` 替代。如果 `other` 为 `callable` 类型，则根据原数据进行计算，返回值必须为 scalar, Series/DataFrame 类型。callable 不允许修改输入 Series/DataFrame.

3. `inplace`

类型：bool, default False

是否对数据进行原位操作。

4. `axis`

类型：int, default None.

是否对其 axis.

5. `level`

Alignment level if needed.

6. `errors`

类型： str, {'raise', 'ignore'}, default 'raise'

该参数不影响结果，结果总会转换为合适的 dtype。

- 'raise'，抛出异常。
- 'ignore'，抑制异常。

7. `try_cast`

类型：bool, default False

尝试将结果转换为输入类型。

返回：和调用者相同的类型。

> `DataFrame.where()` 签名和 `numpy.where()` 略有不同，`df11.where(m, df2)` 基本上等价于 `np.where(m, df1, df2)`。

## 实例

### 默认替换值为 nan

```py
s = pd.Series(range(5))
s1 = s.where(s > 0)
```

Out:

```cmd
0    NaN
1    1.0
2    2.0
3    3.0
4    4.0
dtype: float64
```

### 