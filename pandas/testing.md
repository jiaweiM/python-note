# pandas.testing

- [pandas.testing](#pandastesting)
  - [assert_series_equsl](#assert_series_equsl)
  - [numpy.testing](#numpytesting)

2020-08-13, 12:42
***

## assert_series_equsl

`pandas.testing.assert_series_equal(left, right, check_dtype=True, check_index_type='equiv', check_series_type=True, check_less_precise=False, check_names=True, check_exact=False, check_datetimelike_compat=False, check_categorical=True, check_category_order=True, obj='Series')`

用于检测两个 `Series` 是否相等。

- check_dtype

是否检查 `dtype` 相同，default True。

- check_index_type

bool 或 {'equiv'}，default 'equiv'。

是否检查`Index` 类、dtype 和 inferred_type 相同。

## numpy.testing

使用其测试方法，可以只测试值，而无法关注索引。

`numpy.array_equal`
