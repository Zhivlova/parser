import numpy as np
import pandas as pd
import os

mydir = '/Users/natalazivlova/Desktop/parser/historical_block/'
myfile = 'Производительность_шлихового_золота_1855_1880_27_12_2022.xlsx'
file = os.path.join(mydir, myfile)
df = pd.read_excel(file, usecols='A:Y')

# Урал
ural = df.iloc[4:34, 0:7]
ural = ural.rename(
    columns={'Урал': 'Пудов', 'Unnamed: 2': 'Фунтов', 'Unnamed: 3': 'Золотников', 'Unnamed: 4': 'Пудов',
             'Unnamed: 5': 'Фунтов', 'Unnamed: 6': 'Золотников', 'Unnamed: 7': 'Пудов'})
ural.index = np.arange(len(ural))
print(ural.to_markdown())
