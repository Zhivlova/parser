import numpy as np
import pandas as pd
import os

user_data = {'Pc': 400.0, 'D4': 240.0, 'Pcif': 3.0, 'ER': 75.0, 't_in': 0.1, 't_out': 0.3, 'Qt': 800.0, 'S': 4000.0,
             'D': 4000.0, 'M': 500.0}

class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.Pc = float(dict_from_frontend.get('Pc'))
        self.D4 = float(dict_from_frontend.get('D4'))
        self.Pcif = float(dict_from_frontend.get('Pcif'))
        self.ER = float(dict_from_frontend.get('ER'))
        self.t_in = float(dict_from_frontend.get('t_in'))
        self.t_out = float(dict_from_frontend.get('t_out'))
        self.Qt = float(dict_from_frontend.get('Qt'))
        self.S = float(dict_from_frontend.get('S'))
        self.D = float(dict_from_frontend.get('D'))
        self.M = float(dict_from_frontend.get('M'))

def food_products_import(input_data):
    """Получаем данные из модели"""

    mydir = '/Users/natalazivlova/Desktop/spectr-scientific-backend/food_products_import/food_products_import/'
    myfile = 'Импорт_все_продтовары.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:J', index_col=0)

    # Характеристики ценообразования
    pricing_characteristics = df.iloc[2:11, 0:5]
    pricing_characteristics.index = np.arange(0, len(pricing_characteristics))
    pricing_characteristics = pricing_characteristics.rename(columns={'Unnamed: 1': 'designation',
                                                                      'Unnamed: 2': 'measure', 'до': 'before',
                                                                      'после': 'after', 'Прирост,%': 'increment_pr'})
    print(pricing_characteristics.to_markdown())


input_data = InputDataBase(user_data)
result = food_products_import(input_data)
print(result)