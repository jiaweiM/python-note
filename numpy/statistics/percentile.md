# numpy.percentile

```python
numpy.percentile(a, 
				 q, axis=None, out=None, overwrite_input=False, 
				 method='linear', 
				 keepdims=False, *, interpolation=None)
```

沿指定 axis 计算数据的第 q 个百分位数，返回数组元素的第  q 个百分位数。

**参数：**

- **a**: array_like

输入数组，或可以转换为数组的对象。

- **q**: array_like of float

要计算的百分位数，或百分位数序列，取值 [0,100]。

- **axis**: {int, tuple of int, None}, optional

沿该指定的 axis 或 axes 计算百分位数。默认沿展开的数组计算百分位数。

- **out**: ndarray, optional

放置结果的输出数组（可选）。其 shape 和 buffer length 必须与预期输出相同，类型不需要相同，该方法必要时会强制转换类型。

**overwrite_input**bool, optional

If True, then allow the input array _a_ to be modified by intermediate calculations, to save memory. In this case, the contents of the input _a_ after this function completes is undefined.

**method**str, optional

This parameter specifies the method to use for estimating the percentile. There are many different methods, some unique to NumPy. See the notes for explanation. The options sorted by their R type as summarized in the H&F paper [[1]](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#r08bde0ebf37b-1) are:

1. ‘inverted_cdf’
    
2. ‘averaged_inverted_cdf’
    
3. ‘closest_observation’
    
4. ‘interpolated_inverted_cdf’
    
5. ‘hazen’
    
6. ‘weibull’
    
7. ‘linear’ (default)
    
8. ‘median_unbiased’
    
9. ‘normal_unbiased’
    

The first three methods are discontinuous. NumPy further defines the following discontinuous variations of the default ‘linear’ (7.) option:

- ‘lower’
    
- ‘higher’,
    
- ‘midpoint’
    
- ‘nearest’
    

Changed in version 1.22.0: This argument was previously called “interpolation” and only offered the “linear” default and last four options.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original array _a_.

New in version 1.9.0.

**interpolation**str, optional

Deprecated name for the method keyword argument.

Returns:

**percentile**scalar or ndarray

If _q_ is a single percentile and _axis=None_, then the result is a scalar. If multiple percentiles are given, first axis of the result corresponds to the percentiles. The other axes are the axes that remain after the reduction of _a_. If the input contains integers or floats smaller than `float64`, the output data-type is `float64`. Otherwise, the output data-type is the same as that of the input. If _out_ is specified, that array is returned instead.