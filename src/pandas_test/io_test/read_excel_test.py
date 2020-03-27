import pandas as pd

df = pd.read_excel(r'src\pandas_test\io_test\data_0.xlsx', sheet_name='Sheet1')
print(df)
