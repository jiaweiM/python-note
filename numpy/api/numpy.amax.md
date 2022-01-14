# numpy.amax

```python
numpy.amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
```

返回数组的最大值，或者沿着指定轴的最大值。

## 参数

- `a`

数组。

## 示例

```python
>>> a = np.arange(4).reshape((2,2))
>>> a
array([[0, 1],
       [2, 3]])
```

- 数组最大值

```python
>>> np.amax(a)
3
```

- 沿第 1 个轴的最大值

```python
>>> np.amax(a, axis=0)   # Maxima along the first axis
array([2, 3])
```



## 参考

- https://numpy.org/devdocs/reference/generated/numpy.amax.html
