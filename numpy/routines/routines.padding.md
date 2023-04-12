# 填充数组

## numpy.pad

```python
numpy.pad(array, pad_width, mode='constant', **kwargs)
```

填充数组。

**参数：**

- **array**: `array_like` of rank N

待填充数组。

- **pad_width**: {`sequence`, `array_like`, `int`}

每个维度分别填充值个数。

Number of values padded to the edges of each axis. ((before_1, after_1), ... (before_N, after_N)) unique pad widths for each axis. (before, after) or ((before, after),) yields same before and after pad for each axis. (pad,) or int is a shortcut for before = after = pad width for all axes.

modestr or function, optional
One of the following string values or a user supplied function.

‘constant’ (default)
Pads with a constant value.

‘edge’
Pads with the edge values of array.

‘linear_ramp’
Pads with the linear ramp between end_value and the array edge value.

‘maximum’
Pads with the maximum value of all or part of the vector along each axis.

‘mean’
Pads with the mean value of all or part of the vector along each axis.

‘median’
Pads with the median value of all or part of the vector along each axis.

‘minimum’
Pads with the minimum value of all or part of the vector along each axis.

‘reflect’
Pads with the reflection of the vector mirrored on the first and last values of the vector along each axis.

‘symmetric’
Pads with the reflection of the vector mirrored along the edge of the array.

‘wrap’
Pads with the wrap of the vector along the axis. The first values are used to pad the end and the end values are used to pad the beginning.

‘empty’
Pads with undefined values.

New in version 1.17.

<function>
Padding function, see Notes.

stat_lengthsequence or int, optional
Used in ‘maximum’, ‘mean’, ‘median’, and ‘minimum’. Number of values at edge of each axis used to calculate the statistic value.

((before_1, after_1), ... (before_N, after_N)) unique statistic lengths for each axis.

(before, after) or ((before, after),) yields same before and after statistic lengths for each axis.

(stat_length,) or int is a shortcut for before = after = statistic length for all axes.

Default is None, to use the entire axis.

- **constant_values**: `sequence` or `scalar`, optional

用在 'constant' 中。为每个维度指定填充的值。

`((before_1, after_1), ... (before_N, after_N))` 为每个维度指定填充值。

`(before, after)` 或 `((before, after),)` 每个维度指定相同填充值。

默认 0.。

end_valuessequence or scalar, optional
Used in ‘linear_ramp’. The values used for the ending value of the linear_ramp and that will form the edge of the padded array.

((before_1, after_1), ... (before_N, after_N)) unique end values for each axis.

(before, after) or ((before, after),) yields same before and after end values for each axis.

(constant,) or constant is a shortcut for before = after = constant for all axes.

Default is 0.

reflect_type{‘even’, ‘odd’}, optional
Used in ‘reflect’, and ‘symmetric’. The ‘even’ style is the default with an unaltered reflection around the edge value. For the ‘odd’ style, the extended part of the array is created by subtracting the reflected values from two times the edge value.

## 参考

- https://numpy.org/doc/stable/reference/routines.padding.html
