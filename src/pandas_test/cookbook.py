# %% [markdown]
# # Cookbook
# 这是一个简短的示例库，并提供了一些有用的 pandas 链接。
#
# 下面的示例隐式导入 Pandas (pd) 和 Numpy (np) ，其它的显式导入。
#
# 所有示例以 Python 3 编写，对早期 Python 版本可能部分不兼容。

# %% [markdown]
# ## Idioms
#
# 有一些简洁的 pandas 用例。
#
# %%
import pandas as pd
import numpy as np

# %% [markdown]
# if-then/if-then-else on one column, and assignment to another one or more columns:

# %%
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
df

# %% [markdown]
# ### if-then...
#
# - 对一列执行 if 操作，对另一列赋值

# %%
df.loc[df.AAA >= 5, 'BBB'] = -1  # 如果 AAA >= 5，就设置对应的 BBB 为 -1
df

# %% [markdown]
# - 对一列执行 if 操作，对另两列赋值

# %%
df.loc[df.AAA >= 5, ['BBB', 'CCC']] = 555  # 如果 AAA >= 5，则对应 BBB 和 CCC 设置为 555
df

# %% [markdown]
# - 另一个 if-then 操作

# %%
df.loc[df.AAA < 5, ['BBB', 'CCC']] = 2000  # 如果 AAA < 5，则将 BBB 和 CCC 设置为 2000
df


# %% [markdown]
# Or use pandas where after you’ve set up a mask

# %%
df_mask = pd.DataFrame({'AAA': [True] * 4,
                        'BBB': [False] * 4,
                        'CCC': [True, False] * 2})
df.where(df_mask, -1000)


# %% [markdown]
# if-then-else using numpy’s where()

# %%
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
df

# %%
# 如果 AAA > 5， 设置为 high，否则为 low
df['logic'] = np.where(df['AAA'] > 5, 'high', 'low')
df

# %% [markdown]
# ### Splitting
# 使用 boolean 向量拆分 frame

# %%
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
df

# %%
df[df.AAA <= 5]  # 选择 AAA <= 5 的 rows

# %%
df[df.AAA > 5]  # 选择 AAA > 5 的 rows


# %% [markdown]
# ### Building criteria
#
# #### 使用多列信息构建规则

# %%
pd.DataFrame({'AAA': [4, 5, 6, 7],
              'BBB': [10, 20, 30, 40],
              'CCC': [100, 50, -30, -50]})
df

# %% [markdown]
# without assignment returns a Series

# %%
df.loc[(df['BBB'] < 25) & (df['CCC'] >= -40), 'AAA']

# %% [markdown]
# without assignment returns a Series

# %%
df.loc[(df['BBB'] > 25) | (df['CCC'] >= -40), 'AAA']

# %% [markdown]
# with assignment modifies the DataFrame

# %%
df.loc[(df['BBB'] > 25) | (df['CCC'] >= 75), 'AAA'] = 0.1
df

# %% [markdown]
# #### 使用 argsort 选择数值解决特定值的行


# %%
df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
df

# %%
aValue = 43.0
df.loc[(df.CCC - aValue).abs().argsort()]


# %% [markdown]
# #### 