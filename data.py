import os
import pandas as pd

file = 'state_institutions.xlsx'
xl = pd.ExcelFile(file)
print(xl.sheet_names)
df1 = xl.parse('state_institutions.xlsx')