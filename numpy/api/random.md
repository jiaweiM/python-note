# numpy.random

- [numpy.random](#numpyrandom)
  - [rand](#rand)
  - [randn](#randn)

***

## rand

```python
random.rand(d0, d1, ..., dn)
```

创建指定 shape 的数组，并用均匀分布 [0,1) 上的随机样本填充。

**参数：**

- **d0, d1, …, dn**: `int`, optional

指定数组的维数，非负数。不指定参数，则返回一个 float。

**返回：**

- **out**: `ndarray`, shape (d0, d1, ..., dn)

包含随机数的数组。

**示例：**

```python
>>> np.random.rand(3,2)
array([[ 0.14022471,  0.96360618],  #random
       [ 0.37601032,  0.25528411],  #random
       [ 0.49313049,  0.94909878]]) #random
```

## randn

```python
random.randn(d0, d1, ..., dn)
```

返回满足标准正态分布的随机数组。

