# Input and output

## NumPy binary files (NPY, NPZ)

|                                              |                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------- |
| load(file[, mmap_mode, allow_pickle, …])     | Load arrays or pickled objects from .npy, .npz or pickled files.    |
| save(file, arr[, allow_pickle, fix_imports]) | Save an array to a binary file in NumPy .npy format.                |
| savez(file, \*args, \*\*kwds)                | Save several arrays into a single file in uncompressed .npz format. |
| savez_compressed(file, \*args, \*\*kwds)     | Save several arrays into a single file in compressed .npz format.   |

### numpy.load

## Text formatting options

|                                             |                                                               |
| ------------------------------------------- | ------------------------------------------------------------- |
| set_printoptions([precision, threshold, …]) | Set printing options.                                         |
| get_printoptions()                          | Return the current print options.                             |
| set_string_function(f[, repr])              | Set a Python function to be used when pretty printing arrays. |
| printoptions(\*args, \*\*kwargs)            | Context manager for setting print options.                    |

### numpy.set_printoptions

`numpy.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=None, formatter=None, sign=None, floatmode=None, **kwarg)[source]`

设置打印选项。

这些选项设置浮点数、数组以及其它 NumPy 对象的显示方式。

参数：

- precision: int or None, optional

浮点数输出的小数点位数（默认 8）。如果 `floatmode` 不固定，则为 `None`，则打印足够多的位数以保证该值的唯一性。

- threshold: int, optional

触发 summarization 而不是完整 repr 的数组元素个数（默认 1000）。

- edgeitems: int, optional

Number of array items in summary at beginning and end of each dimension (default 3).

- linewidth : int, optional

The number of characters per line for the purpose of inserting line breaks (default 75).

- suppress : bool, optional

If True, always print floating point numbers using fixed point notation, in which case numbers equal to zero in the current precision will print as zero.

If False, then scientific notation is used when absolute value of the smallest number is < 1e-4 or the ratio of the maximum absolute value to the minimum is > 1e3. The default is False.

nanstr : str, optional
String representation of floating point not-a-number (default nan).

infstr : str, optional
String representation of floating point infinity (default inf).

sign : string, either ‘-‘, ‘+’, or ‘ ‘, optional
Controls printing of the sign of floating-point types. If ‘+’, always print the sign of positive values. If ‘ ‘, always prints a space (whitespace character) in the sign position of positive values. If ‘-‘, omit the sign character of positive values. (default ‘-‘)

formatter : dict of callables, optional
If not None, the keys should indicate the type(s) that the respective formatting function applies to. Callables should return a string. Types that are not specified (by their corresponding keys) are handled by the default formatters. Individual types for which a formatter can be set are:

‘bool’
‘int’
‘timedelta’ : a numpy.timedelta64
‘datetime’ : a numpy.datetime64
‘float’
‘longfloat’ : 128-bit floats
‘complexfloat’
‘longcomplexfloat’ : composed of two 128-bit floats
‘numpystr’ : types numpy.string_ and numpy.unicode_
‘object’ : np.object_ arrays
‘str’ : all other strings
Other keys that can be used to set a group of types at once are:

‘all’ : sets all types
‘int_kind’ : sets ‘int’
‘float_kind’ : sets ‘float’ and ‘longfloat’
‘complex_kind’ : sets ‘complexfloat’ and ‘longcomplexfloat’
‘str_kind’ : sets ‘str’ and ‘numpystr’
floatmode : str, optional
Controls the interpretation of the precision option for floating-point types. Can take the following values (default maxprec_equal):

‘fixed’: Always print exactly precision fractional digits,
even if this would print more or fewer digits than necessary to specify the value uniquely.
‘unique’: Print the minimum number of fractional digits necessary
to represent each value uniquely. Different elements may have a different number of digits. The value of the precision option is ignored.
‘maxprec’: Print at most precision fractional digits, but if
an element can be uniquely represented with fewer digits only print it with that many.
‘maxprec_equal’: Print at most precision fractional digits,
but if every element in the array can be uniquely represented with an equal number of fewer digits, use that many digits for all elements.
legacy : string or False, optional
If set to the string ‘1.13’ enables 1.13 legacy printing mode. This approximates numpy 1.13 print output by including a space in the sign position of floats and different behavior for 0d arrays. If set to False, disables legacy mode. Unrecognized strings will be ignored with a warning for forward compatibility.

New in version 1.14.0.