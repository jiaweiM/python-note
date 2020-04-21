import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]},
                  index=pd.MultiIndex.from_product([['a', 'b'], ['c', 'd']]))

df.to_excel('path_to_file.xlsx')

df = pd.read_excel('path_to_file.xlsx', index_col=[0, 1])

print(df)
