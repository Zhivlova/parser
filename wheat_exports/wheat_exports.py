from pprint import pprint

import numpy as np
import pandas as pd
import os

user_data = {'PW_A_shift_after': 0.0, 'ER_before': 75.0, 'ER_after': 75.0,
             'CT_before': 50.0, 'CT_after': 50.0, 'TD_before': 0.0, 'TD_after': 0.0,
             'Pb_before': 15000.0, 'Pb_after': 15000.0, 'Pb2_before': 375.0,
             'Pb2_after': 375.0, 'Pb3_before': 400.0, 'Pb3_after': 400.0,
             't1_before': 0.7, 't1_after': 0.69, 't2_before': 0.8, 't2_after': 0.8,
             't3_before': 0.9, 't3_after': 0.9, 'demp_before': 0.1, 'demp_after': 0.1,
             'i_cost_before': 1.0, 'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0,
             'shift_QSI_A_after': 0.0, 'shift_QSW_A_before': 0.0,
             'shift_QSW_A_after': 0.0, 'i_cost_world_before': 1.0, 'i_cost_world_after': 1.0}


class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.PW_A_shift_after = float(dict_from_frontend.get('PW_A_shift_after'))
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.CT_before = float(dict_from_frontend.get('CT_before'))
        self.CT_after = float(dict_from_frontend.get('CT_after'))
        self.TD_before = float(dict_from_frontend.get('TD_before'))
        self.TD_after = float(dict_from_frontend.get('TD_after'))
        self.Pb_before = float(dict_from_frontend.get('Pb_before'))
        self.Pb_after = float(dict_from_frontend.get('Pb_after'))
        self.Pb2_before = float(dict_from_frontend.get('Pb2_before'))
        self.Pb2_after = float(dict_from_frontend.get('Pb2_after'))
        self.Pb3_before = float(dict_from_frontend.get('Pb3_before'))
        self.Pb3_after = float(dict_from_frontend.get('Pb3_after'))
        self.t1_before = float(dict_from_frontend.get('t1_before'))
        self.t1_after = float(dict_from_frontend.get('t1_after'))
        self.t2_before = float(dict_from_frontend.get('t2_before'))
        self.t2_after = float(dict_from_frontend.get('t2_after'))
        self.t3_before = float(dict_from_frontend.get('t3_before'))
        self.t3_after = float(dict_from_frontend.get('t3_after'))
        self.demp_before = float(dict_from_frontend.get('demp_before'))
        self.demp_after = float(dict_from_frontend.get('demp_after'))
        self.i_cost_before = float(dict_from_frontend.get('i_cost_before'))
        self.i_cost_after = float(dict_from_frontend.get('i_cost_after'))
        self.shift_QSI_A_before = float(dict_from_frontend.get('shift_QSI_A_before'))
        self.shift_QSI_A_after = float(dict_from_frontend.get('shift_QSI_A_after'))
        self.shift_QSW_A_before = float(dict_from_frontend.get('shift_QSW_A_before'))
        self.shift_QSW_A_after = float(dict_from_frontend.get('shift_QSW_A_after'))
        self.i_cost_world_before = float(dict_from_frontend.get('i_cost_world_before'))
        self.i_cost_world_after = float(dict_from_frontend.get('i_cost_world_after'))


def wheat_exports(input_data):
    # Получаем данные из модели
    mydir = 'C:/Users/Professional/Desktop/parser/wheat_exports/'
    myfile = 'Экспорт_пшеница.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:Q', index_col=0)

    # Список товаров
    list_of_products = df.iloc[:4][['Список товаров', 'Вклад в ИПЦ']]
    print(list_of_products.to_markdown())


input_data = InputDataBase(user_data)
result = wheat_exports(input_data)
