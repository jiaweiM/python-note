# %%
import numpy as np
import pandas as pd

# %%
dates = pd.date_range('1/1/2000', periods=8)

# %%
df = pd.DataFrame(np.random.default_rng().standard_normal(size=(8, 4)),
                  index=dates, columns=['A', 'B', 'C', 'D'])

# %%
df

# %%
s = df['A']
s[dates[5]]

# %%
df[['B', 'A']] = df[['A', 'B']]
df

# %%
df[['A', 'B']]

# %%
df.loc[:, ['B', 'A']] = df[['A', 'B']]
df[['A', 'B']]

# %%
df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()
df[['A', 'B']]


# %%
sa = pd.Series([1, 2, 3], index=list('abc'))
sa.b


# %%
dfa = df.copy()
dfa.A


# %%
sa.a = 5
sa

# %%
dfa.A = list(range(len(dfa.index)))
dfa

# %%
