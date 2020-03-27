import pandas as pd
df = pd.DataFrame({"col1": [1, 2, 3],
                   "col2": [4, 5, 6],
                   "col3": [7, 8, 9]},
                  index=["row1", "row2", "row3"])
df1 = df.iloc[[0, 2], [1, 2]]
print(df)
print(df1)