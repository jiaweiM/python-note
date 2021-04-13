# Function application

- [Function application](#function-application)
  - [简介](#简介)
  - [方法链](#方法链)
  - [Row or column-wise 函数](#row-or-column-wise-函数)

2020-04-21, 10:20
***

## 简介

如果需要将你自定义的函数或某个库函数应用于 pandas 对象，可以考虑下面三个方法。具体使用哪个函数，取决于函数应用的数据。

1. Tablewise 函数：`pipe()`
2. Row 或 Column-wise 函数：`apply()`
3. Aggregation API:`agg()` 和 `transform()`
4. Elementwise 函数：`applymap()`

## 方法链

将 `DataFrame` 和 `Series` 传入函数。如果需要链式调用函数，则建议使用 `pipe()` 方法。

首先进行初始设置：

```py
def extract_city_name(df):
    """
    Chicago, IL -> Chicago for city_name column
    """
    df["city_name"] = df["city_and_code"].str.split(",").str.get(0)
    return df


def add_country_name(df, country_name=None):
    """
    Chicago -> Chicago-US for city_name column
    """
    col = "city_name"
    df["city_and_country"] = df[col] + country_name

df_p = pd.DataFrame({'city_and_code': ['Chicago, IL']})
```

`extract_city_name` 和 `add_country_name` 两个函数接受 `DataFrame`，也返回 `DataFrame`。

对比：

```py
In : add_country_name(extract_city_name(df_p), country_name='US')
Out:
  city_and_code city_name city_and_country
0   Chicago, IL   Chicago        ChicagoUS
```

等价于：

```py
In : (df_p.pipe(extract_city_name)
   :      .pipe(add_country_name, country_name="US"))
Out:
  city_and_code city_name city_and_country
0   Chicago, IL   Chicago        ChicagoUS
```

pandas 鼓励使用第二种方式，称之为**方法链**。`pipe` 使得方法的链式调用更为便捷。

在上例中，`extract_city_name` 和 `add_country_name` 都要求第一个参数为 `DataFrame`。如果你要应用的函数将数据放在第二个参数怎么办？

此时可以为 `pipe` 提供 tuple 类型 `(callable, data_keyword)` 参数。`pipe` 会将 `DataFrame` 放到 tuple 对应的参数位置。

例如，使用 statsmodels 拟合回归，其 API 要求第一个参数为 formula，第二个参数 `data` 为 `DataFrame`。此时可以用 `(sm.ols, 'data')` 作为 `pipe` 参数：

```py
In [143]: import statsmodels.formula.api as sm

In [144]: bb = pd.read_csv('data/baseball.csv', index_col='id')

In [145]: (bb.query('h > 0')
   .....:    .assign(ln_h=lambda df: np.log(df.h))
   .....:    .pipe((sm.ols, 'data'), 'hr ~ ln_h + year + g + C(lg)')
   .....:    .fit()
   .....:    .summary()
   .....:  )
   .....:
Out[145]:
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results
==============================================================================
Dep. Variable:                     hr   R-squared:                       0.685
Model:                            OLS   Adj. R-squared:                  0.665
Method:                 Least Squares   F-statistic:                     34.28
Date:                Wed, 18 Mar 2020   Prob (F-statistic):           3.48e-15
Time:                        15:38:44   Log-Likelihood:                -205.92
No. Observations:                  68   AIC:                             421.8
Df Residuals:                      63   BIC:                             432.9
Df Model:                           4
Covariance Type:            nonrobust
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept   -8484.7720   4664.146     -1.819      0.074   -1.78e+04     835.780
C(lg)[T.NL]    -2.2736      1.325     -1.716      0.091      -4.922       0.375
ln_h           -1.3542      0.875     -1.547      0.127      -3.103       0.395
year            4.2277      2.324      1.819      0.074      -0.417       8.872
g               0.1841      0.029      6.258      0.000       0.125       0.243
==============================================================================
Omnibus:                       10.875   Durbin-Watson:                   1.999
Prob(Omnibus):                  0.004   Jarque-Bera (JB):               17.298
Skew:                           0.537   Prob(JB):                     0.000175
Kurtosis:                       5.225   Cond. No.                     1.49e+07
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.49e+07. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
```

pipe 方法受  unix pipe 以及 R 中引入的管道流 %>% 的启发。

## Row or column-wise 函数

使用 `apply()` 可以应用函数到 DataFrame 的任意 axes 的数据。包含一个可选的 `axis` 参数:

- "index" (axis=0, default)
- "columns"(axis=1)

例如：

```py
In [146]: df.apply(np.mean)
Out[146]:
one      0.811094
two      1.360588
three    0.187958
dtype: float64

In [147]: df.apply(np.mean, axis=1)
Out[147]:
a    1.583749
b    0.734929
c    1.133683
d   -0.166914
dtype: float64

In [148]: df.apply(lambda x: x.max() - x.min())
Out[148]:
one      1.051928
two      1.632779
three    1.840607
dtype: float64

In [149]: df.apply(np.cumsum)
Out[149]:
        one       two     three
a  1.394981  1.772517       NaN
b  1.738035  3.684640 -0.050390
c  2.433281  5.163008  1.177045
d       NaN  5.442353  0.563873

In [150]: df.apply(np.exp)
Out[150]:
        one       two     three
a  4.034899  5.885648       NaN
b  1.409244  6.767440  0.950858
c  2.004201  4.385785  3.412466
d       NaN  1.322262  0.541630
```

`apply()` 方法