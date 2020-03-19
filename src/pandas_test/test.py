# %%
import pandas as pd
import numpy as np

# %%
n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
df
