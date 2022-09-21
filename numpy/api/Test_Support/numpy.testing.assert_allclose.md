# numpy.testing.assert_allclose

Last updated: 2022-09-21, 09:02
****

```python
testing.assert_allclose(actual, desired, rtol=1e-07, atol=0, equal_nan=True, err_msg='', verbose=True)
```

如果两个对象在指定 tolerance 下不相等，抛出 `AssertionError`。

对两个 array_like 对象，检查 shape 和所有元素是否相等。如果 shape 不匹配，或任何值不相等，抛出异常。

与 numpy 的标准用法不同，该方法支持 NaN，相同位置都是 NaN 不抛出异常。

该 test 等价于 `allclose(actual, desired, rtol, atol)` (不过默认值不同)。要求 `actual` 的 `desired` 值的差别不超过 `atol + rtol * abs(desired)`。

|参数|类型|说明|
|---|---|---|
|actual|array_like|实际数组|
|desired|array_like|期望数组|
|rtol|float|相对 tolerance|
|atol|float|绝对 tolerance|
|equal_nan|bool|True 时认为 NaN 值相等|
|err_msg|str|断言失败时的错误信息|
|verbose|bool|在错误信息中是否附加冲突值|

## 示例

```python
>>> x = [1e-5, 1e-3, 1e-1]
>>> y = np.arccos(np.cos(x))
>>> np.testing.assert_allclose(x, y, rtol=1e-5, atol=0)
```

## 参考

- https://numpy.org/devdocs/reference/generated/numpy.testing.assert_allclose.html
