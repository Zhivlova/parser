import cmath
import math
from pprint import pprint

import numpy as np
import pandas as pd
import os

from mpmath import fsum
from numpy import sqrt

example_data = {'PW_A_const_before': 228.0, 'PW_A_const_after': 228.798691500235, 'PW_A_shift_before': 0.0, 'PW_A_shift_after': 0.0,
             'ER_before': 72.32, 'ER_after': 72.32, 'CT_before': 59.0, 'TD_before': 0.0, 'TD_after': 0.0,
             'Pb_before': 15000.0, 'Pb_after': 15000.0, 'Pb2_before': 375.0, 'Pb2_after': 375.0,
             'Pb3_before': 400.0, 'Pb3_after': 400.0, 't1_before': 0.0, 't1_after': 0.7, 't2_before': 0.8,
             't2_after': 0.8, 't3_before': 0.9, 't3_after': 0.9, 'demp_before': 0.1, 'demp_after': 0.1,
             'QSI_A_before': 76.882, 'i_cost_before': 1.0, 'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0,
             'shift_QSI_A_after': 0.0, 'QDI_С1_before': 14.03, 'QDI_A_C1_before': 15.129,
             'SpI_C1_before': 1883521.0, 'QDI_С2_before': 13.297, 'QDI_A_C2_before': 17.736,
             'SpI_C2_before': 3505628.0, 'QS_exRUS_A_before': 678.67, 'QD_A_before': 191.191,
             'QD_exRUS_A_before': 524.002, 'shift_QSW_A_before': 0.0, 'shift_QSW_A_after': 0.0,
             'i_cost_world_before': 1.0, 'i_cost_world_after': 1.0}

user_data = {'PW_A_const_before': 228.0, 'PW_A_const_after': 228.798691500235, 'PW_A_shift_before': 0.0, 'PW_A_shift_after': 0.0,
             'ER_before': 72.32, 'ER_after': 72.32, 'CT_before': 59.0, 'TD_before': 0.0, 'TD_after': 0.0,
             'Pb_before': 15000.0, 'Pb_after': 15000.0, 'Pb2_before': 375.0, 'Pb2_after': 375.0,
             'Pb3_before': 400.0, 'Pb3_after': 400.0, 't1_before': 0.0, 't1_after': 0.7, 't2_before': 0.8,
             't2_after': 0.8, 't3_before': 0.9, 't3_after': 0.9, 'demp_before': 0.1, 'demp_after': 0.1,
             'QSI_A_before': 76.882, 'i_cost_before': 1.0, 'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0,
             'shift_QSI_A_after': 0.0, 'QDI_С1_before': 14.03, 'QDI_A_C1_before': 15.129,
             'SpI_C1_before': 1883521.0, 'QDI_С2_before': 13.297, 'QDI_A_C2_before': 17.736,
             'SpI_C2_before': 3505628.0, 'QS_exRUS_A_before': 678.67, 'QD_A_before': 191.191,
             'QD_exRUS_A_before': 524.002, 'shift_QSW_A_before': 0.0, 'shift_QSW_A_after': 0.0,
             'i_cost_world_before': 1.0, 'i_cost_world_after': 1.0}


class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.PW_A_const_before = float(dict_from_frontend.get('PW_A_const_before'))
        self.PW_A_const_after = float(dict_from_frontend.get('PW_A_const_after'))
        self.PW_A_shift_before = float(dict_from_frontend.get('PW_A_shift_before'))
        self.PW_A_shift_after = float(dict_from_frontend.get('PW_A_shift_after'))
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.CT_before = float(dict_from_frontend.get('CT_before'))
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
        self.QSI_A_before = float(dict_from_frontend.get('QSI_A_before'))
        self.i_cost_before = float(dict_from_frontend.get('i_cost_before'))
        self.i_cost_after = float(dict_from_frontend.get('i_cost_after'))
        self.shift_QSI_A_before = float(dict_from_frontend.get('shift_QSI_A_before'))
        self.shift_QSI_A_after = float(dict_from_frontend.get('shift_QSI_A_after'))
        self.QDI_С1_before = float(dict_from_frontend.get('QDI_С1_before'))
        self.QDI_A_C1_before = float(dict_from_frontend.get('QDI_A_C1_before'))
        self.SpI_C1_before = float(dict_from_frontend.get('SpI_C1_before'))
        self.QDI_С2_before = float(dict_from_frontend.get('QDI_С2_before'))
        self.QDI_A_C2_before = float(dict_from_frontend.get('QDI_A_C2_before'))
        self.SpI_C2_before = float(dict_from_frontend.get('SpI_C2_before'))
        self.QS_exRUS_A_before = float(dict_from_frontend.get('QS_exRUS_A_before'))
        self.QD_A_before = float(dict_from_frontend.get('QD_A_before'))
        self.QD_exRUS_A_before = float(dict_from_frontend.get('QD_exRUS_A_before'))
        self.shift_QSW_A_before = float(dict_from_frontend.get('shift_QSW_A_before'))
        self.shift_QSW_A_after = float(dict_from_frontend.get('shift_QSW_A_after'))
        self.i_cost_world_before = float(dict_from_frontend.get('i_cost_world_before'))
        self.i_cost_world_after = float(dict_from_frontend.get('i_cost_world_after'))


def wheat_exports(input_data):
    # Получаем данные из модели
    mydir = '/Users/natalazivlova/Desktop/parser/wheat_exports/'
    myfile = 'Экспорт_пшеница_легенда.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:Q', index_col=0)

    # Список товаров
    list_of_products = df.iloc[0:3, 0:2]
    list_of_products.reset_index(inplace=True)
    list_of_products = list_of_products.rename(columns={
        'Список товаров': 'Обозначение',
        'Unnamed: 1': 'Список товаров'})

    # Эластичности по собственной цене
    elasticity_at_price = df.iloc[5:14, 0:1]
    elasticity_at_price.reset_index(inplace=True)
    elasticity_at_price = elasticity_at_price.rename(columns={'Список товаров': 'Обозначение',
                                                              'Unnamed: 1': 'Эластичности по собственной цене'})

    # Цены на мировом рынке
    prices_on_world_market = df.iloc[1:7, 3:9]
    prices_on_world_market.index = np.arange(0, len(prices_on_world_market))
    prices_on_world_market = prices_on_world_market.rename(
        columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure', 'Unnamed: 6': 'designation',
                 'до': 'before', 'после': 'after', 'Unnamed: 9': 'status'})

    # Расчет суммы вывозной таможенной пошлины
    calc_customs_duty = df.iloc[9:20, 3:9]
    calc_customs_duty.index = np.arange(0, len(calc_customs_duty))
    calc_customs_duty = calc_customs_duty.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                          'Unnamed: 6': 'designation', 'до': 'before', 'после': 'after',
                                                          'Unnamed: 9': 'status'})

    # Внутренние цены с учетом демпфера
    int_prices_inc_dempfer = df.iloc[22:25, 3:9]
    int_prices_inc_dempfer.index = np.arange(0, len(int_prices_inc_dempfer))
    int_prices_inc_dempfer = int_prices_inc_dempfer.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                                    'Unnamed: 6': 'designation', 'до': 'before',
                                                                    'после': 'after', 'Unnamed: 9': 'status'})

    # Внутреннее производство товара А
    int_prod_product_a = df.iloc[27:31, 3:9]
    int_prod_product_a.index = np.arange(0, len(int_prod_product_a))
    int_prod_product_a = int_prod_product_a.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                            'Unnamed: 6': 'designation', 'до': 'before',
                                                            'после': 'after', 'Unnamed: 9': 'status'})

    # Внутреннее производство товара С1
    int_prod_product_c1 = df.iloc[33:40, 3:8]
    int_prod_product_c1.index = np.arange(0, len(int_prod_product_c1))

    int_prod_product_c1 = int_prod_product_c1.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                              'Unnamed: 6': 'designation', 'до': 'before',
                                                              'после': 'after'})

    # Внутреннее производство товара С2
    int_prod_product_c2 = df.iloc[42:49, 3:8]
    int_prod_product_c2.index = np.arange(0, len(int_prod_product_c2))

    int_prod_product_c2 = int_prod_product_c2.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                              'Unnamed: 6': 'designation', 'до': 'before',
                                                              'после': 'after'})

    # Прочее использование и баланс товара А
    other_use_prod_a = df.iloc[51:54, 3:8]
    other_use_prod_a.index = np.arange(0, len(other_use_prod_a))

    other_use_prod_a = other_use_prod_a.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                        'Unnamed: 6': 'designation', 'до': 'before',
                                                        'после': 'after'})

    # Мировой рынок товара А
    world_market_good_a = df.iloc[56:68, 3:9]
    world_market_good_a.index = np.arange(0, len(world_market_good_a))

    world_market_good_a = world_market_good_a.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                              'Unnamed: 6': 'designation', 'до': 'before',
                                                              'после': 'after', 'Unnamed: 9': 'status'})

    # Цены
    prices = df.iloc[2:8, 10:17]
    prices.index = np.arange(0, len(prices))
    prices = prices.rename(columns={'Результаты': 'title', 'Unnamed: 12': 'measure', 'до.1': 'before',
                                    'после.1': 'after', 'Прирост': 'increment', 'Unnamed: 16': 'increment_pr'})

    # Производство и потребление
    production_and_consumption = df.iloc[10:15, 10:17]
    production_and_consumption.index = np.arange(0, len(production_and_consumption))
    production_and_consumption = production_and_consumption.rename(columns={'Результаты': 'title',
                                                                            'Unnamed: 12': 'measure',
                                                                            'до.1': 'before',
                                                                            'после.1': 'after',
                                                                            'Прирост': 'increment',
                                                                            'Unnamed: 16': 'increment_pr'})

    # Стоимостные эффекты
    cost_effects = df.iloc[17:46, 10:17]
    cost_effects.index = np.arange(0, len(cost_effects))
    cost_effects = cost_effects.rename(columns={'Результаты': 'title', 'Unnamed: 12': 'measure',
                                                'до.1': 'before', 'после.1': 'after',
                                                'Прирост': 'increment', 'Unnamed: 16': 'increment_pr'})

    """Вводим новые значения"""

    # Цены на мировом рынке
    prices_on_world_market.at[0, 'before'] = input_data.PW_A_const_before
    prices_on_world_market.at[0, 'after'] = input_data.PW_A_const_after

    prices_on_world_market.at[1, 'before'] = input_data.PW_A_shift_before
    prices_on_world_market.at[1, 'after'] = input_data.PW_A_shift_after
    prices_on_world_market.at[1, 'status'] = prices_on_world_market['status'].pipe(lambda x: 'Параметр изменен' if
    prices_on_world_market.at[1, 'before'] != prices_on_world_market.at[1, 'after'] else 'Параметр не изменен')

    prices_on_world_market.at[3, 'before'] = input_data.ER_before
    prices_on_world_market.at[3, 'after'] = input_data.ER_after
    prices_on_world_market.at[3, 'status'] = prices_on_world_market['status'].pipe(lambda x: 'Параметр изменен' if
    prices_on_world_market.at[3, 'before'] != prices_on_world_market.at[3, 'after'] else 'Параметр не изменен')

    prices_on_world_market.at[4, 'before'] = input_data.CT_before
    prices_on_world_market.at[4, 'status'] = prices_on_world_market['status'].pipe(lambda x: 'Параметр изменен' if
    prices_on_world_market.at[4, 'before'] != prices_on_world_market.at[4, 'after'] else 'Параметр не изменен')

    prices_on_world_market.at[5, 'before'] = input_data.TD_before
    prices_on_world_market.at[5, 'after'] = input_data.TD_after
    prices_on_world_market.at[5, 'status'] = prices_on_world_market['status'].pipe(lambda x: 'Параметр изменен' if
    prices_on_world_market.at[5, 'before'] != prices_on_world_market.at[5, 'after'] else 'Параметр не изменен')

    # Расчет суммы вывозной таможенной пошлины
    calc_customs_duty.at[0, 'before'] = input_data.Pb_before
    calc_customs_duty.at[0, 'after'] = input_data.Pb_after
    calc_customs_duty.at[0, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен' if
    calc_customs_duty.at[0, 'before'] != calc_customs_duty.at[0, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[1, 'before'] = input_data.Pb2_before
    calc_customs_duty.at[1, 'after'] = input_data.Pb2_after
    calc_customs_duty.at[1, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен' if
    calc_customs_duty.at[1, 'before'] != calc_customs_duty.at[1, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[2, 'before'] = input_data.Pb3_before
    calc_customs_duty.at[2, 'after'] = input_data.Pb3_after
    calc_customs_duty.at[2, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен' if
    calc_customs_duty.at[2, 'before'] != calc_customs_duty.at[2, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[3, 'before'] = input_data.t1_before
    calc_customs_duty.at[3, 'after'] = input_data.t1_after
    calc_customs_duty.at[3, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен' if
    calc_customs_duty.at[3, 'before'] != calc_customs_duty.at[3, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[4, 'before'] = input_data.t2_before
    calc_customs_duty.at[4, 'after'] = input_data.t2_after
    calc_customs_duty.at[4, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен' if
    calc_customs_duty.at[4, 'before'] != calc_customs_duty.at[4, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[5, 'before'] = input_data.t3_before
    calc_customs_duty.at[5, 'after'] = input_data.t3_after
    calc_customs_duty.at[5, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен' if
    calc_customs_duty.at[5, 'before'] != calc_customs_duty.at[5, 'after'] else 'Параметр не изменен')

    # Внутренние цены с учетом демпфера
    int_prices_inc_dempfer.at[1, 'before'] = input_data.demp_before
    int_prices_inc_dempfer.at[1, 'after'] = input_data.demp_after
    int_prices_inc_dempfer.at[1, 'status'] = int_prices_inc_dempfer['status'].pipe(lambda x: 'Параметр изменен' if
    int_prices_inc_dempfer.at[1, 'before'] != int_prices_inc_dempfer.at[1, 'after'] else 'Параметр не изменен')

    # Внутреннее производство товара А
    int_prod_product_a.at[0, 'before'] = input_data.QSI_A_before

    int_prod_product_a.at[1, 'before'] = input_data.i_cost_before
    int_prod_product_a.at[1, 'after'] = input_data.i_cost_after
    int_prod_product_a.at[1, 'status'] = int_prod_product_a['status'].pipe(lambda x: 'Параметр изменен' if
    int_prod_product_a.at[1, 'before'] != int_prod_product_a.at[1, 'after'] else 'Параметр не изменен')

    int_prod_product_a.at[2, 'before'] = input_data.shift_QSI_A_before
    int_prod_product_a.at[2, 'after'] = input_data.shift_QSI_A_after
    int_prod_product_a.at[2, 'status'] = int_prod_product_a['status'].pipe(lambda x: 'Параметр изменен' if
    int_prod_product_a.at[2, 'before'] != int_prod_product_a.at[2, 'after'] else 'Параметр не изменен')

    # Внутреннее производство товара С1
    int_prod_product_c1.at[0, 'before'] = input_data.QDI_С1_before

    int_prod_product_c1.at[2, 'before'] = input_data.QDI_A_C1_before

    int_prod_product_c1.at[5, 'before'] = input_data.SpI_C1_before

    # Внутреннее производство товара С2
    int_prod_product_c2.at[0, 'before'] = input_data.QDI_С2_before

    int_prod_product_c2.at[2, 'before'] = input_data.QDI_A_C2_before

    int_prod_product_c2.at[5, 'before'] = input_data.SpI_C2_before

    # Мировой рынок товара А
    world_market_good_a.at[0, 'before'] = input_data.QS_exRUS_A_before

    world_market_good_a.at[1, 'before'] = input_data.QD_A_before

    world_market_good_a.at[2, 'before'] = input_data.QD_exRUS_A_before

    world_market_good_a.at[8, 'before'] = input_data.shift_QSW_A_before
    world_market_good_a.at[8, 'after'] = input_data.shift_QSW_A_after
    world_market_good_a.at[8, 'status'] = world_market_good_a['status'].pipe(lambda x: 'Параметр изменен' if
    world_market_good_a.at[8, 'before'] != world_market_good_a.at[8, 'after'] else 'Параметр не изменен')

    world_market_good_a.at[9, 'before'] = input_data.i_cost_world_before
    world_market_good_a.at[9, 'after'] = input_data.i_cost_world_after
    world_market_good_a.at[9, 'status'] = world_market_good_a['status'].pipe(lambda x: 'Параметр изменен' if
    world_market_good_a.at[9, 'before'] != world_market_good_a.at[9, 'after'] else 'Параметр не изменен')

    """Перерасчет ячеек с новыми значениями"""

    # H5
    def func_h5(df, H4, H3):
        return H4 + H3

    prices_on_world_market.at[2, 'before'] = prices_on_world_market['before'].pipe(func_h5,
                                                                                   prices_on_world_market.at[
                                                                                       1, 'before'],
                                                                                   prices_on_world_market.at[
                                                                                       0, 'before'])

    # I5
    def func_i5(df, I4, I3):
        return I4 + I3

    prices_on_world_market.at[2, 'after'] = prices_on_world_market['after'].pipe(func_i5,
                                                                                 prices_on_world_market.at[1, 'after'],
                                                                                 prices_on_world_market.at[0, 'after'])

    # I7
    prices_on_world_market.at[4, 'after'] = prices_on_world_market.at[4, 'before']

    # H17
    def func_h17(df, H5, H6, H11, H14):
        return (H5 * H6 - H11) * H14

    calc_customs_duty.at[6, 'before'] = calc_customs_duty['before'].pipe(func_h17,
                                                                         prices_on_world_market.at[2, 'before'],
                                                                         prices_on_world_market.at[3, 'before'],
                                                                         calc_customs_duty.at[0, 'before'],
                                                                         calc_customs_duty.at[3, 'before'])

    # I17
    def func_i17(df, I5, I6, I11, I14):
        return (I5 * I6 - I11) * I14

    calc_customs_duty.at[6, 'after'] = calc_customs_duty['after'].pipe(func_h17, prices_on_world_market.at[2, 'after'],
                                                                       prices_on_world_market.at[3, 'after'],
                                                                       calc_customs_duty.at[0, 'after'],
                                                                       calc_customs_duty.at[3, 'after'])
    print(calc_customs_duty.at[3, 'after'])
    # H18
    def func_h18(df, H5, H12, H6, H15, H11, H14):
        return (H5 - H12) * H6 * H15 + (H12 * H6 - H11) * H14

    calc_customs_duty.at[7, 'before'] = calc_customs_duty['before'].pipe(func_h18,
                                                                         prices_on_world_market.at[2, 'before'],
                                                                         calc_customs_duty.at[1, 'before'],
                                                                         prices_on_world_market.at[3, 'before'],
                                                                         calc_customs_duty.at[4, 'before'],
                                                                         calc_customs_duty.at[0, 'before'],
                                                                         calc_customs_duty.at[3, 'before'])

    # I18
    def func_i18(df, I5, I12, I6, I15, I11, I14):
        return (I5 - I12) * I6 * I15 + (I12 * I6 - I11) * I14

    calc_customs_duty.at[7, 'after'] = calc_customs_duty['after'].pipe(func_i18,
                                                                       prices_on_world_market.at[2, 'after'],
                                                                       calc_customs_duty.at[1, 'after'],
                                                                       prices_on_world_market.at[3, 'after'],
                                                                       calc_customs_duty.at[4, 'after'],
                                                                       calc_customs_duty.at[0, 'after'],
                                                                       calc_customs_duty.at[3, 'after'])

    # H19
    def func_h19(df, H5, H13, H6, H16, H12, H15, H11, H14):
        return (H5 - H13) * H6 * H16 + (H13 - H12) * H6 * H15 + (H12 * H6 - H11) * H14

    calc_customs_duty.at[8, 'before'] = calc_customs_duty['before'].pipe(func_h19,
                                                                         prices_on_world_market.at[2, 'before'],
                                                                         calc_customs_duty.at[2, 'before'],
                                                                         prices_on_world_market.at[3, 'before'],
                                                                         calc_customs_duty.at[5, 'before'],
                                                                         calc_customs_duty.at[1, 'before'],
                                                                         calc_customs_duty.at[4, 'before'],
                                                                         calc_customs_duty.at[0, 'before'],
                                                                         calc_customs_duty.at[3, 'before'])

    # I19
    def func_i19(df, I5, I13, I6, I16, I12, I15, I11, I14):
        return (I5 - I13) * I6 * I16 + (I13 - I12) * I6 * I15 + (I12 * I6 - I11) * I14

    calc_customs_duty.at[8, 'after'] = calc_customs_duty['after'].pipe(func_i19,
                                                                       prices_on_world_market.at[2, 'after'],
                                                                       calc_customs_duty.at[2, 'after'],
                                                                       prices_on_world_market.at[3, 'after'],
                                                                       calc_customs_duty.at[5, 'after'],
                                                                       calc_customs_duty.at[1, 'after'],
                                                                       calc_customs_duty.at[4, 'after'],
                                                                       calc_customs_duty.at[0, 'after'],
                                                                       calc_customs_duty.at[3, 'after'])

    # H20
    def func_h20(df, H5, H12, H17, H13, H18, H19):
        if H5 < H12:
            H20 = H17
        elif H5 < H13:
            H20 = H18
        else:
            H20 = H19
        return H20

    calc_customs_duty.at[9, 'before'] = calc_customs_duty['before'].pipe(func_h20,
                                                                         prices_on_world_market.at[2, 'before'],
                                                                         calc_customs_duty.at[1, 'before'],
                                                                         calc_customs_duty.at[6, 'before'],
                                                                         calc_customs_duty.at[2, 'before'],
                                                                         calc_customs_duty.at[7, 'before'],
                                                                         calc_customs_duty.at[8, 'before'])

    # I20
    def func_i20(df, I3, I12, I17, I13, I18, I19):
        if I3 < I12:
            I20 = I17
        elif I3 < I13:
            I20 = I18
        else:
            I20 = I19
        return I20

    calc_customs_duty.at[9, 'after'] = calc_customs_duty['after'].pipe(func_i20,
                                                                       prices_on_world_market.at[0, 'after'],
                                                                       calc_customs_duty.at[1, 'after'],
                                                                       calc_customs_duty.at[6, 'after'],
                                                                       calc_customs_duty.at[2, 'after'],
                                                                       calc_customs_duty.at[7, 'after'],
                                                                       calc_customs_duty.at[8, 'after'])

    # H21
    def func_h21(df, H20, H5, H6):
        return H20 / (H5 * H6)

    calc_customs_duty.at[10, 'before'] = calc_customs_duty['before'].pipe(func_h21,
                                                                          calc_customs_duty.at[9, 'before'],
                                                                          prices_on_world_market.at[2, 'before'],
                                                                          prices_on_world_market.at[3, 'before'])

    # I21
    def func_i21(df, I20, I5, I6):
        return I20 / (I5 * I6)

    calc_customs_duty.at[10, 'after'] = calc_customs_duty['after'].pipe(func_i21,
                                                                        calc_customs_duty.at[9, 'after'],
                                                                        prices_on_world_market.at[2, 'after'],
                                                                        prices_on_world_market.at[3, 'after'])

    # H24
    def func_h24(df, H5, H7, H6, H20, H8):
        return ((H5 - H7) * H6 - H20) * (1 - H8)

    int_prices_inc_dempfer.at[0, 'before'] = int_prices_inc_dempfer['before'].pipe(func_h24,
                                                                                   prices_on_world_market.at[
                                                                                       2, 'before'],
                                                                                   prices_on_world_market.at[
                                                                                       4, 'before'],
                                                                                   prices_on_world_market.at[
                                                                                       3, 'before'],
                                                                                   calc_customs_duty.at[9, 'before'],
                                                                                   prices_on_world_market.at[
                                                                                       5, 'before'])

    # I24
    def func_i24(df, I5, I7, I6, I20, I8):
        return ((I5 - I7) * I6 - I20) * (1 - I8)

    int_prices_inc_dempfer.at[0, 'after'] = int_prices_inc_dempfer['after'].pipe(func_i24,
                                                                                 prices_on_world_market.at[2, 'after'],
                                                                                 prices_on_world_market.at[4, 'after'],
                                                                                 prices_on_world_market.at[3, 'after'],
                                                                                 calc_customs_duty.at[9, 'after'],
                                                                                 prices_on_world_market.at[5, 'after'])

    # H47
    def func_h47(df, H46, H44):
        return H46 / H44

    int_prod_product_c2.at[3, 'before'] = int_prod_product_c2['before'].pipe(func_h47,
                                                                             int_prod_product_c2.at[2, 'before'],
                                                                             int_prod_product_c2.at[0, 'before'])
    # I47
    int_prod_product_c2.at[3, 'after'] = int_prod_product_c2.at[3, 'before']

    # H38
    def func_h38(df, H37, H35):
        return H37 / H35

    int_prod_product_c1.at[3, 'before'] = int_prod_product_c1['before'].pipe(func_h38,
                                                                             int_prod_product_c1.at[2, 'before'],
                                                                             int_prod_product_c1.at[0, 'before'])
    # I38
    int_prod_product_c1.at[3, 'after'] = int_prod_product_c1.at[3, 'before']

    # H54
    def func_h54(df, H53, H44, H47, H35, H38):
        return H53 + H44 * H47 + H35 * H38

    other_use_prod_a.at[1, 'before'] = other_use_prod_a['before'].pipe(func_h54, other_use_prod_a.at[0, 'before'],
                                                                       int_prod_product_c2.at[0, 'before'],
                                                                       int_prod_product_c2.at[3, 'before'],
                                                                       int_prod_product_c1.at[0, 'before'],
                                                                       int_prod_product_c1.at[3, 'before'])

    # H55
    def func_h55(df, H29, H54):
        return H29 - H54

    other_use_prod_a.at[2, 'before'] = other_use_prod_a['before'].pipe(func_h55, int_prod_product_a.at[0, 'before'],
                                                                       other_use_prod_a.at[1, 'before'])
    # H53
    other_use_prod_a.at[0, 'before'] = int_prod_product_a.at[0, 'before'] * 0.098

    # I53
    other_use_prod_a.at[0, 'after'] = int_prod_product_a.at[0, 'after'] * 0.098

    # H26
    def func_h26(df, H24, H20, H55, H29, H25):
        return H24 + H20 * H55 / H29 * H25

    int_prices_inc_dempfer.at[2, 'before'] = int_prices_inc_dempfer['before'].pipe(func_h26,
                                                                                   int_prices_inc_dempfer.at[
                                                                                       0, 'before'],
                                                                                   calc_customs_duty.at[9, 'before'],
                                                                                   other_use_prod_a.at[2, 'before'],
                                                                                   int_prod_product_a.at[0, 'before'],
                                                                                   int_prices_inc_dempfer.at[
                                                                                       1, 'before'])

    # I26
    def func_i26(df, I24, I20, H55, H29, I25):
        return I24 + I20 * H55 / H29 * I25

    int_prices_inc_dempfer.at[2, 'after'] = int_prices_inc_dempfer['after'].pipe(func_i26,
                                                                                 int_prices_inc_dempfer.at[
                                                                                     0, 'after'],
                                                                                 calc_customs_duty.at[9, 'after'],
                                                                                 other_use_prod_a.at[2, 'before'],
                                                                                 int_prod_product_a.at[0, 'before'],
                                                                                 int_prices_inc_dempfer.at[
                                                                                     1, 'after'])

    # H32
    def func_h32(df, H29, H31, H26, H30, B7):
        return H29 / (1 + H31) / (H26 / H30) ** B7

    int_prod_product_a.at[3, 'before'] = int_prod_product_a['before'].pipe(func_h32, int_prod_product_a.at[0, 'before'],
                                                                           int_prod_product_a.at[2, 'before'],
                                                                           int_prices_inc_dempfer.at[2, 'before'],
                                                                           int_prod_product_a.at[1, 'before'],
                                                                           elasticity_at_price.at[
                                                                               0, 'Эластичности по собственной цене'])

    # I29
    def func_i29(df, H32, I31, I26, I30, B7):
        return H32 * (1 + I31) * (I26 / I30) ** B7

    int_prod_product_a.at[0, 'after'] = int_prod_product_a['after'].pipe(func_i29, int_prod_product_a.at[3, 'before'],
                                                                         int_prod_product_a.at[2, 'after'],
                                                                         int_prices_inc_dempfer.at[2, 'after'],
                                                                         int_prod_product_a.at[1, 'after'],
                                                                         elasticity_at_price.at[
                                                                             0, 'Эластичности по собственной цене'])

    # H41
    def func_h41(df, H40, H35):
        return H40 / H35

    int_prod_product_c1.at[6, 'before'] = int_prod_product_c1['before'].pipe(func_h41,
                                                                             int_prod_product_c1.at[5, 'before'],
                                                                             int_prod_product_c1.at[0, 'before'])

    # H36
    def func_h36(df, H35, H41, B8):
        return H35 / (H41 ** B8)

    int_prod_product_c1.at[1, 'before'] = int_prod_product_c1['before'].pipe(func_h36,
                                                                             int_prod_product_c1.at[0, 'before'],
                                                                             int_prod_product_c1.at[6, 'before'],
                                                                             elasticity_at_price.at[
                                                                                 1, 'Эластичности по собственной цене'])

    # I35
    def func_i35(df, H36, I41, B8):
        return H36 * (I41) ** B8

    int_prod_product_c1.at[0, 'after'] = int_prod_product_c1['after'].pipe(func_i35,
                                                                           int_prod_product_c1.at[1, 'before'],
                                                                           int_prod_product_c1.at[6, 'after'],
                                                                           elasticity_at_price.at[
                                                                               1, 'Эластичности по собственной цене'])

    # H39
    def func_h39(df, H41, H38, H24):
        return H41 - H38 * H24

    int_prod_product_c1.at[4, 'before'] = int_prod_product_c1['before'].pipe(func_h39,
                                                                             int_prod_product_c1.at[6, 'before'],
                                                                             int_prod_product_c1.at[3, 'before'],
                                                                             int_prices_inc_dempfer.at[0, 'before'])

    # I39
    int_prod_product_c1.at[4, 'after'] = int_prod_product_c1.at[4, 'before']

    # I41
    def func_i41(df, I38, I24, I39):
        return I38 * I24 + I39

    int_prod_product_c1.at[6, 'after'] = int_prod_product_c1['after'].pipe(func_i41, int_prod_product_c1.at[3, 'after'],
                                                                           int_prices_inc_dempfer.at[0, 'after'],
                                                                           int_prod_product_c1.at[4, 'after'])

    # I40
    def func_i40(df, I35, I41):
        return I35 * I41

    int_prod_product_c1.at[5, 'after'] = int_prod_product_c1['after'].pipe(func_i40, int_prod_product_c1.at[0, 'after'],
                                                                           int_prod_product_c1.at[6, 'after'])

    # H50
    def func_h50(df, H49, H44):
        return H49 / H44

    int_prod_product_c2.at[6, 'before'] = int_prod_product_c2['before'].pipe(func_h50,
                                                                             int_prod_product_c2.at[5, 'before'],
                                                                             int_prod_product_c2.at[0, 'before'])

    # H45
    def func_h45(df, H44, H50, B9):
        return H44 / (H50 ** B9)

    int_prod_product_c2.at[1, 'before'] = int_prod_product_c2['before'].pipe(func_h45,
                                                                             int_prod_product_c2.at[0, 'before'],
                                                                             int_prod_product_c2.at[6, 'before'],
                                                                             elasticity_at_price.at[
                                                                                 2, 'Эластичности по собственной цене'])

    # I44
    def func_i44(df, H45, I50, B9):
        return H45 * (I50) ** B9

    int_prod_product_c2.at[0, 'after'] = int_prod_product_c2['after'].pipe(func_i44,
                                                                           int_prod_product_c2.at[1, 'before'],
                                                                           int_prod_product_c2.at[6, 'after'],
                                                                           elasticity_at_price.at[
                                                                               2, 'Эластичности по собственной цене'])

    # H48
    def func_h48(df, H50, H47, H24):
        return H50 - H47 * H24

    int_prod_product_c2.at[4, 'before'] = int_prod_product_c2['before'].pipe(func_h48,
                                                                             int_prod_product_c2.at[6, 'before'],
                                                                             int_prod_product_c2.at[3, 'before'],
                                                                             int_prices_inc_dempfer.at[0, 'before'])
    # I48
    int_prod_product_c2.at[4, 'after'] = int_prod_product_c2.at[4, 'before']

    # I50
    def func_i50(df, I47, I24, I48):
        return I47 * I24 + I48

    int_prod_product_c2.at[6, 'after'] = int_prod_product_c2['after'].pipe(func_i50, int_prod_product_c2.at[3, 'after'],
                                                                           int_prices_inc_dempfer.at[0, 'after'],
                                                                           int_prod_product_c2.at[4, 'after'])

    # I54
    def func_i54(df, I53, I44, I47, I35, I38):
        return I53 + I44 * I47 + I35 * I38

    other_use_prod_a.at[1, 'after'] = other_use_prod_a['after'].pipe(func_i54, other_use_prod_a.at[0, 'after'],
                                                                     int_prod_product_c2.at[0, 'after'],
                                                                     int_prod_product_c2.at[3, 'after'],
                                                                     int_prod_product_c1.at[0, 'after'],
                                                                     int_prod_product_c1.at[3, 'after'])

    # I55
    def func_i55(df, I29, I54):
        return I29 - I54

    other_use_prod_a.at[2, 'after'] = other_use_prod_a['after'].pipe(func_i55, int_prod_product_a.at[0, 'after'],
                                                                     other_use_prod_a.at[1, 'after'])

    # H61
    def func_h61(df, H58, H60):
        return H58 - H60

    world_market_good_a.at[3, 'before'] = world_market_good_a['before'].pipe(func_h61,
                                                                             world_market_good_a.at[0, 'before'],
                                                                             world_market_good_a.at[2, 'before'])

    # H62
    def func_h62(df, H58, H66, H5, H7, H67, B10):
        return H58 / (1 + H66) / ((H5 - H7) / H67) ** B10

    world_market_good_a.at[4, 'before'] = world_market_good_a['before'].pipe(func_h62,
                                                                             world_market_good_a.at[0, 'before'],
                                                                             world_market_good_a.at[8, 'before'],
                                                                             prices_on_world_market.at[2, 'before'],
                                                                             prices_on_world_market.at[4, 'before'],
                                                                             world_market_good_a.at[9, 'before'],
                                                                             elasticity_at_price.at[
                                                                                 3, 'Эластичности по собственной цене'])

    # I58
    def func_i58(df, H62, I66, I5, I7, I67, B10):
        return H62 * (1 + I66) * ((I5 - I7) / I67) ** B10

    world_market_good_a.at[0, 'after'] = world_market_good_a['after'].pipe(func_i58,
                                                                           world_market_good_a.at[4, 'before'],
                                                                           world_market_good_a.at[8, 'after'],
                                                                           prices_on_world_market.at[2, 'after'],
                                                                           prices_on_world_market.at[4, 'after'],
                                                                           world_market_good_a.at[9, 'after'],
                                                                           elasticity_at_price.at[
                                                                               3, 'Эластичности по собственной цене'])

    # H63
    def func_h63(df, H59, H5, B11):
        return H59 / H5 ** B11

    world_market_good_a.at[5, 'before'] = world_market_good_a['before'].pipe(func_h63,
                                                                             world_market_good_a.at[1, 'before'],
                                                                             prices_on_world_market.at[2, 'before'],
                                                                             elasticity_at_price.at[
                                                                                 4, 'Эластичности по собственной цене'])

    # I59
    def func_i59(df, H63, I3, B11):
        return H63 * I3 ** B11

    world_market_good_a.at[1, 'after'] = world_market_good_a['after'].pipe(func_i59,
                                                                           world_market_good_a.at[5, 'before'],
                                                                           prices_on_world_market.at[0, 'after'],
                                                                           elasticity_at_price.at[
                                                                               4, 'Эластичности по собственной цене'])

    # H64
    def func_h64(df, H60, H5, B11):
        return H60 / H5 ** B11

    world_market_good_a.at[6, 'before'] = world_market_good_a['before'].pipe(func_h64,
                                                                             world_market_good_a.at[2, 'before'],
                                                                             prices_on_world_market.at[2, 'before'],
                                                                             elasticity_at_price.at[
                                                                                 4, 'Эластичности по собственной цене'])

    # I60
    def func_i60(df, H64, I3, B11):
        return H64 * I3 ** B11

    world_market_good_a.at[2, 'after'] = world_market_good_a['after'].pipe(func_i60,
                                                                           world_market_good_a.at[6, 'before'],
                                                                           prices_on_world_market.at[0, 'after'],
                                                                           elasticity_at_price.at[
                                                                               4, 'Эластичности по собственной цене'])

    # I61
    def func_i61(df, I58, I60):
        return I58 - I60

    world_market_good_a.at[3, 'after'] = world_market_good_a['after'].pipe(func_i61, world_market_good_a.at[0, 'after'],
                                                                           world_market_good_a.at[2, 'after'])

    # H65
    def func_h65(df, H55, H61):
        return H55 + H61

    world_market_good_a.at[7, 'before'] = world_market_good_a['before'].pipe(func_h65, other_use_prod_a.at[2, 'before'],
                                                                             world_market_good_a.at[3, 'before'])

    # I65
    def func_i65(df, I55, I61):
        return I55 + I61

    world_market_good_a.at[7, 'after'] = world_market_good_a['after'].pipe(func_i65, other_use_prod_a.at[2, 'after'],
                                                                           world_market_good_a.at[3, 'after'])

    # H68
    def func_h68(df, H59, H65):
        return H59 - H65

    world_market_good_a.at[10, 'before'] = world_market_good_a['before'].pipe(func_h68,
                                                                              world_market_good_a.at[1, 'before'],
                                                                              world_market_good_a.at[7, 'before'])

    # I68
    def func_i68(df, I59, I65):
        return I59 - I65

    world_market_good_a.at[10, 'after'] = world_market_good_a['after'].pipe(func_i68,
                                                                            world_market_good_a.at[1, 'after'],
                                                                            world_market_good_a.at[7, 'after'])
    # N4
    prices.at[0, 'before'] = prices_on_world_market.at[2, 'before']
    # O4
    prices.at[0, 'after'] = prices_on_world_market.at[2, 'after']
    # P4
    prices.at[0, 'increment'] = prices.at[0, 'after'] - prices.at[0, 'before']
    # Q4
    prices.at[0, 'increment_pr'] = prices.at[0, 'after'] / prices.at[0, 'before'] - 1

    # N5
    prices.at[1, 'before'] = int_prices_inc_dempfer.at[0, 'before']
    # O5
    prices.at[1, 'after'] = int_prices_inc_dempfer.at[0, 'after']
    # P5
    prices.at[1, 'increment'] = int_prices_inc_dempfer.at[0, 'after'] - int_prices_inc_dempfer.at[0, 'before']
    # Q5
    prices.at[1, 'increment_pr'] = int_prices_inc_dempfer.at[0, 'after'] / int_prices_inc_dempfer.at[0, 'before'] - 1

    # N6
    prices.at[2, 'before'] = int_prices_inc_dempfer.at[2, 'before']
    # O6
    prices.at[2, 'after'] = int_prices_inc_dempfer.at[2, 'after']
    # P6
    prices.at[2, 'increment'] = int_prices_inc_dempfer.at[2, 'after'] - int_prices_inc_dempfer.at[2, 'before']
    # Q6
    prices.at[2, 'increment_pr'] = int_prices_inc_dempfer.at[2, 'after'] / int_prices_inc_dempfer.at[2, 'before'] - 1

    # N7
    prices.at[3, 'before'] = int_prod_product_c1.at[6, 'before']
    # O7
    prices.at[3, 'after'] = int_prod_product_c1.at[6, 'after']
    # P7
    prices.at[3, 'increment'] = int_prod_product_c1.at[6, 'after'] - int_prod_product_c1.at[6, 'before']
    # Q7
    prices.at[3, 'increment_pr'] = int_prod_product_c1.at[6, 'after'] / int_prod_product_c1.at[6, 'before'] - 1

    # N8
    prices.at[4, 'before'] = int_prod_product_c2.at[6, 'before']
    # O8
    prices.at[4, 'after'] = int_prod_product_c2.at[6, 'after']
    # P8
    prices.at[4, 'increment'] = int_prod_product_c2.at[6, 'after'] - int_prod_product_c2.at[6, 'before']
    # Q8
    prices.at[4, 'increment_pr'] = int_prod_product_c2.at[6, 'after'] / int_prod_product_c2.at[6, 'before'] - 1

    # P9
    def func_p9(df, Q7, C3, Q8, C4):
        return Q7 * C3 / 100 + Q8 * C4 / 100

    prices.at[5, 'increment'] = prices['increment'].pipe(func_p9, prices.at[3, 'increment_pr'],
                                                         list_of_products.at[1, 'Вклад в ИПЦ'],
                                                         prices.at[3, 'increment_pr'],
                                                         list_of_products.at[2, 'Вклад в ИПЦ'])

    # N12
    production_and_consumption.at[0, 'before'] = int_prod_product_a.at[0, 'before']
    # O12
    production_and_consumption.at[0, 'after'] = int_prod_product_a.at[0, 'after']
    # P12
    production_and_consumption.at[0, 'increment'] = int_prod_product_a.at[0, 'after'] - int_prod_product_a.at[
        0, 'before']
    # Q12
    production_and_consumption.at[0, 'increment_pr'] = int_prod_product_a.at[0, 'after'] / int_prod_product_a.at[
        0, 'before'] - 1

    # N13
    production_and_consumption.at[1, 'before'] = other_use_prod_a.at[1, 'before']
    # O13
    production_and_consumption.at[1, 'after'] = other_use_prod_a.at[1, 'after']
    # P13
    production_and_consumption.at[1, 'increment'] = other_use_prod_a.at[1, 'after'] - other_use_prod_a.at[1, 'before']
    # Q13
    production_and_consumption.at[1, 'increment_pr'] = other_use_prod_a.at[1, 'after'] / other_use_prod_a.at[
        1, 'before'] - 1

    # N14
    production_and_consumption.at[2, 'before'] = other_use_prod_a.at[2, 'before']
    # O14
    production_and_consumption.at[2, 'after'] = other_use_prod_a.at[2, 'after']
    # P14
    production_and_consumption.at[2, 'increment'] = other_use_prod_a.at[2, 'after'] - other_use_prod_a.at[2, 'before']
    # Q14
    production_and_consumption.at[2, 'increment_pr'] = other_use_prod_a.at[2, 'after'] / other_use_prod_a.at[
        2, 'before'] - 1

    # N15
    production_and_consumption.at[3, 'before'] = int_prod_product_c1.at[0, 'before']
    # O15
    production_and_consumption.at[3, 'after'] = int_prod_product_c1.at[0, 'after']
    # P15
    production_and_consumption.at[3, 'increment'] = int_prod_product_c1.at[0, 'after'] - int_prod_product_c1.at[
        0, 'before']
    # Q15
    production_and_consumption.at[3, 'increment_pr'] = int_prod_product_c1.at[0, 'after'] / int_prod_product_c1.at[
        0, 'before'] - 1

    # N16
    production_and_consumption.at[4, 'before'] = int_prod_product_c2.at[0, 'before']
    # O16
    production_and_consumption.at[4, 'after'] = int_prod_product_c2.at[0, 'after']
    # P16
    production_and_consumption.at[4, 'increment'] = int_prod_product_c2.at[0, 'after'] - int_prod_product_c2.at[
        0, 'before']
    # Q16
    production_and_consumption.at[4, 'increment_pr'] = int_prod_product_c2.at[0, 'after'] / int_prod_product_c2.at[
        0, 'before'] - 1

    # N19
    def func_n19(df, H5, H6, H55):
        return H5 * H6 * H55

    cost_effects.at[0, 'before'] = cost_effects['before'].pipe(func_n19, prices_on_world_market.at[2, 'before'],
                                                               prices_on_world_market.at[3, 'before'],
                                                               other_use_prod_a.at[2, 'before'])

    # O19
    def func_o19(df, I5, I6, I55):
        return I5 * I6 * I55

    cost_effects.at[0, 'after'] = cost_effects['after'].pipe(func_o19, prices_on_world_market.at[2, 'after'],
                                                             prices_on_world_market.at[3, 'after'],
                                                             other_use_prod_a.at[2, 'after'])
    # P19
    cost_effects.at[0, 'increment'] = cost_effects.at[0, 'after'] - cost_effects.at[0, 'before']
    # Q19
    cost_effects.at[0, 'increment_pr'] = cost_effects.at[0, 'after'] / cost_effects.at[0, 'before'] - 1

    # N20
    def func_n20(df, H20, N14, H25):
        return H20 * N14 * (1 - H25)

    cost_effects.at[1, 'before'] = cost_effects['before'].pipe(func_n20, calc_customs_duty.at[9, 'before'],
                                                               production_and_consumption.at[2, 'before'],
                                                               int_prices_inc_dempfer.at[1, 'before'])

    # O20
    def func_o20(df, I20, O14, I25):
        return I20 * O14 * (1 - I25)

    cost_effects.at[1, 'after'] = cost_effects['after'].pipe(func_o20, calc_customs_duty.at[9, 'after'],
                                                             production_and_consumption.at[2, 'after'],
                                                             int_prices_inc_dempfer.at[1, 'after'])

    # P20
    cost_effects.at[1, 'increment'] = cost_effects.at[1, 'after'] - cost_effects.at[1, 'before']

    # Q20
    def func_q20(df, O20, N20):
        try:
            Q20 = O20 / N20 - 1
        except ZeroDivisionError:
            Q20 = '-'
        else:
            Q20 = '-'
        return Q20

    cost_effects.at[1, 'increment_pr'] = cost_effects['increment_pr'].pipe(func_q20, cost_effects.at[1, 'after'],
                                                                           cost_effects.at[1, 'before'])

    # N23
    def func_n23(df, N12, N6, O6, O12):
        return -(N12 * (N6 - O6) - 0.5 * (N6 - O6) * (N12 - O12))

    cost_effects.at[4, 'before'] = cost_effects['before'].pipe(func_n23, production_and_consumption.at[0, 'before'],
                                                               prices.at[2, 'before'], prices.at[2, 'after'],
                                                               production_and_consumption.at[0, 'after'])

    # N24
    def func_n24(df, N5, O5, N13, O13):
        return (N5 - O5) * N13 + 0.5 * (N5 - O5) * (O13 - N13)

    cost_effects.at[5, 'before'] = cost_effects['before'].pipe(func_n24, prices.at[1, 'before'], prices.at[1, 'after'],
                                                               production_and_consumption.at[1, 'before'],
                                                               production_and_consumption.at[1, 'after'])

    # N25
    def func_n25(df, N7, O7, N15, O15):
        return (N7 - O7) * N15 + 0.5 * (N7 - O7) * (O15 - N15)

    cost_effects.at[6, 'before'] = cost_effects['before'].pipe(func_n25, prices.at[3, 'before'], prices.at[3, 'after'],
                                                               production_and_consumption.at[3, 'before'],
                                                               production_and_consumption.at[3, 'after'])

    # N26
    def func_n26(df, N8, O8, N16, O16):
        return (N8 - O8) * N16 + 0.5 * (N8 - O8) * (O16 - N16)

    cost_effects.at[7, 'before'] = cost_effects['before'].pipe(func_n26, prices.at[4, 'before'], prices.at[4, 'after'],
                                                               production_and_consumption.at[4, 'before'],
                                                               production_and_consumption.at[4, 'after'])

    # N27
    def func_n27(df, N23, N24, P20):
        return N23 + N24 + P20

    cost_effects.at[8, 'before'] = cost_effects['before'].pipe(func_n27, cost_effects.at[4, 'before'],
                                                               cost_effects.at[5, 'before'],
                                                               cost_effects.at[1, 'increment'])

    # N30
    def func_n30(df, N12, O6, N6, O12):
        return N12 * (O6 - N6) + 0.5 * (O6 - N6) * (O12 - N12)

    cost_effects.at[11, 'before'] = cost_effects['before'].pipe(func_n30, production_and_consumption.at[0, 'before'],
                                                                prices.at[2, 'after'], prices.at[2, 'before'],
                                                                production_and_consumption.at[0, 'after'])

    # N31
    def func_n31(df, N6, O12, N12, O6):
        return N6 * (O12 - N12) + 0.5 * (O6 - N6) * (O12 - N12)

    cost_effects.at[12, 'before'] = cost_effects['before'].pipe(func_n31, prices.at[2, 'before'],
                                                                production_and_consumption.at[0, 'after'],
                                                                production_and_consumption.at[0, 'before'],
                                                                prices.at[2, 'after'])
    # N29
    cost_effects.at[10, 'before'] = cost_effects.at[11, 'before'] + cost_effects.at[12, 'before']

    # N34
    def func_n34(df, N15, O7, N7, O15):
        return N15 * (O7 - N7) + 0.5 * (O7 - N7) * (O15 - N15)

    cost_effects.at[15, 'before'] = cost_effects['before'].pipe(func_n34, production_and_consumption.at[3, 'before'],
                                                                prices.at[3, 'after'], prices.at[3, 'before'],
                                                                production_and_consumption.at[3, 'after'])

    # N35
    def func_n35(df, N7, O15, N15, O7):
        return N7 * (O15 - N15) + 0.5 * (O7 - N7) * (O15 - N15)

    cost_effects.at[16, 'before'] = cost_effects['before'].pipe(func_n35, prices.at[3, 'before'],
                                                                production_and_consumption.at[3, 'after'],
                                                                production_and_consumption.at[3, 'before'],
                                                                prices.at[3, 'after'])

    # N33
    cost_effects.at[14, 'before'] = cost_effects.at[15, 'before'] + cost_effects.at[16, 'before']

    # N38
    def func_n38(df, N15, O7, N7, O15):
        return N15 * (O7 - N7) + 0.5 * (O7 - N7) * (O15 - N15)

    cost_effects.at[19, 'before'] = cost_effects['before'].pipe(func_n38, production_and_consumption.at[3, 'before'],
                                                                prices.at[3, 'after'], prices.at[3, 'before'],
                                                                production_and_consumption.at[3, 'after'])

    # N39
    def func_n39(df, N7, O15, N15, O7):
        return N7 * (O15 - N15) + 0.5 * (O15 - N15) * (O7 - N7)

    cost_effects.at[20, 'before'] = cost_effects['before'].pipe(func_n39, prices.at[3, 'before'],
                                                                production_and_consumption.at[3, 'after'],
                                                                production_and_consumption.at[3, 'before'],
                                                                prices.at[3, 'after'])

    # N37
    cost_effects.at[18, 'before'] = cost_effects.at[19, 'before'] + cost_effects.at[20, 'before']

    # N42
    def func_n42(df, N16, O8, N8, O16):
        return N16 * (O8 - N8) + 0.5 * (O8 - N8) * (O16 - N16)

    cost_effects.at[23, 'before'] = cost_effects['before'].pipe(func_n42, production_and_consumption.at[4, 'before'],
                                                                prices.at[4, 'after'], prices.at[4, 'before'],
                                                                production_and_consumption.at[4, 'after'])

    # N43
    def func_n43(df, N8, O16, N16, O8):
        return N8 * (O16 - N16) + 0.5 * (O8 - N8) * (O16 - N16)

    cost_effects.at[24, 'before'] = cost_effects['before'].pipe(func_n43, prices.at[4, 'before'],
                                                                production_and_consumption.at[4, 'after'],
                                                                production_and_consumption.at[4, 'before'],
                                                                prices.at[4, 'after'])
    # N41
    cost_effects.at[22, 'before'] = cost_effects.at[23, 'before'] + cost_effects.at[24, 'before']

    # N46
    def func_n46(df, N16, O8, N8, O16):
        return N16 * (O8 - N8) + 0.5 * (O8 - N8) * (O16 - N16)

    cost_effects.at[27, 'before'] = cost_effects['before'].pipe(func_n46, production_and_consumption.at[4, 'before'],
                                                                prices.at[4, 'after'], prices.at[4, 'before'],
                                                                production_and_consumption.at[4, 'after'])

    # N47
    def func_n47(df, N8, O16, N16, O8):
        return N8 * (O16 - N16) + 0.5 * (O16 - N16) * (O8 - N8)

    cost_effects.at[28, 'before'] = cost_effects['before'].pipe(func_n47, prices.at[4, 'before'],
                                                                production_and_consumption.at[4, 'after'],
                                                                production_and_consumption.at[4, 'before'],
                                                                prices.at[4, 'after'])

    # N45
    cost_effects.at[26, 'before'] = cost_effects.at[27, 'before'] + cost_effects.at[28, 'before']


    if world_market_good_a.at[10, 'after']**2 < 0.000001:
        solution = True
    else:
        solution = False

    result_to_front = {
        'finding_solution': solution}
    return result_to_front


input_data = InputDataBase(user_data)
result = wheat_exports(input_data)
print(result)
