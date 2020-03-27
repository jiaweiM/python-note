import pandas as pd
import numpy as np

df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])
df1 = df.filter(regex='e$', axis=1)
print(df)
print(df1)
