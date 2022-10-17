from pprint import pprint

import numpy as np
import pandas as pd
import os

example_data = {'PW_A_shift_after': 0.0, 'ER_before': 75.0, 'ER_after': 75.0,
                'CT_before': 50.0, 'CT_after': 50.0, 'TD_before': 0.0, 'TD_after': 0.0,
                'Pb_before': 15000.0, 'Pb_after': 15000.0, 'Pb2_before': 375.0,
                'Pb2_after': 375.0, 'Pb3_before': 400.0, 'Pb3_after': 400.0,
                't1_before': 0.7, 't1_after': 0.69, 't2_before': 0.8, 't2_after': 0.8,
                't3_before': 0.9, 't3_after': 0.9, 'demp_before': 0.1, 'demp_after': 0.1,
                'i_cost_before': 1.0, 'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0,
                'shift_QSI_A_after': 0.0, 'shift_QSW_A_before': 0.0,
                'shift_QSW_A_after': 0.0, 'i_cost_world_before': 1.0, 'i_cost_world_after': 1.0}

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
    mydir = '/Users/natalazivlova/Desktop/parser/wheat_exports/'
    myfile = 'Экспорт_пшеница.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:Q')

    # Список товаров
    list_of_products = df.iloc[0:3, 0:2]
    list_of_products.reset_index(inplace=True)
    list_of_products = list_of_products.rename(columns={
        'Список товаров': 'Обозначение',
        'Unnamed: 1': 'Список товаров'})
    # print(list_of_products.to_markdown())

    # Эластичности по собственной цене
    elasticity_at_price = df.iloc[5:14, 0:1]
    elasticity_at_price.reset_index(inplace=True)
    elasticity_at_price = elasticity_at_price.rename(columns={'Список товаров': 'Обозначение',
                                                              'Unnamed: 1': 'Эластичности по собственной цене'})
    # print(elasticity_at_price)

    # Цены на мировом рынке
    prices_on_world_market = df.iloc[1:7, 4:10]
    prices_on_world_market.index = np.arange(0, len(prices_on_world_market))
    prices_on_world_market = prices_on_world_market.rename(
        columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure', 'Unnamed: 6': 'designation',
                 'до': 'before', 'после': 'after', 'Unnamed: 9': 'status'})

    # Расчет суммы вывозной таможенной пошлины
    calc_customs_duty = df.iloc[9:20, 4:10]
    calc_customs_duty.index = np.arange(0, len(calc_customs_duty))
    calc_customs_duty = calc_customs_duty.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                          'Unnamed: 6': 'designation', 'до': 'before', 'после': 'after',
                                                          'Unnamed: 9': 'status'})
    # print(calc_customs_duty.to_markdown())

    # Внутренние цены с учетом демпфера
    int_prices_inc_dempfer = df.iloc[22:25, 4:10]
    int_prices_inc_dempfer.index = np.arange(0, len(int_prices_inc_dempfer))
    int_prices_inc_dempfer = int_prices_inc_dempfer.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                                    'Unnamed: 6': 'designation', 'до': 'before',
                                                                    'после': 'after', 'Unnamed: 9': 'status'})
    # print(int_prices_inc_dempfer.to_markdown())

    # Внутреннее производство товара А
    int_prod_product_a = df.iloc[27:31, 4:10]
    int_prod_product_a.index = np.arange(0, len(int_prod_product_a))
    int_prod_product_a = int_prod_product_a.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                            'Unnamed: 6': 'designation', 'до': 'before',
                                                            'после': 'after', 'Unnamed: 9': 'status'})
    # print(int_prod_product_a.to_markdown())

    # Внутреннее производство товара С1
    int_prod_product_c1 = df.iloc[33:40, 4:9]
    int_prod_product_c1.index = np.arange(0, len(int_prod_product_c1))

    int_prod_product_c1 = int_prod_product_c1.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                              'Unnamed: 6': 'designation', 'до': 'before',
                                                              'после': 'after', 'Unnamed: 9': 'status'})
    # print(int_prod_product_c1.to_markdown())

    # Внутреннее производство товара С2
    int_prod_product_c2 = df.iloc[42:49, 4:9]
    int_prod_product_c2.index = np.arange(0, len(int_prod_product_c2))

    int_prod_product_c2 = int_prod_product_c2.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                              'Unnamed: 6': 'designation', 'до': 'before',
                                                              'после': 'after', 'Unnamed: 9': 'status'})
    # print(int_prod_product_c2.to_markdown())

    # Прочее использование и баланс товара А
    other_use_prod_a = df.iloc[51:54, 4:9]
    other_use_prod_a.index = np.arange(0, len(other_use_prod_a))

    other_use_prod_a = other_use_prod_a.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                        'Unnamed: 6': 'designation', 'до': 'before',
                                                        'после': 'after', 'Unnamed: 9': 'status'})
    # print(other_use_prod_a.to_markdown())

    # Мировой рынок товара А
    world_market_good_a = df.iloc[56:68, 4:10]
    world_market_good_a.index = np.arange(0, len(world_market_good_a))

    world_market_good_a = world_market_good_a.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                              'Unnamed: 6': 'designation', 'до': 'before',
                                                              'после': 'after', 'Unnamed: 9': 'status'})
    # print(world_market_good_a.to_markdown())

    # Цены
    prices = df.iloc[2:8, 11:17]
    prices.index = np.arange(0, len(prices))
    prices = prices.rename(columns={'Результаты': 'title', 'Unnamed: 12': 'measure', 'до.1': 'before',
                                    'после.1': 'after', 'Прирост': 'increment', 'Unnamed: 16': 'increment_pr'})
    # print(prices.to_markdown())

    # Производство и потребление
    production_and_consumption = df.iloc[10:15, 11:17]
    production_and_consumption.index = np.arange(0, len(production_and_consumption))
    production_and_consumption = production_and_consumption.rename(columns={'Результаты': 'title',
                                                                            'Unnamed: 12': 'measure',
                                                                            'до.1': 'before',
                                                                            'после.1': 'after',
                                                                            'Прирост': 'increment',
                                                                            'Unnamed: 16': 'increment_pr'})
    # print(production_and_consumption.to_markdown())

    # Стоимостные эффекты
    cost_effects = df.iloc[17:46, 11:17]
    cost_effects.index = np.arange(0, len(cost_effects))
    cost_effects = cost_effects.rename(columns={'Результаты': 'title', 'Unnamed: 12': 'measure',
                                                'до.1': 'before', 'после.1': 'after',
                                                'Прирост': 'increment', 'Unnamed: 16': 'increment_pr'})
    # print(cost_effects.to_markdown())

    """Вводим новые значения"""

    # Цены на мировом рынке

    prices_on_world_market.at[1, 'after'] = input_data.PW_A_shift_after
    prices_on_world_market.at[1, 'status'] = prices_on_world_market['status'].pipe(lambda x: 'Параметр изменен' if
    prices_on_world_market.at[1, 'before'] != prices_on_world_market.at[1, 'after'] else 'Параметр не изменен')

    prices_on_world_market.at[3, 'before'] = input_data.ER_before
    prices_on_world_market.at[3, 'after'] = input_data.ER_after
    prices_on_world_market.at[3, 'status'] = prices_on_world_market['status'].pipe(lambda x: 'Параметр изменен'
    if prices_on_world_market.at[3, 'before'] != prices_on_world_market.at[3, 'after'] else 'Параметр не изменен')

    prices_on_world_market.at[4, 'before'] = input_data.CT_before
    prices_on_world_market.at[4, 'after'] = input_data.CT_after
    prices_on_world_market.at[4, 'status'] = prices_on_world_market['status'].pipe(lambda x: 'Параметр изменен'
    if prices_on_world_market.at[4, 'before'] != prices_on_world_market.at[4, 'after'] else 'Параметр не изменен')

    prices_on_world_market.at[5, 'before'] = input_data.TD_before
    prices_on_world_market.at[5, 'after'] = input_data.TD_after
    prices_on_world_market.at[5, 'status'] = prices_on_world_market['status'].pipe(lambda x: 'Параметр изменен'
    if prices_on_world_market.at[5, 'before'] != prices_on_world_market.at[5, 'after'] else 'Параметр не изменен')

    # print(prices_on_world_market.to_markdown())

    # Расчет суммы вывозной таможенной пошлины
    calc_customs_duty.at[0, 'before'] = input_data.Pb_before
    calc_customs_duty.at[0, 'after'] = input_data.Pb_after
    calc_customs_duty.at[0, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_customs_duty.at[0, 'before'] != calc_customs_duty.at[0, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[1, 'before'] = input_data.Pb2_before
    calc_customs_duty.at[1, 'after'] = input_data.Pb2_after
    calc_customs_duty.at[1, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_customs_duty.at[1, 'before'] != calc_customs_duty.at[1, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[2, 'before'] = input_data.Pb3_before
    calc_customs_duty.at[2, 'after'] = input_data.Pb3_after
    calc_customs_duty.at[2, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_customs_duty.at[2, 'before'] != calc_customs_duty.at[2, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[3, 'before'] = input_data.t1_before
    calc_customs_duty.at[3, 'after'] = input_data.t1_after
    calc_customs_duty.at[3, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_customs_duty.at[3, 'before'] != calc_customs_duty.at[3, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[4, 'before'] = input_data.t2_before
    calc_customs_duty.at[4, 'after'] = input_data.t2_after
    calc_customs_duty.at[4, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_customs_duty.at[4, 'before'] != calc_customs_duty.at[4, 'after'] else 'Параметр не изменен')

    calc_customs_duty.at[5, 'before'] = input_data.t3_before
    calc_customs_duty.at[5, 'after'] = input_data.t3_after
    calc_customs_duty.at[5, 'status'] = calc_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_customs_duty.at[5, 'before'] != calc_customs_duty.at[5, 'after'] else 'Параметр не изменен')

    # Внутренние цены с учетом демпфера
    int_prices_inc_dempfer.at[1, 'before'] = input_data.demp_before
    int_prices_inc_dempfer.at[1, 'after'] = input_data.demp_after
    int_prices_inc_dempfer.at[1, 'status'] = int_prices_inc_dempfer['status'].pipe(lambda x: 'Параметр изменен'
    if int_prices_inc_dempfer.at[1, 'before'] != int_prices_inc_dempfer.at[1, 'after'] else 'Параметр не изменен')

    # Внутреннее производство товара А
    int_prod_product_a.at[1, 'before'] = input_data.i_cost_before
    int_prod_product_a.at[1, 'after'] = input_data.i_cost_after
    int_prod_product_a.at[0, 'status'] = int_prod_product_a['status'].pipe(lambda x: 'Параметр изменен'
    if int_prod_product_a.at[1, 'before'] != int_prod_product_a.at[1, 'after'] else 'Параметр не изменен')

    int_prod_product_a.at[2, 'before'] = input_data.shift_QSI_A_before
    int_prod_product_a.at[2, 'after'] = input_data.shift_QSI_A_after
    int_prod_product_a.at[1, 'status'] = int_prod_product_a['status'].pipe(lambda x: 'Параметр изменен'
    if int_prod_product_a.at[2, 'before'] != int_prod_product_a.at[2, 'after'] else 'Параметр не изменен')

    # Мировой рынок товара А
    world_market_good_a.at[8, 'before'] = input_data.shift_QSW_A_before
    world_market_good_a.at[8, 'after'] = input_data.shift_QSW_A_after
    world_market_good_a.at[8, 'status'] = world_market_good_a['status'].pipe(lambda x: 'Параметр изменен'
    if world_market_good_a.at[8, 'before'] != world_market_good_a.at[8, 'after'] else 'Параметр не изменен')

    world_market_good_a.at[9, 'before'] = input_data.i_cost_world_before
    world_market_good_a.at[9, 'after'] = input_data.i_cost_world_after
    world_market_good_a.at[9, 'status'] = world_market_good_a['status'].pipe(lambda x: 'Параметр изменен'
    if world_market_good_a.at[9, 'before'] != world_market_good_a.at[9, 'after'] else 'Параметр не изменен')
    print(world_market_good_a.to_markdown())


input_data = InputDataBase(user_data)
result = wheat_exports(input_data)
print(result)
