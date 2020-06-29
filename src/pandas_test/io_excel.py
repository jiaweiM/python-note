import pandas as pd

with pd.ExcelFile(r'..\a.xlsx') as xlsx:
    data = pd.read_excel(xlsx, "Sheet1", header=0)
    print(data.columns)
