import math
from pprint import pprint

import numpy as np
import pandas as pd
import os

example_data = {'Pc_before': 400.0, 'Pd_before': 240.0, 'Pcif_before': 3.0, 'Pcif_after': 3.0, 'ER_before': 75.0,
                'ER_after': 75.0, 't_in_before': 0.1, 't_in_after': 0.1, 't_out_before': 0.3, 't_out_after': 0.3,
                'Qt_before': 800.0, 'Qt_after': 800.0, 'S_before': 4000.0, 'M_before': 500.0}

user_data = {'Pc_before': 400.0, 'Pd_before': 240.0, 'Pcif_before': 3.0, 'Pcif_after': 3.0, 'ER_before': 75.0,
                'ER_after': 75.0, 't_in_before': 0.1, 't_in_after': 0.1, 't_out_before': 0.3, 't_out_after': 0.3,
                'Qt_before': 800.0, 'Qt_after': 800.0, 'S_before': 4000.0, 'M_before': 500.0}



class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.Pc_before = float(dict_from_frontend.get('Pc_before'))
        self.Pd_before = float(dict_from_frontend.get('Pd_before'))
        self.Pcif_before = float(dict_from_frontend.get('Pcif_before'))
        self.Pcif_after = float(dict_from_frontend.get('Pcif_after'))
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.t_in_before = float(dict_from_frontend.get('t_in_before'))
        self.t_in_after = float(dict_from_frontend.get('t_in_after'))
        self.t_out_before = float(dict_from_frontend.get('t_out_before'))
        self.t_out_after = float(dict_from_frontend.get('t_out_after'))
        self.Qt_before = float(dict_from_frontend.get('Qt_before'))
        self.Qt_after = float(dict_from_frontend.get('Qt_after'))
        self.S_before = float(dict_from_frontend.get('S_before'))
        self.M_before = float(dict_from_frontend.get('M_before'))


def food_products_import(input_data):
    """Получаем данные из модели"""

    mydir = '/Users/natalazivlova/Desktop/parser/food_products_import/food_products_import/'
    myfile = 'Импорт_все_продтовары (2).xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:J')

    # Характеристики ценообразования
    pricing_characteristics = df.iloc[1:11, 0:6]
    pricing_characteristics.index = np.arange(0, len(pricing_characteristics))
    pricing_characteristics = pricing_characteristics.rename(
        columns={'Unnamed: 0': 'title', 'Unnamed: 1': 'designation',
                 'Unnamed: 2': 'measure', 'до': 'before',
                 'после': 'after', 'Прирост,%': 'increment_pr'})

    # Количественные характеристики
    quantitative_characteristics = df.iloc[13:19, 0:6]
    quantitative_characteristics.index = np.arange(0, len(quantitative_characteristics))
    quantitative_characteristics = quantitative_characteristics.rename(columns={'Unnamed: 0': 'title',
                                                                                'Unnamed: 1': 'designation',
                                                                                'Unnamed: 2': 'measure', 'до': 'before',
                                                                                'после': 'after',
                                                                                'Прирост,%': 'increment_pr'})

    # Эффекты
    effects = df.iloc[22:46, 0:4]
    effects.index = np.arange(0, len(effects))
    effects = effects.rename(columns={'Unnamed: 0': 'title', 'Unnamed: 1': 'meaning', 'Unnamed: 2': 'measure',
                                      'до': 'increment'})

    # Значения параметров
    parameter_values = df.iloc[1:9, 7:10]
    parameter_values.index = np.arange(0, len(parameter_values))
    parameter_values = parameter_values.rename(columns={'Unnamed: 7': 'title', 'Unnamed: 8': 'designation',
                                                        'Unnamed: 9': 'values'})

    # Уравнения
    equations = df.iloc[10:17, 7:10]
    equations.index = np.arange(0, len(equations))
    equations = equations.rename(columns={'Unnamed: 7': 'title', 'Unnamed: 8': 'formulas',
                                          'Unnamed: 9': 'values'})

    """Вводим новые значения"""

    # Характеристики ценообразования
    pricing_characteristics.at[0, 'before'] = input_data.Pc_before
    pricing_characteristics.at[1, 'before'] = input_data.Pd_before
    pricing_characteristics.at[4, 'before'] = input_data.Pcif_before
    pricing_characteristics.at[4, 'after'] = input_data.Pcif_after
    pricing_characteristics.at[5, 'before'] = input_data.ER_before
    pricing_characteristics.at[5, 'after'] = input_data.ER_after
    pricing_characteristics.at[6, 'before'] = input_data.t_in_before
    pricing_characteristics.at[6, 'after'] = input_data.t_in_after
    pricing_characteristics.at[7, 'before'] = input_data.t_out_before
    pricing_characteristics.at[7, 'after'] = input_data.t_out_after
    pricing_characteristics.at[8, 'before'] = input_data.Qt_before
    pricing_characteristics.at[8, 'after'] = input_data.Qt_after

    # Количественные характеристики
    quantitative_characteristics.at[0, 'before'] = input_data.S_before
    quantitative_characteristics.at[2, 'before'] = input_data.M_before

    """Перерасчет ячеек с новыми значениями"""


    # F7
    pricing_characteristics.at[4, 'increment_pr'] = pricing_characteristics.at[4, 'after'] / \
                                                    pricing_characteristics.at[4, 'before'] - 1

    # F8
    pricing_characteristics.at[5, 'increment_pr'] = pricing_characteristics.at[5, 'after'] / \
                                                    pricing_characteristics.at[5, 'before'] - 1

    # I16
    def func_i16(df, D9, D17, D11, J9, D10):
        return D9 + math.exp(min(0, (D17 - (D11 + 0.001)) / (D11 + 0.001) * J9)) / (
                    1 + math.exp(-abs(D17 - (D11 + 0.001)) / (D11 + 0.001) * J9)) * (D10 - D9)

    equations.at[4, 'formulas'] = equations['formulas'].pipe(func_i16, pricing_characteristics.at[6, 'before'],
                                                             quantitative_characteristics.at[2, 'before'],
                                                             pricing_characteristics.at[8, 'before'],
                                                             parameter_values.at[6, 'values'],
                                                             pricing_characteristics.at[7, 'before']
                                                             )



    # D12
    pricing_characteristics.at[9, 'before'] = equations.at[4, 'formulas']

    # I12
    def func_i12(df, E7, D7, E8, D8, E12, D12):
        return np.log(E7) - np.log(D7) + np.log(E8) - np.log(D8) + (np.log(E12 + 1) - np.log(D12 + 1))

    equations.at[0, 'formulas'] = equations['formulas'].pipe(func_i12, pricing_characteristics.at[4, 'after'],
                                                             pricing_characteristics.at[4, 'before'],
                                                             pricing_characteristics.at[5, 'after'],
                                                             pricing_characteristics.at[5, 'before'],
                                                             pricing_characteristics.at[9, 'after'],
                                                             pricing_characteristics.at[9, 'before'])

    # D5
    def func_d5(df, D7, D8, D12):
        return D7 * D8 * (1 + D12)

    pricing_characteristics.at[2, 'before'] = pricing_characteristics['before'].pipe(func_d5,
                                                                                     pricing_characteristics.at[
                                                                                         4, 'before'],
                                                                                     pricing_characteristics.at[
                                                                                         5, 'before'],
                                                                                     pricing_characteristics.at[
                                                                                         9, 'before'])

    # E5
    def func_e5(df, E7, E8, E12):
        return E7 * E8 * (1 + E12)

    pricing_characteristics.at[2, 'after'] = pricing_characteristics['after'].pipe(func_e5,
                                                                                   pricing_characteristics.at[
                                                                                       4, 'after'],
                                                                                   pricing_characteristics.at[
                                                                                       5, 'after'],
                                                                                   pricing_characteristics.at[
                                                                                       9, 'after'])
    # F5
    pricing_characteristics.at[2, 'increment_pr'] = pricing_characteristics.at[2, 'after'] / \
                                                    pricing_characteristics.at[2, 'before'] - 1

    # D19
    def func_d14(df, D4, D15, D5, D17):
        return D4 * D15 / (D4 * D15 + D5 * D17)

    quantitative_characteristics.at[4, 'before'] = quantitative_characteristics['before'].pipe(func_d14,
                                                                                               pricing_characteristics.at[
                                                                                                   1, 'before'],
                                                                                               quantitative_characteristics.at[
                                                                                                   0, 'before'],
                                                                                               pricing_characteristics.at[
                                                                                                   2, 'before'],
                                                                                               quantitative_characteristics.at[
                                                                                                   2, 'before'])

    # D20
    quantitative_characteristics.at[5, 'before'] = 1 - quantitative_characteristics.at[4, 'before']

    # J6
    def func_j6(df, J5, J3, D20):
        return (J5 + J3) * D20

    parameter_values.at[3, 'values'] = parameter_values['values'].pipe(func_j6, parameter_values.at[2, 'values'],
                                                                       parameter_values.at[0, 'values'],
                                                                       quantitative_characteristics.at[5, 'before'])

    # J7
    def func_j7(df, J3, D19, J5, D20):
        return J3 * D19 - J5 * D20

    parameter_values.at[4, 'values'] = parameter_values['values'].pipe(func_j7, parameter_values.at[0, 'values'],
                                                                       quantitative_characteristics.at[4, 'before'],
                                                                       parameter_values.at[2, 'values'],
                                                                       quantitative_characteristics.at[5, 'before'])

    # J8
    def func_j8(df, J6, J4, J7):
        return J6 / (J4 - J7)

    parameter_values.at[5, 'values'] = parameter_values['values'].pipe(func_j8, parameter_values.at[3, 'values'],
                                                                       parameter_values.at[1, 'values'],
                                                                       parameter_values.at[4, 'values'])

    # I13
    def func_i13(df, J8, I12):
        return J8 * I12

    equations.at[1, 'formulas'] = equations['formulas'].pipe(func_i13, parameter_values.at[5, 'values'],
                                                             equations.at[0, 'formulas'])

    # E4
    def func_e4(df, D4, I13):
        return D4 * math.exp(I13)

    pricing_characteristics.at[1, 'after'] = pricing_characteristics['after'].pipe(func_e4,
                                                                                   pricing_characteristics.at[
                                                                                       1, 'before'],
                                                                                   equations.at[1, 'formulas'])

    # F4
    pricing_characteristics.at[1, 'increment_pr'] = pricing_characteristics.at[1, 'after'] / \
                                                    pricing_characteristics.at[1, 'before'] - 1

    # I14
    def func_i14(df, I13, J4):
        return I13 * J4

    equations.at[2, 'formulas'] = equations['formulas'].pipe(func_i14, equations.at[1, 'formulas'],
                                                             parameter_values.at[1, 'values'])

    # E15
    def func_e15(df, D15, I14):
        return D15 * math.exp(I14)

    quantitative_characteristics.at[0, 'after'] = quantitative_characteristics['after'].pipe(func_e15,
                                                                                             quantitative_characteristics.at[
                                                                                                 0, 'before'],
                                                                                             equations.at[
                                                                                                 2, 'formulas'])

    # F15
    quantitative_characteristics.at[0, 'increment_pr'] = quantitative_characteristics.at[0, 'after'] / \
                                                         quantitative_characteristics.at[0, 'before'] - 1

    # D16
    quantitative_characteristics.at[1, 'before'] = quantitative_characteristics.at[0, 'before']

    # D6
    def func_d6(df, D4, D16, D17, D5):
        return D4 * D16 / (D16 + D17) + D5 * D17 / (D16 + D17)

    pricing_characteristics.at[3, 'before'] = pricing_characteristics['before'].pipe(func_d6,
                                                                                     pricing_characteristics.at[
                                                                                         1, 'before'],
                                                                                     quantitative_characteristics.at[
                                                                                         1, 'before'],
                                                                                     quantitative_characteristics.at[
                                                                                         2, 'before'],
                                                                                     pricing_characteristics.at[
                                                                                         2, 'before'])

    # D18
    quantitative_characteristics.at[3, 'before'] = quantitative_characteristics.at[1, 'before'] + \
                                                   quantitative_characteristics.at[2, 'before']

    # E16
    quantitative_characteristics.at[1, 'after'] = quantitative_characteristics.at[0, 'after']

    # F16
    quantitative_characteristics.at[1, 'increment_pr'] = quantitative_characteristics.at[1, 'after'] / \
                                                         quantitative_characteristics.at[1, 'before'] - 1

    # I15
    def func_i15(df, I14, J5, J8, I12):
        return I14 + J5 * (J8 - 1) * I12

    equations.at[3, 'formulas'] = equations['formulas'].pipe(func_i15, equations.at[2, 'formulas'],
                                                             parameter_values.at[2, 'values'],
                                                             parameter_values.at[5, 'values'],
                                                             equations.at[0, 'formulas'])

    # E17
    def func_e17(df, D17, I15):
        return D17 * math.exp(I15)

    quantitative_characteristics.at[2, 'after'] = quantitative_characteristics['after'].pipe(func_e17,
                                                                                             quantitative_characteristics.at[
                                                                                                 2, 'before'],
                                                                                             equations.at[
                                                                                                 3, 'formulas'])

    # F17
    quantitative_characteristics.at[2, 'increment_pr'] = quantitative_characteristics.at[2, 'after'] / \
                                                         quantitative_characteristics.at[2, 'before'] - 1

    # J16
    def func_j16(df, E9, E17, E11, J9, E10):
        return E9+math.exp(min(0, (E17-(E11+0.001))/(E11+0.001)*J9))/(1+math.exp(-abs(E17-(E11+0.001))/(E11+0.001)*J9))*(E10-E9)

    equations.at[4, 'values'] = equations['values'].pipe(func_j16, pricing_characteristics.at[6, 'after'],
                                                         quantitative_characteristics.at[2, 'after'],
                                                         pricing_characteristics.at[8, 'after'],
                                                         parameter_values.at[6, 'values'],
                                                         pricing_characteristics.at[7, 'after'])

    # I17
    equations.at[5, 'formulas'] = equations.at[4, 'values'] - pricing_characteristics.at[9, 'after']

    # E6
    def func_e6(df, E4, E16, E17, E5):
        return E4 * E16 / (E16 + E17) + E5 * E17 / (E16 + E17)

    pricing_characteristics.at[3, 'after'] = pricing_characteristics['after'].pipe(func_e6, pricing_characteristics.at[1, 'after'],
                                                                                   quantitative_characteristics.at[
                                                                                       1, 'after'],
                                                                                   quantitative_characteristics.at[
                                                                                       2, 'after'],
                                                                                   pricing_characteristics.at[
                                                                                       2, 'after'])

    # F6
    pricing_characteristics.at[3, 'increment_pr'] = pricing_characteristics.at[3, 'after'] / \
                                                    pricing_characteristics.at[3, 'before'] - 1

    # E3
    def func_e3(df, D3, D6, E6):
        return D3 - D6 + E6

    pricing_characteristics.at[0, 'after'] = pricing_characteristics['after'].pipe(func_e3,
                                                                                   pricing_characteristics.at[
                                                                                       0, 'before'],
                                                                                   pricing_characteristics.at[
                                                                                       3, 'before'],
                                                                                   pricing_characteristics.at[
                                                                                       3, 'after'])

    # F3
    pricing_characteristics.at[0, 'increment_pr'] = pricing_characteristics.at[0, 'after'] / \
                                                    pricing_characteristics.at[0, 'before'] - 1

    # E18
    quantitative_characteristics.at[3, 'after'] = quantitative_characteristics.at[1, 'after'] + \
                                                  quantitative_characteristics.at[2, 'after']

    # F18
    quantitative_characteristics.at[3, 'increment_pr'] = quantitative_characteristics.at[3, 'after'] / \
                                                         quantitative_characteristics.at[3, 'before'] - 1

    # E19
    def func_e19(df, E4, E15, E5, E17):
        return E4*E15/(E4*E15+E5*E17)

    quantitative_characteristics.at[4, 'after'] = quantitative_characteristics['after'].pipe(func_e19,
                                                                    pricing_characteristics.at[1, 'after'],
                                                                    quantitative_characteristics.at[0, 'after'],
                                                                    pricing_characteristics.at[2, 'after'],
                                                                    quantitative_characteristics.at[2, 'after'])

    # E20
    quantitative_characteristics.at[5, 'after'] = 1 - quantitative_characteristics.at[4, 'after']

    if (equations.at[5, 'formulas']) ** 2 < 0.000001:
        solution = True
    else:
        solution = False

    # B24
    effects.at[0, 'meaning'] = quantitative_characteristics.at[0, 'after'] - quantitative_characteristics.at[
        0, 'before']
    # D24
    effects.at[0, 'increment'] = effects.at[0, 'meaning'] / quantitative_characteristics.at[0, 'before']
    # B25
    effects.at[1, 'meaning'] = quantitative_characteristics.at[3, 'after'] - quantitative_characteristics.at[
        3, 'before']
    # D25
    effects.at[1, 'increment'] = effects.at[1, 'meaning'] / quantitative_characteristics.at[3, 'before']
    # B26
    effects.at[2, 'meaning'] = quantitative_characteristics.at[2, 'after'] - quantitative_characteristics.at[
        2, 'before']
    # D26
    effects.at[2, 'increment'] = effects.at[2, 'meaning'] / quantitative_characteristics.at[2, 'before']

    # B29
    def func_b29(df, E7, E8, E17, D7, D8, D17):
        return -(E7 * E8 * E17 - D7 * D8 * D17)

    effects.at[5, 'meaning'] = effects['meaning'].pipe(func_b29, pricing_characteristics.at[4, 'after'],
                                                       pricing_characteristics.at[5, 'after'],
                                                       quantitative_characteristics.at[2, 'after'],
                                                       pricing_characteristics.at[4, 'before'],
                                                       pricing_characteristics.at[5, 'before'],
                                                       quantitative_characteristics.at[2, 'before'])

    # D29
    def func_d29(df, B29, D7, D8, D17):
        return B29 / (D7 * D8 * D17)

    effects.at[5, 'increment'] = effects['increment'].pipe(func_d29, effects.at[5, 'meaning'],
                                                           pricing_characteristics.at[4, 'before'],
                                                           pricing_characteristics.at[5, 'before'],
                                                           quantitative_characteristics.at[2, 'before'])

    # B30
    def func_b30(df, E5, E12, E17, D5, D12, D17):
        return E5 * (1 - 1 / (1 + E12)) * E17 - D5 * (1 - 1 / (1 + D12)) * D17

    effects.at[6, 'meaning'] = effects['meaning'].pipe(func_b30, pricing_characteristics.at[2, 'after'],
                                                       pricing_characteristics.at[9, 'after'],
                                                       quantitative_characteristics.at[2, 'after'],
                                                       pricing_characteristics.at[2, 'before'],
                                                       pricing_characteristics.at[9, 'before'],
                                                       quantitative_characteristics.at[2, 'before'])

    # D30
    def func_d30(df, B30, D5, D12, D17):
        return B30 / (D5 * (1 - 1 / (1 + D12)) * D17)

    effects.at[6, 'increment'] = effects['increment'].pipe(func_d30, effects.at[6, 'meaning'],
                                                           pricing_characteristics.at[2, 'before'],
                                                           pricing_characteristics.at[9, 'before'],
                                                           quantitative_characteristics.at[2, 'before'])

    # B32
    def func_b32(df, D15, E4, D4, E15):
        return D15 * (E4 - D4) + 0.5 * (E4 - D4) * (E15 - D15)

    effects.at[8, 'meaning'] = effects['meaning'].pipe(func_b32, quantitative_characteristics.at[0, 'before'],
                                                       pricing_characteristics.at[1, 'after'],
                                                       pricing_characteristics.at[1, 'before'],
                                                       quantitative_characteristics.at[0, 'after'])

    # B33
    def func_b33(df, D18, E3, D3, E18):
        return -(D18 * (E3 - D3) + 0.5 * (E3 - D3) * (E18 - D18))

    effects.at[9, 'meaning'] = effects['meaning'].pipe(func_b33, quantitative_characteristics.at[3, 'before'],
                                                       pricing_characteristics.at[0, 'after'],
                                                       pricing_characteristics.at[0, 'before'],
                                                       quantitative_characteristics.at[3, 'after'])

    # B34
    def func_b34(df, B32, B33, B30):
        return B32 + B33 + B30

    effects.at[10, 'meaning'] = effects['meaning'].pipe(func_b34, effects.at[8, 'meaning'],
                                                        effects.at[9, 'meaning'],
                                                        effects.at[6, 'meaning'])

    # B37
    def func_b37(df, D18, E3, D3, E18):
        return D18 * (E3 - D3) + 0.5 * (E3 - D3) * (E18 - D18)

    effects.at[13, 'meaning'] = effects['meaning'].pipe(func_b37, quantitative_characteristics.at[3, 'before'],
                                                        pricing_characteristics.at[0, 'after'],
                                                        pricing_characteristics.at[0, 'before'],
                                                        quantitative_characteristics.at[3, 'after'])

    # B38
    def func_b38(df, D3, E18, D18, E3):
        return D3 * (E18 - D18) + 0.5 * (E3 - D3) * (E18 - D18)

    effects.at[14, 'meaning'] = effects['meaning'].pipe(func_b38, pricing_characteristics.at[0, 'before'],
                                                        quantitative_characteristics.at[3, 'after'],
                                                        quantitative_characteristics.at[3, 'before'],
                                                        pricing_characteristics.at[0, 'after'])

    # B36
    effects.at[12, 'meaning'] = effects.at[13, 'meaning'] + effects.at[14, 'meaning']

    # B41
    def func_b41(df, D15, E4, D4, E15):
        return D15 * (E4 - D4) + 0.5 * (E4 - D4) * (E15 - D15)

    effects.at[17, 'meaning'] = effects['meaning'].pipe(func_b41, quantitative_characteristics.at[0, 'before'],
                                                        pricing_characteristics.at[1, 'after'],
                                                        pricing_characteristics.at[1, 'before'],
                                                        quantitative_characteristics.at[0, 'after'])

    # B42
    def func_b42(df, D4, E15, D15, E4):
        return D4 * (E15 - D15) + 0.5 * (E4 - D4) * (E15 - D15)

    effects.at[18, 'meaning'] = effects['meaning'].pipe(func_b42, pricing_characteristics.at[1, 'before'],
                                                        quantitative_characteristics.at[0, 'after'],
                                                        quantitative_characteristics.at[0, 'before'],
                                                        pricing_characteristics.at[1, 'after'])

    # B40
    effects.at[16, 'meaning'] = effects.at[17, 'meaning'] + effects.at[18, 'meaning']

    # B45
    effects.at[21, 'meaning'] = pricing_characteristics.at[0, 'after'] - pricing_characteristics.at[0, 'before']
    # D45
    effects.at[21, 'increment'] = effects.at[21, 'meaning'] / pricing_characteristics.at[0, 'before']

    # B46
    def func_b46(df, D45, J10):
        return D45 * J10 / 100

    effects.at[22, 'meaning'] = effects['meaning'].pipe(func_b46, effects.at[21, 'increment'],
                                                        parameter_values.at[7, 'values'])

    result_to_front = {
        'table1': [
            {
                'id': '1',
                'title': pricing_characteristics.at[0, 'title'],
                'params': pricing_characteristics.at[0, 'designation'],
                'measure': pricing_characteristics.at[0, 'measure'],
                'basebalance': pricing_characteristics.at[0, 'before'],
                'newbalance': pricing_characteristics.at[0, 'after'].round(decimals=2),
                'growthpercent': (pricing_characteristics.at[0, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '2',
                'title': pricing_characteristics.at[1, 'title'],
                'params': pricing_characteristics.at[1, 'designation'],
                'measure': pricing_characteristics.at[1, 'measure'],
                'basebalance': pricing_characteristics.at[1, 'before'],
                'newbalance': pricing_characteristics.at[1, 'after'].round(decimals=2),
                'growthpercent': (pricing_characteristics.at[1, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '3',
                'title': pricing_characteristics.at[2, 'title'],
                'params': pricing_characteristics.at[2, 'designation'],
                'measure': pricing_characteristics.at[2, 'measure'],
                'basebalance': pricing_characteristics.at[2, 'before'].round(decimals=2),
                'newbalance': pricing_characteristics.at[2, 'after'].round(decimals=2),
                'growthpercent': (pricing_characteristics.at[2, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '4',
                'title': pricing_characteristics.at[3, 'title'],
                'params': pricing_characteristics.at[3, 'designation'],
                'measure': pricing_characteristics.at[3, 'measure'],
                'basebalance': pricing_characteristics.at[3, 'before'].round(decimals=2),
                'newbalance': pricing_characteristics.at[3, 'after'].round(decimals=2),
                'growthpercent': (pricing_characteristics.at[3, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '5',
                'title': pricing_characteristics.at[4, 'title'],
                'params': pricing_characteristics.at[4, 'designation'],
                'measure': pricing_characteristics.at[4, 'measure'],
                'basebalance': pricing_characteristics.at[4, 'before'],
                'newbalance': pricing_characteristics.at[4, 'after'],
                'growthpercent': (pricing_characteristics.at[4, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '6',
                'title': pricing_characteristics.at[5, 'title'],
                'params': pricing_characteristics.at[5, 'designation'],
                'measure': pricing_characteristics.at[5, 'measure'],
                'basebalance': pricing_characteristics.at[5, 'before'],
                'newbalance': pricing_characteristics.at[5, 'after'],
                'growthpercent': (pricing_characteristics.at[5, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '7',
                'title': pricing_characteristics.at[6, 'title'],
                'params': pricing_characteristics.at[6, 'designation'],
                'measure': '',
                'basebalance': pricing_characteristics.at[6, 'before'],
                'newbalance': pricing_characteristics.at[6, 'after'],
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '8',
                'title': pricing_characteristics.at[7, 'title'],
                'params': pricing_characteristics.at[7, 'designation'],
                'measure': '',
                'basebalance': pricing_characteristics.at[7, 'before'],
                'newbalance': pricing_characteristics.at[7, 'after'],
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '9',
                'title': pricing_characteristics.at[8, 'title'],
                'params': pricing_characteristics.at[8, 'designation'],
                'measure': pricing_characteristics.at[8, 'measure'],
                'basebalance': pricing_characteristics.at[8, 'before'],
                'newbalance': pricing_characteristics.at[8, 'after'],
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '10',
                'title': pricing_characteristics.at[9, 'title'],
                'params': pricing_characteristics.at[9, 'designation'],
                'measure': '',
                'basebalance': pricing_characteristics.at[9, 'before'].round(decimals=2),
                'newbalance': pricing_characteristics.at[9, 'after'].round(decimals=2),
                "editBase": 'false',
                "editNew": 'false'
            }
        ],
        "table2": [
            {
                'id': '1',
                'title': quantitative_characteristics.at[0, 'title'],
                'params': quantitative_characteristics.at[0, 'designation'],
                'measure': quantitative_characteristics.at[0, 'measure'],
                'basebalance': quantitative_characteristics.at[0, 'before'],
                'newbalance': quantitative_characteristics.at[0, 'after'].round(decimals=2),
                'growthpercent': (quantitative_characteristics.at[0, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '2',
                'title': quantitative_characteristics.at[1, 'title'],
                'params': quantitative_characteristics.at[1, 'designation'],
                'measure': quantitative_characteristics.at[1, 'measure'],
                'basebalance': quantitative_characteristics.at[1, 'before'].round(decimals=2),
                'newbalance': quantitative_characteristics.at[1, 'after'].round(decimals=2),
                'growthpercent': (quantitative_characteristics.at[1, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '3',
                'title': quantitative_characteristics.at[2, 'title'],
                'params': quantitative_characteristics.at[2, 'designation'],
                'measure': quantitative_characteristics.at[2, 'measure'],
                'basebalance': quantitative_characteristics.at[2, 'before'],
                'newbalance': quantitative_characteristics.at[2, 'after'].round(decimals=2),
                'growthpercent': (quantitative_characteristics.at[2, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '4',
                'title': quantitative_characteristics.at[3, 'title'],
                'params': quantitative_characteristics.at[3, 'designation'],
                'measure': quantitative_characteristics.at[3, 'measure'],
                'basebalance': quantitative_characteristics.at[3, 'before'].round(decimals=2),
                'newbalance': quantitative_characteristics.at[3, 'after'].round(decimals=2),
                'growthpercent': (quantitative_characteristics.at[3, 'increment_pr'] * 100).round(decimals=3),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '5',
                'title': quantitative_characteristics.at[4, 'title'],
                'params': quantitative_characteristics.at[4, 'designation'],
                'measure': '',
                'basebalance': quantitative_characteristics.at[4, 'before'].round(decimals=2),
                'newbalance': quantitative_characteristics.at[4, 'after'].round(decimals=2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '6',
                'title': quantitative_characteristics.at[5, 'title'],
                'params': quantitative_characteristics.at[5, 'designation'],
                'measure': '',
                'basebalance': quantitative_characteristics.at[5, 'before'].round(decimals=2),
                'newbalance': quantitative_characteristics.at[5, 'after'].round(decimals=2),
                "editBase": 'false',
                "editNew": 'false'
            }
        ],
        "fintable1": [
            {
                "id": "1",
                "title": effects.at[0, 'title'],
                "growth": effects.at[0, 'meaning'].round(decimals=2),
                "measure": effects.at[0, 'measure'],
                "growthpercent": (effects.at[0, 'increment'] * 100).round(decimals=3)
            },
            {
                "id": "2",
                "title": effects.at[1, 'title'],
                "growth": effects.at[1, 'meaning'].round(decimals=2),
                "measure": effects.at[1, 'measure'],
                "growthpercent": (effects.at[1, 'increment'] * 100).round(decimals=3)
            },
            {
                "id": "3",
                "title": effects.at[2, 'title'],
                "growth": effects.at[2, 'meaning'].round(decimals=2),
                "measure": effects.at[2, 'measure'],
                "growthpercent": (effects.at[2, 'increment'] * 100).round(decimals=3)
            }
        ],
        "fintable2": [
            {
                "id": "1",
                "title": effects.at[5, 'title'],
                "growth": effects.at[5, 'meaning'].round(decimals=2),
                "measure": effects.at[5, 'measure'],
                "growthpercent": (effects.at[5, 'increment'] * 100).round(decimals=3)
            },
            {
                "id": "2",
                "title": effects.at[6, 'title'],
                "growth": effects.at[6, 'meaning'].round(decimals=2),
                "measure": effects.at[6, 'measure'],
                "growthpercent": (effects.at[6, 'increment'] * 100).round(decimals=3)
            }
        ],
        "fintable3": [
            {
                "id": "1",
                "title": effects.at[8, 'title'],
                "growth": effects.at[8, 'meaning'].round(decimals=2),
                "measure": effects.at[8, 'measure']
            },
            {
                "id": "2",
                "title": effects.at[9, 'title'],
                "growth": effects.at[9, 'meaning'].round(decimals=2),
                "measure": effects.at[9, 'measure']
            },
            {
                "id": "3",
                "title": effects.at[10, 'title'],
                "growth": effects.at[10, 'meaning'].round(decimals=2),
                "measure": effects.at[10, 'measure']
            }
        ],
        "fintable4": [
            {
                "id": "1",
                "title": effects.at[12, 'title'],
                "growth": effects.at[12, 'meaning'].round(decimals=2),
                "measure": effects.at[12, 'measure']
            },
            {
                "id": "2",
                "title": effects.at[13, 'title'],
                "growth": effects.at[13, 'meaning'].round(decimals=2),
                "measure": effects.at[13, 'measure']
            },
            {
                "id": "3",
                "title": effects.at[14, 'title'],
                "growth": effects.at[14, 'meaning'].round(decimals=2),
                "measure": effects.at[14, 'measure']
            }
        ],
        "fintable5": [
            {
                "id": "1",
                "title": effects.at[16, 'title'],
                "growth": effects.at[16, 'meaning'].round(decimals=2),
                "measure": effects.at[16, 'measure']
            },
            {
                "id": "2",
                "title": effects.at[17, 'title'],
                "growth": effects.at[17, 'meaning'].round(decimals=2),
                "measure": effects.at[17, 'measure']
            },
            {
                "id": "3",
                "title": effects.at[18, 'title'],
                "growth": effects.at[18, 'meaning'].round(decimals=2),
                "measure": effects.at[18, 'measure']
            }
        ],
        "fintable6": [
            {
                "id": "1",
                "title": effects.at[21, 'title'],
                "growth": effects.at[21, 'meaning'].round(decimals=2),
                "measure": effects.at[21, 'measure'],
                "growthpercent": (effects.at[21, 'increment'] * 100).round(decimals=3)
            },
            {
                "id": "2",
                "title": effects.at[22, 'title'],
                "growth": effects.at[22, 'meaning'].round(decimals=2)
            }
        ],
        "finding_solution": solution
    }

    print(effects.to_markdown())
    return result_to_front




input_data = InputDataBase(user_data)
result = food_products_import(input_data)
print(result)
