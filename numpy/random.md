# Random sampling

- [Random sampling](#random-sampling)
  - [Quick Start](#quick-start)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [Random Generator](#random-generator)
    - [Access BitGenerator](#access-bitgenerator)
    - [Simple random date](#simple-random-date)
    - [Permutations](#permutations)
    - [Distribution](#distribution)
      - [Generator.standard_normal](#generatorstandardnormal)
  - [方法总结](#%e6%96%b9%e6%b3%95%e6%80%bb%e7%bb%93)
    - [`RandomState.randn(d0, d1,...,dn)`](#randomstaterandnd0-d1dn)

Numpy 的随机数生成器组合使用 `BitGenerator` 和 `Generator`生成伪随机数：

- `BitGenerator`，生产随机数的对象。通常生成 unsigned integer 填充 32 或 64 字节的随机序列
- `Generator` 使用序列根据统计分布取样，即将来自 `BitGenerator` 的随机字节序列按照指定概率分布转换为数字序列。

从 Numpy 1.17.0 开始，可以使用不同的 `BitGenerator` 初始化 `Generator`。

## Quick Start

使用 `default_rng` 获得 `Generator` 实例，然后调用其方法获得不同分布的样本。`Generator` 默认使用 `PCG64` 提供的bits，其统计性质比旧版中 `RandomState` 使用的 `MT19937` 更好。

新版使用方式（推荐）：

```py
from numpy.random import default_rng

rng = default_rng()
vals = rng.standard_normal(10)
more_vals = rng.standard_normal(10)
```

旧版使用方式（不推荐）：

```py
from numpy import random

vals = random.standard_normal(10)
more_vals = random.standard_normal(10)
```

`Generator` 可以替代 `RandomState`，两个类的内部都使用 `BitGenerator` 实例提供 bit 流，可以使用 `gen.bit_generator` 对其进行访问。

|`RandomState`|`Generator`|说明|
|----|---|----|
|random_sample|random|和 `random.random` 兼容|
|rand|||
|randint|integers|添加了 `endpoint` 参数|
|random_integers|||
|tomaxint|removed|使用 `integers(0, np.iinfo(np.int_).max, endpoint=False)`|
|seed|removed|使用 `SeedSequence.spawn`|

下面的代码同时支持 `RandomState` 和 `Generator`，不过要明白去接口略有不同：

```py
try:
    rg_integers = rg.integers
except AttributeError:
    rg_integers = rg.randint

a = rg_integers(1000)
```

Seed 可以通过 `BitGenerator` 设置。提供的 seed 值通过 `SeedSequence` 进行混合，以将 seed 序列分布到 `BitGenerator` 的初始化状态。下面使用 `PCG64`：

```py
from numpy.random import Generator, PCG64

rg = Generator(PCG64(12345))
rg.standard_normal()
```

## 简介

新版采用了不同的方法从 `RandomState` 对象生成随机数。随机数生成分为两部分，即位生成器和随机生成器。

位生成器（BitGenerator） 负责管理状态，可以生成随机的 doubles, unsigned 32-bit 和 64-bit 值。

随机生成器（random generator）将位生成器提供的数据流转换为更有用的分布，如模拟正态分布随机数值。该结构可以很容易的更改位生成器。

`Generator` 是一个面向用户的对象，它和 `RandomState` 几乎相同。

默认采用 `PCG64` 位生成器作为唯一参数初始化 generator。

```py
from numpy.random import default_rng
rg = default_rng(12345)
rg.random()
```

也可以直接使用 `BitGenerator`实例初始化 `Generator`。例如，如果要使用旧版的 `MT19937` 算法，可以直接使用其实例初始化 `Generator`：

```py
from numpy.random import Generator, MT19937
rg = Generator(MT19937(12345))
rg.random()
```

> `Generator` 不再支持 Box-Muller 方法生成正态分布。使用 `Generator` 无法重现正态分布或依赖于正态分布（如 RandomState.gamma 或 RandomState.standard_t）的随机值。如果需要向后兼容，可以使用 `RandomState`。

- `Generator` 的 normal, exponential 和 gamma 函数使用 256-step Ziggurat 方法，比 Box-Muller 或 inverse CDF 实现快 2-10 倍。
- 可选的 `dtype` 参数接受 `np.float32` 或 `np.float64`，用于生成单精度或双精度随机值。
- 可选的 `out` 参数接受数组，填充选择分布的随机值。
- `Generator.integers` 是从离散均匀分布生成整数随机数的规范方法。`rand` 和 `randn` 方法仅可通过旧版的 `RandomState` 使用。

`numpy.random` 模块用于生成随机数。

`numpy.random.RandomState` 是 Mersenne Twister 伪随机数生成器的容器。

|函数|说明|
|---|---|
|rand(d0, d1, …, dn)|创建指定 shape 的数组，并以均匀分布数值填充|
|randn(d0, d1,…,dn)	|生成满足标准正态分布的浮点数数组，数组 shape d0, d1,…,dn.|
|random(size=None)	|生成[0.0,1.0)之间的随机浮点数|

## Random Generator

### Access BitGenerator

### Simple random date

### Permutations

### Distribution

#### Generator.standard_normal

`Generator.standard_normal(size=None, dtype='d', out=None)`

从标准正态分布（mean=0, stdev=1）中抽样。

参数：

- size, int or tuple of ints，输出随机数 shape，例如，`(m,n,k)` 表示抽取样本数为 `m*n*k`。默认为 `None`，表示返回单个值。
- dtype, {str, dtype}，结果类型，'d' ('float64') 或 'f' ('float32')。
- out, ndarray，备用的输出数组。如果 `size` 不为 `None`，则其 shape 必须为 `size` 相同，类型匹配。

返回值：

float or ndarray，如果未指定 `size`，返回一个浮点数；如果指定 `size`，返回浮点数数组。

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

## 方法总结

### `RandomState.randn(d0, d1,...,dn)`

从标准正态分布中返回一个或多个样本。

- 如果提供了 int 参数，则以均值0、方差1的正态分布随机浮点数填充指定 shape (d0,d1,...,dn) 的数组。
- 如果没有提供参数，则从分布中返回一个随机取样的浮点数。

> 新代码应该是用 `defualt_rng()` 的 `standard_normal` 方法。
