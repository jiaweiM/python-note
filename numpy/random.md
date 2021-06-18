# Random sampling

- [Random sampling](#random-sampling)
  - [快速入门](#快速入门)
  - [简介](#简介)
    - [新旧API的主要差异](#新旧api的主要差异)
  - [Generator](#generator)
    - [Generator.integers](#generatorintegers)
  - [Distribution](#distribution)
    - [Generator.standard_normal](#generatorstandard_normal)
  - [随机排列](#随机排列)
  - [RandomState](#randomstate)
    - [`RandomState.randn(d0, d1,...,dn)`](#randomstaterandnd0-d1dn)
    - [`RandomState.rand(d0,d1,...,dn)`](#randomstaterandd0d1dn)
    - [`Generator.integer`](#generatorinteger)
  - [参考](#参考)

2021-06-18, 15:11
***

## 快速入门

Numpy 使用 `BitGenerator` 和 `Generator` 生成伪随机数：

- `BitGenerator`，用于生产随机数，通常使用 32 或 64 个随机位（bit）序列填充 unsigned int。
- `Generator`，将 `BitGenerator` 生成的随机位（bit）序列按照指定统计分布转换为数字序列。

> 从 Numpy 1.17.0 开始，可以使用不同的 `BitGenerator` 初始化 `Generator`。

调用 `default_rng` 获得 `Generator` 实例，然后根据分布调用合适方法获得样本。`Generator` 默认使用 `PCG64` 提供的bits，其统计学性质比旧版中 `RandomState` 使用的 `MT19937` 更好。

- 新版方式（推荐）：

```py
from numpy.random import default_rng

rng = default_rng()
vals = rng.standard_normal(10)
more_vals = rng.standard_normal(10)
```

- 旧版方式（不推荐）：

```py
from numpy import random

vals = random.standard_normal(10)
more_vals = random.standard_normal(10)
```

可以将 `Generator` 看作 `RandomState` 的更新版本。两个类的内部都使用 `BitGenerator` 提供 bit 流，使用 `gen.bit_generator` 访问 `BitGenerator`。两者对比：

| `RandomState`   | `Generator` | 说明  |
| ---- | ---- | ----- |
| random_sample   | random      | 和 `random.random` 兼容 |
| rand            |             |                                                           |
| randint         | integers    | 添加了 `endpoint` 参数   |
| random_integers |             |                                                           |
| tomaxint        | removed     | 使用 `integers(0, np.iinfo(np.int_).max, endpoint=False)` |
| seed            | removed     | 使用 `SeedSequence.spawn`                                 |

下面的代码同时支持 `RandomState` 和 `Generator`，不过要明白两者接口略有不同：

```py
try:
    rg_integers = rg.integers
except AttributeError:
    rg_integers = rg.randint

a = rg_integers(1000)
```

Seed 通过 `BitGenerator` 设置。所有的 seed 值通过 `SeedSequence` 进行混合，以将 seed 序列分布到 `BitGenerator` 的初始化状态。

下面使用 `PCG64`：

```py
from numpy.random import Generator, PCG64

rg = Generator(PCG64(12345))
rg.standard_normal()
```

- 下面使用 `default_rng` 创建 `Generator` 生成随机浮点数：

```py
>>> import numpy as np
>>> rng = np.random.default_rng(12345)
>>> print(rng)
Generator(PCG64)
>>> rfloat = rng.random()
>>> rfloat
0.22733602246716966
>>> type(rfloat)
<class 'float'>
```

- 使用 `default_rng` 创建 `Generator` 生成3个 [0,10) 之间的整数

```py
>>> import numpy as np
>>> rng = np.random.default_rng(12345)
>>> rints = rng.integers(low=0, high=10, size=3)
>>> rints
array([6, 2, 7])
>>> type(rints[0])
<class 'numpy.int64'>
```

## 简介

新版采用了不同的方法从 `RandomState` 对象生成随机数。随机数的生成分为两步，即位生成器和随机生成器。

位生成器（BitGenerator）负责维护状态、生成随机的 doubles, unsigned 32-bit 和 64-bit 值。

随机生成器（random generator）将位生成器提供的数据流转换为更有用的分布，如模拟正态分布随机数值。而且可以采用不同的位生成器。

`Generator` 是一个面向用户的对象，它和旧版的 `RandomState` 几乎相同。`Generator` 以 `BitGenerator` 为参数，默认为 `PCG64`。NumPy 提供 `default_rng` 函数，以隐藏这些细节。

- 默认采用 `PCG64` 位生成器作为唯一参数初始化 generator。

```py
>>> from numpy.random import default_rng
>>> rg = default_rng(12345)
>>> print(rg)
Generator(PCG64)
>>> print(rg.random())
0.22733602246716966
```

- 也可以使用 `BitGenerator` 初始化 `Generator`。

例如，使用 `PCG64` 作为位生成器初始化 `Generator`:

```py
>>> from numpy.random import Generator, PCG64
>>> rg = Generator(PCG64(12345))
>>> print(rg)
Generator(PCG64)
```

如果想使用旧版的 `MT19937` 算法（不建议），可以使用其实例初始化 `Generator`：

```py
>>> from numpy.random import Generator, MT19937
>>> rg = Generator(MT19937(12345))
>>> print(rg)
Generator(MT19937)
```

### 新旧API的主要差异

> `Generator` 不再支持 Box-Muller 方法生成正态分布。使用 `Generator` 无法重现正态分布或依赖于正态分布（如 `RandomState.gamma` 或 `RandomState.standard_t`）的随机值。如果需要向后兼容，可以使用 `RandomState`。

- `Generator` 的 normal, exponential 和 gamma 函数使用 256-step Ziggurat 方法，比 Box-Muller 或 inverse CDF 快 2-10 倍。
- 可选 `dtype` 参数为 `np.float32` 或 `np.float64`，用于生成单精度或双精度随机数。
- 可选 `out` 参数可用随机数填充已有数组。
- BitGenerator 可以用于下游的 Cython 项目。
- `Generator.integers` 是从离散均匀分布生成随机整数的标准方法。`rand` 和 `randn` 方法仅可通过旧版的 `RandomState` 访问。`endpoint` kw 参数用于指定区间。彻底替换 `randint` 和 `random_integers`。
- `Generator.random` 是生成随机浮点数的标准方法，替换 `RandomState.random_sample`, `RandomState.sample` 和 `RandomState.ranf`，和`random.random` 一致；
- 所有的 BitGenerators 使用 `SeedSequence` 将 seeds 初始化。

`numpy.random.RandomState` 是 Mersenne Twister 伪随机数生成器的容器。

| 函数                | 说明                                                      |
| ------------------- | --------------------------------------------------------- |
| rand(d0, d1, …, dn) | 创建指定 shape 的数组，并以均匀分布数值填充               |
| randn(d0, d1,…,dn)  | 生成满足标准正态分布的浮点数数组，数组 shape d0, d1,…,dn. |
| random(size=None)   | 生成[0.0,1.0)之间的随机浮点数                             |

## Generator

### Generator.integers

```py
random.Generator.integers(low, high=None, size=None, dtype=np.int64, endpoint=False)
```

生成 [low,high) 之间的随机整数，如果 `endpoint=True`，则生成 [low,high] 之间的随机整数。替代了 `RandomState.randint` 和 `RandomState.random_integers` 方法。


## Distribution

### Generator.standard_normal

`Generator.standard_normal(size=None, dtype='d', out=None)`

从标准正态分布（mean=0, stdev=1）中抽样。

|参数|类型|说明|
|---|---|----|
|size|int or tuple of ints, *optional*|输出随机数 shape，例如，`(m,n,k)` 表示抽取`m*n*k` 个样本。默认为 `None`，表示返回单个值|
|dtype|dtype, *optional*|结果类型，支持 `float64` 和 `float32`，字节顺序必须为 native，默认为 np.float64|
|out|ndarray, *optional*|输出数组，如果 `size` 不为 None，则该数组和 `size` 必须相同，类型匹配|

返回值：float or ndarray，如果未指定 `size`，返回一个浮点数；如果指定 `size`，返回浮点数数组。

如果需要从 $N(\mu, \sigma^2)$ 中随机取样，使用下面两种方法的一种：

```py
mu + singma * gen.starnard_normal(size=...)
gen.normal(mu, sigma, size=...)
```

- 例：单个随机数

```py
from numpy.random import default_rng

rng = default_rng()
rng.standard_normal()
```

- 例：指定数目的随机数

```py
from numpy.random import default_rng

rng = default_rng()
s = rng.standard_normal(10)
print(s)
print(s.shape)
```

Out:

```cmd
[-1.12844901  0.64260562 -0.3847536  -0.68510945  2.06075599  0.30675705
 -0.92733534 -1.0526262  -1.26503188 -0.85412492]

(10,)
```

- 例：指定 shape

```py
from numpy.random import default_rng

rng = default_rng()
s = rng.standard_normal(size=(3, 4, 2))
print(s)
print(s.shape)
```

Out:

```cmd
[[[-0.91317958 -0.92788231]
  [-1.4459228   0.97802877]
  [-0.46631587  1.22369929]
  [ 0.85839833  0.90292751]]

 [[ 0.57149976  1.25118439]
  [ 0.65197806 -0.48483036]
  [ 0.83249725 -0.82719083]
  [ 0.24669684 -1.61963322]]

 [[ 0.01824205  0.21728075]
  [ 0.80506933  0.08693854]
  [ 0.23074958 -1.03725207]
  [-0.82439024 -1.85402158]]]

(3, 4, 2)
```

- 例：指定正态分布 $N(3, 6.25)$

```py
from numpy.random import default_rng

rng = default_rng()
s = 3 + 2.5 * rng.standard_normal(size=(2, 4))
print(s)
```

输出：

```cmd
array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
       [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
```

## 随机排列

```py
random.Generator.permutation(x, axis=0)
```

随机排列一个序列，或者返回一个排列过的范围。

- x: int or array_like

如果 x 为整数，则随机排列 `np.arange(x)`。如果 x 是数组，则复制数组，并随机排列数组元素。

- axis: int, optional

随机排列的轴，默认为 0.


例1，生成指定范围内数值的随机排序：

```py
rng = np.random.default_rng()
a1 = rng.permutation(10)
print(a1)
# [5 8 6 2 7 1 0 3 9 4]
```

例2，对数组随机排序：

```py
a2 = rng.permutation([1, 4, 9, 12, 15])
print(a2)
# [ 1 15  4  9 12]
```

例 3，多维数组随机排序：

```py
rng = np.random.default_rng()
arr = np.arange(9).reshape((3, 3))
print(arr)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

a3 = rng.permutation(arr)
print(a3)
# [[6 7 8]
#  [0 1 2]
#  [3 4 5]]
```

`axis`默认为 0，所以这里只对第 1 维进行了随机排序。

例 4，多维数组指定随机排序轴：

```py
rng = np.random.default_rng()
arr = np.arange(9).reshape((3, 3))
print(arr)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

a3 = rng.permutation(arr, axis=1)
print(a3)
# [[1 2 0]
#  [4 5 3]
#  [7 8 6]]
```

解释：这里指定 `axis=1`，所以对第二维进行随机排序，第1维保持不变。

## RandomState

`RandomState` 是 NumPy 遗留的随机数生成器，不再推荐使用。

|                                |                              |
| ------------------------------ | ---------------------------- |
| rand(d0,d1,...,dn)             | 指定shape的随机数            |
| randn(d0,d1,...,dn)            | 从标准正态分布中返回一个样本 |
| randint(low[,high,size,dtype]) |

### `RandomState.randn(d0, d1,...,dn)`

从标准正态分布中返回一个或多个样本。

- 如果提供了 int 参数，则以均值0、方差1的正态分布随机浮点数填充指定 shape (d0,d1,...,dn) 的数组。
- 如果没有提供参数，则从分布中返回一个随机取样的浮点数。

> 新代码应该是用 `defualt_rng()` 的 `standard_normal` 方法。

### `RandomState.rand(d0,d1,...,dn)`

创建指定 shape 的数组，并用 [0,1) 均匀分布的随机样本填充该数组。

参数：

1. `d0,d1,...,dn` 返回数组的 shape。如果无参数，返回一个 float值

返回：

ndarray, shape (d0, d1, ..., dn) 随机值。

- 例如：

```py
import numpy as np

def test_rand():
    values = np.random.rand(3, 2)
    assert values.shape == (3, 2)
    print(values)
```

Out:

```cmd
[[0.67083557 0.38698512]
 [0.54298704 0.66626554]
 [0.44859257 0.63306649]]
```

### `Generator.integer`

`integers(low[, high, size, dtype, endpoint])`

## 参考

- https://numpy.org/doc/stable/reference/random/index.html
