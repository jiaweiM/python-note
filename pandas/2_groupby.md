- [简介](#%e7%ae%80%e4%bb%8b)
- [分组（split）](#%e5%88%86%e7%bb%84split)
  - [根据列名进行分组](#%e6%a0%b9%e6%8d%ae%e5%88%97%e5%90%8d%e8%bf%9b%e8%a1%8c%e5%88%86%e7%bb%84)
  - [通过函数定义分组](#%e9%80%9a%e8%bf%87%e5%87%bd%e6%95%b0%e5%ae%9a%e4%b9%89%e5%88%86%e7%bb%84)
  - [查看 groups 数据](#%e6%9f%a5%e7%9c%8b-groups-%e6%95%b0%e6%8d%ae)
- [应用函数（applying）](#%e5%ba%94%e7%94%a8%e5%87%bd%e6%95%b0applying)
- [合并（combining）](#%e5%90%88%e5%b9%b6combining)

# 简介
pandas 的 `GroupBy` 功能可以方便地对数据进行分组、操作、转换和聚合；分组运算，也称为 "split-apply-combine" 操作。

|操作|功能|
|---|---|
|分组（Splitting）|根据规则将数据分组|
|操作（Applying）|对各个分组应用特定操作|
|合并（Combining）|将操作结果合并成一个数据结构|

# 分组（split）
splitting, 根据指定规则对数据分组。

<img src="images/2019-08-28-14-24-08.png" alt="drawing" width="363" height="311">

split 功能由 obj.groupby() 方法实现。
```py
groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs)
```

将一个 DataFrame 根据指定映射规则分成多个 DataFrame，定义映射关系的方法有：
- Python 函数，根据特定 axis label 计算
- 选择的 axis 长度相同的 NumPy array
- A dict or Series, 提供 label -> group name 的映射
- 对 `DataFrame` 对象，可以使用特定的 column name，例如 df.groupby('A')，即 df.groupby(df['A'])，使用'A' 列进行分组

## 根据列名进行分组
将字符串作为 `groupby` 参数，因为 `column label` 和 `index label`都可能包含该字符串，出现重复时，会抛出警告，并优先使用 `column label`。

**例1：根据列名分组**
```py
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
```
Out:

![](images/2019-08-28-14-29-55.png)

根据A列分组：

```py
grouped = df.groupby('A')
for name, group in grouped:
    print(name)
    print(group)
```
Out:

![](images/2019-08-28-14-30-49.png)

说明：A 列只有两类值，'foo' 和 'bar'，所以结果分为了两组。

**例2：根据多列进行分组**

```py
for name, group in df.groupby(['A', 'B']):
    print(name)
    print(group)
```
同时使用A列和B列进行分组，结果如下：

![](images/2019-08-28-14-32-11.png)

## 通过函数定义分组
定义函数：
```py
def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'
```

分组：
```py
grouped = df.groupby(get_letter_type, axis=1)
```

## 查看 groups 数据
groupby 返回值可以看做包含 `groupName`, `group` 的字典。

**例：查看分组数据**
```py
for name, group in grouped:
    print(name)
    print(group)
```
Out:

![](images/2019-08-28-14-34-42.png)

如果根据多个键值进行分组，返回的 group name 为 tuple。

**例：查看多键值分组数据**
```py
for name, group in df.groupby(['A', 'B']):
    print(name)
    print(group)
```
Out:

![](images/2019-08-28-14-35-25.png)

# 应用函数（applying）
applying, 对分组数据执行特定运算函数。

<img src="images/2019-08-28-14-24-53.png" alt="drawing" width="417" height="435">

Applying 涉及到如下操作

|操作|说明|
|---|---|
|Aggregation|对分组数据进行统计运算，例如：计算加和或均值；计算 group sizes / counts|
|Transformation|对特定分组进行运算，例如：标准化数据 (zscore)；根据分组数据特征填充 NAs值|
|Filtration|根据规则舍弃部分分组，例如：舍弃数据太少的分组；根据分组数据的特征，如加和、均值等过滤分组|

# 合并（combining）
combining, 将结果合并为一个数据结构

<img src="images/2019-08-28-14-25-27.png" width="553" height="391">
