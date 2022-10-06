from pprint import pprint

import numpy as np
import pandas as pd
import os

example_data = {'PW_B1_before': 1500.0, 'PW_B1_after': 1500.0, 'PW_B2_before': 300.0, 'PW_B2_after': 300.0,
                'ER_before': 75.0, 'ER_after': 75.0, 'TD_before': 0.0, 'TD_after': 0.0, 'Pb_B1_before': 82500.0,
                'Pb_B1_after': 82500.0, 'tb_B1_before': 0.0, 'tb_B1_after': 0.7, 'Pb_B2_before': 13875.0,
                'Pb_B2_after': 13875.0, 'tb_B2_before': 0.7, 'tb_B2_after': 0.7, 'PI_B1': 90000.0, 'PI_B2': 15000.0,
                'PI_A': 40000.0, 'QSI_A': 15.0, 'QSW_RUS_A_before': 0.0, 'QSW_RUS_A_after': 0.0, 'i_cost_before': 1.0,
                'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0, 'shift_QSI_A_after': 0.0, 'PI_С': 130000.0,
                'QDI_С': 3.0, 'QDI_B2': 2.0}

user_data = {'PW_B1_before': 1500.0, 'PW_B1_after': 1500.0, 'PW_B2_before': 300.0, 'PW_B2_after': 300.0,
                'ER_before': 75.0, 'ER_after': 75.0, 'TD_before': 0.0, 'TD_after': 0.0, 'Pb_B1_before': 82500.0,
                'Pb_B1_after': 82500.0, 'tb_B1_before': 0.0, 'tb_B1_after': 0.7, 'Pb_B2_before': 13875.0,
                'Pb_B2_after': 13875.0, 'tb_B2_before': 0.7, 'tb_B2_after': 0.7, 'PI_B1': 90000.0, 'PI_B2': 15000.0,
                'PI_A': 40000.0, 'QSI_A': 15.0, 'QSW_RUS_A_before': 0.0, 'QSW_RUS_A_after': 0.0, 'i_cost_before': 1.0,
                'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0, 'shift_QSI_A_after': 0.0, 'PI_С': 130000.0,
                'QDI_С': 3.0, 'QDI_B2': 2.0}


class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.PW_B1_before = float(dict_from_frontend.get('PW_B1_before'))
        self.PW_B1_after = float(dict_from_frontend.get('PW_B1_after'))
        self.PW_B2_before = float(dict_from_frontend.get('PW_B2_before'))
        self.PW_B2_after = float(dict_from_frontend.get('PW_B2_after'))
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.TD_before = float(dict_from_frontend.get('TD_before'))
        self.TD_after = float(dict_from_frontend.get('TD_after'))
        self.Pb_B1_before = float(dict_from_frontend.get('Pb_B1_before'))
        self.Pb_B1_after = float(dict_from_frontend.get('Pb_B1_after'))
        self.tb_B1_before = float(dict_from_frontend.get('tb_B1_before'))
        self.tb_B1_after = float(dict_from_frontend.get('tb_B1_after'))
        self.Pb_B2_before = float(dict_from_frontend.get('Pb_B2_before'))
        self.Pb_B2_after = float(dict_from_frontend.get('Pb_B2_after'))
        self.tb_B2_before = float(dict_from_frontend.get('tb_B2_before'))
        self.tb_B2_after = float(dict_from_frontend.get('tb_B2_after'))
        self.PI_B1 = float(dict_from_frontend.get('PI_B1'))
        self.PI_B2 = float(dict_from_frontend.get('PI_B2'))
        self.PI_A = float(dict_from_frontend.get('PI_A'))
        self.QSI_A = float(dict_from_frontend.get('QSI_A'))
        self.QSW_RUS_A_before = float(dict_from_frontend.get('QSW_RUS_A_before'))
        self.QSW_RUS_A_after = float(dict_from_frontend.get('QSW_RUS_A_after'))
        self.i_cost_before = float(dict_from_frontend.get('i_cost_before'))
        self.i_cost_after = float(dict_from_frontend.get('i_cost_after'))
        self.shift_QSI_A_before = float(dict_from_frontend.get('shift_QSI_A_before'))
        self.shift_QSI_A_after = float(dict_from_frontend.get('shift_QSI_A_after'))
        self.PI_С = float(dict_from_frontend.get('PI_С'))
        self.QDI_С = float(dict_from_frontend.get('QDI_С'))
        self.QDI_B2 = float(dict_from_frontend.get('QDI_B2'))


def oil_export(input_data):
    # Получаем данные из модели
    mydir = '/Users/natalazivlova/Desktop/parser/new_calc/'
    myfile = 'Экспорт_масло_легенда.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:Q', index_col=0)

    # Список товаров
    list_of_products = df[:4][['Список товаров', 'Вклад в ИПЦ']]
    # print(list_of_products.to_markdown())

    # Эластичности по собственной цене
    elasticity_at_its_own_price = df.iloc[6:12, 0:1]
    elasticity_at_its_own_price = elasticity_at_its_own_price.rename(columns={
        'Список товаров': 'Эластичности по собственной цене'})
    # print(elasticity_at_its_own_price.to_markdown())

    # Коэффициенты выхода продукции
    output_coefficients = df.iloc[14:16, 0:1]
    output_coefficients = output_coefficients.rename(columns={
        'Список товаров': 'Коэффициенты выхода продукции'})
    # print(output_coefficients.to_markdown())

    # Цены на мировом рынке товаров группы B
    prices_group_b_products = df.iloc[1:7, 3:9]
    prices_group_b_products.index = np.arange(0, len(prices_group_b_products))
    prices_group_b_products = prices_group_b_products.rename(columns={
        'Unnamed: 4': 'title',
        'Unnamed: 5': 'currency',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })

    # Расчет суммы вывозной таможенной пошлины
    calc_export_customs_duty = df.iloc[9:17, 3:9]
    calc_export_customs_duty.index = np.arange(0, len(calc_export_customs_duty))
    calc_export_customs_duty = calc_export_customs_duty.rename(columns={
        'Unnamed: 4': 'title',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })

    # Внутренний рынок товаров группы B
    domestic_market_of_group_b_products = df.iloc[19:21, 3:8]
    domestic_market_of_group_b_products.index = np.arange(0, len(domestic_market_of_group_b_products))
    domestic_market_of_group_b_products = domestic_market_of_group_b_products.rename(columns={
        'Unnamed: 4': 'title',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })

    # Внутренний рынок товара А
    internal_market_of_product_a = df.iloc[23:26, 3:8]
    internal_market_of_product_a.index = np.arange(0, len(internal_market_of_product_a))
    internal_market_of_product_a = internal_market_of_product_a.rename(columns={
        'Unnamed: 4': 'title',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })

    # Внутреннее производство и баланс товара А
    int_prod_balance_of_goods_a = df.iloc[28:33, 3:9]
    int_prod_balance_of_goods_a.index = np.arange(0, len(int_prod_balance_of_goods_a))
    int_prod_balance_of_goods_a = int_prod_balance_of_goods_a.rename(columns={
        'Unnamed: 4': 'title',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })

    # Внутреннее производство товара С
    int_prod_of_goods_c = df.iloc[35:39, 3:8]
    int_prod_of_goods_c.index = np.arange(0, len(int_prod_of_goods_c))
    int_prod_of_goods_c = int_prod_of_goods_c.rename(columns={
        'Unnamed: 4': 'title',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })

    # Производство и баланс товаров группы B
    prod_bal_of_group_b_goods = df.iloc[41:47, 3:8]
    prod_bal_of_group_b_goods.index = np.arange(0, len(prod_bal_of_group_b_goods))
    prod_bal_of_group_b_goods = prod_bal_of_group_b_goods.rename(columns={
        'Unnamed: 4': 'title',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })

    # Цены
    prices = df.iloc[2:7, 10:16]
    prices.index = np.arange(0, len(prices))
    prices = prices.rename(columns={
        'Результаты': 'title',
        'Unnamed: 12': 'measure',
        'до.1': 'before',
        'после.1': 'after',
        'Прирост': 'increment',
        'Unnamed: 16': 'increment_pr'
    })
    # print(prices.to_markdown())

    # Производство и потребление
    production_and_consumption = df.iloc[9:17, 10:16]
    production_and_consumption.index = np.arange(0, len(production_and_consumption))
    production_and_consumption = production_and_consumption.rename(columns={
        'Результаты': 'title',
        'Unnamed: 12': 'measure',
        'до.1': 'before',
        'после.1': 'after',
        'Прирост': 'increment',
        'Unnamed: 16': 'increment_pr'
    })
    # print(production_and_consumption.to_markdown())

    # Стоимостные эффекты
    cost_effects = df.iloc[20:57, 10:16]
    cost_effects.index = np.arange(0, len(cost_effects))
    cost_effects = cost_effects.rename(columns={
        'Результаты': 'title',
        'Unnamed: 12': 'measure',
        'до.1': 'before',
        'после.1': 'after',
        'Прирост': 'increment',
        'Unnamed: 16': 'increment_pr'
    })
    # print(cost_effects.to_string())

    # вводим новые значения

    # Цены на мировом рынке товаров группы B
    prices_group_b_products.at[0, 'before'] = input_data.PW_B1_before
    prices_group_b_products.at[0, 'after'] = input_data.PW_B1_after
    prices_group_b_products.at[0, 'status'] = prices_group_b_products['status'].pipe(
        lambda x: 'Параметр изменен' if prices_group_b_products.at[0, 'before']
                                        != prices_group_b_products.at[0, 'after'] else 'Параметр не изменен')

    prices_group_b_products.at[1, 'before'] = input_data.PW_B2_before
    prices_group_b_products.at[1, 'after'] = input_data.PW_B2_after
    prices_group_b_products.at[1, 'status'] = prices_group_b_products['status'].pipe(
        lambda x: 'Параметр изменен' if prices_group_b_products.at[1, 'before']
                                        != prices_group_b_products.at[1, 'after'] else 'Параметр не изменен')

    prices_group_b_products.at[4, 'before'] = input_data.ER_before
    prices_group_b_products.at[4, 'after'] = input_data.ER_after
    prices_group_b_products.at[4, 'status'] = prices_group_b_products['status'].pipe(
        lambda x: 'Параметр изменен' if prices_group_b_products.at[4, 'before']
                                        != prices_group_b_products.at[4, 'after'] else 'Параметр не изменен')

    prices_group_b_products.at[5, 'before'] = input_data.TD_before
    prices_group_b_products.at[5, 'after'] = input_data.TD_after
    prices_group_b_products.at[5, 'status'] = prices_group_b_products['status'].pipe(
        lambda x: 'Параметр изменен' if prices_group_b_products.at[5, 'before']
                                        != prices_group_b_products.at[5, 'after'] else 'Параметр не изменен')

    print(prices_group_b_products.to_markdown())

    # Расчет суммы вывозной таможенной пошлины
    calc_export_customs_duty.at[0, 'before'] = input_data.Pb_B1_before
    calc_export_customs_duty.at[0, 'after'] = input_data.Pb_B1_after
    calc_export_customs_duty.at[0, 'status'] = calc_export_customs_duty['status'].pipe(
        lambda x: 'Параметр изменен' if calc_export_customs_duty.at[0, 'before']
                                        != calc_export_customs_duty.at[0, 'after'] else 'Параметр не изменен')

    calc_export_customs_duty.at[1, 'before'] = input_data.tb_B1_before
    calc_export_customs_duty.at[1, 'after'] = input_data.tb_B1_after
    calc_export_customs_duty.at[1, 'status'] = calc_export_customs_duty['status'].pipe(
        lambda x: 'Параметр изменен' if calc_export_customs_duty.at[1, 'before']
                                        != calc_export_customs_duty.at[1, 'after'] else 'Параметр не изменен')

    calc_export_customs_duty.at[4, 'before'] = input_data.Pb_B2_before
    calc_export_customs_duty.at[4, 'after'] = input_data.Pb_B2_after
    calc_export_customs_duty.at[4, 'status'] = calc_export_customs_duty['status'].pipe(
        lambda x: 'Параметр изменен' if calc_export_customs_duty.at[4, 'before']
                                        != calc_export_customs_duty.at[4, 'after'] else 'Параметр не изменен')

    calc_export_customs_duty.at[5, 'before'] = input_data.tb_B2_before
    calc_export_customs_duty.at[5, 'after'] = input_data.tb_B2_after
    calc_export_customs_duty.at[5, 'status'] = calc_export_customs_duty['status'].pipe(
        lambda x: 'Параметр изменен' if calc_export_customs_duty.at[5, 'before']
                                        != calc_export_customs_duty.at[5, 'after'] else 'Параметр не изменен')
    print(calc_export_customs_duty.to_markdown())

    # Внутренний рынок товаров группы B
    domestic_market_of_group_b_products.at[0, 'before'] = input_data.PI_B1
    domestic_market_of_group_b_products.at[1, 'before'] = input_data.PI_B2
    # print(domestic_market_of_group_b_products.to_markdown())

    # Внутренний рынок товара А
    internal_market_of_product_a.at[2, 'before'] = input_data.PI_A
    # print(internal_market_of_product_a.to_markdown())

    # Внутреннее производство и баланс товара А
    int_prod_balance_of_goods_a.at[0, 'before'] = input_data.QSI_A
    int_prod_balance_of_goods_a.at[1, 'before'] = input_data.QSW_RUS_A_before
    int_prod_balance_of_goods_a.at[1, 'after'] = input_data.QSW_RUS_A_after
    int_prod_balance_of_goods_a.at[2, 'before'] = input_data.i_cost_before
    int_prod_balance_of_goods_a.at[2, 'after'] = input_data.i_cost_after
    int_prod_balance_of_goods_a.at[2, 'status'] = int_prod_balance_of_goods_a['status'].pipe(
        lambda x: 'Параметр изменен' if int_prod_balance_of_goods_a.at[2, 'before']
                                        != int_prod_balance_of_goods_a.at[2, 'after'] else 'Параметр не изменен')
    int_prod_balance_of_goods_a.at[3, 'before'] = input_data.shift_QSI_A_before
    int_prod_balance_of_goods_a.at[3, 'after'] = input_data.shift_QSI_A_after
    int_prod_balance_of_goods_a.at[3, 'status'] = int_prod_balance_of_goods_a['status'].pipe(
        lambda x: 'Параметр изменен' if int_prod_balance_of_goods_a.at[3, 'before']
                                        != int_prod_balance_of_goods_a.at[3, 'after'] else 'Параметр не изменен')
    print(int_prod_balance_of_goods_a.to_markdown())

    # Внутреннее производство товара С
    int_prod_of_goods_c.at[0, 'before'] = input_data.PI_С
    int_prod_of_goods_c.at[2, 'before'] = input_data.QDI_С
    # print(internal_production_of_goods_c.to_markdown())

    # Производство и баланс товаров группы B
    prod_bal_of_group_b_goods.at[4, 'before'] = input_data.QDI_B2
    # print(production_and_balance_of_group_b_goods.to_markdown())

    # перерасчет

    # H13
    def func_h13(df, H3, H7, H11, H12):
        return (H3*H7-H11)*H12

    calc_export_customs_duty.at[2, 'before'] = calc_export_customs_duty['before'].pipe(func_h13,
        prices_group_b_products.at[0, 'before'], prices_group_b_products.at[4, 'before'],
        calc_export_customs_duty.at[0, 'before'], calc_export_customs_duty.at[1, 'before'])
    print(f"H13 {calc_export_customs_duty.at[2, 'before']} ")

    # H5
    def func_h5(df, H3, H21, H8, H13, H7):
        return H3-((H21/(1-H8)+H13)/H7)

    prices_group_b_products.at[2, 'before'] = prices_group_b_products['before'].pipe(func_h5,
        prices_group_b_products.at[0, 'before'], domestic_market_of_group_b_products.at[0, 'before'],
        prices_group_b_products.at[5, 'before'], calc_export_customs_duty.at[2, 'before'],
        prices_group_b_products.at[4, 'before'])

    print(f"H5 {prices_group_b_products.at[2, 'before']} ")

    # I5
    prices_group_b_products.at[2, 'after'] = prices_group_b_products.at[2, 'before']
    print(f"I5 {prices_group_b_products.at[2, 'after']} ")

    # H17
    def func_h17(df, H4, H7, H15, H16):
        return (H4*H7-H15)*H16

    calc_export_customs_duty.at[6, 'before'] = calc_export_customs_duty['before'].pipe(func_h17,
        prices_group_b_products.at[1, 'before'], prices_group_b_products.at[4, 'before'],
        calc_export_customs_duty.at[4, 'before'], calc_export_customs_duty.at[5, 'before'])
    print(f"H17 {calc_export_customs_duty.at[6, 'before']} ")

    # H6
    def func_h6(df, H4, H22, H8, H17, H7):
        return H4 - ((H22 / (1 - H8) + H17) / H7)
    prices_group_b_products.at[3, 'before'] = prices_group_b_products['before'].pipe(func_h6,
        prices_group_b_products.at[1, 'before'], domestic_market_of_group_b_products.at[1, 'before'],
        prices_group_b_products.at[5, 'before'], calc_export_customs_duty.at[6, 'before'],
        prices_group_b_products.at[4, 'before'])
    print(f"H6 {prices_group_b_products.at[3, 'before']} ")

    # I6
    prices_group_b_products.at[3, 'after'] = prices_group_b_products.at[3, 'before']
    print(f"I5 {prices_group_b_products.at[3, 'after']} ")

    # H13
    def func_h13(df, H3, H7, H11, H12):
        return (H3*H7-H11)*H12

    calc_export_customs_duty.at[2, 'before'] = calc_export_customs_duty['before'].pipe(func_h13,
        prices_group_b_products.at[0, 'before'], prices_group_b_products.at[4, 'before'],
        calc_export_customs_duty.at[0, 'before'], calc_export_customs_duty.at[1, 'before'])
    print(f"H13 {calc_export_customs_duty.at[2, 'before']} ")

    # I13
    def func_i13(df, I3, I7, I11, I12):
        return (I3*I7-I11)*I12

    calc_export_customs_duty.at[2, 'after'] = calc_export_customs_duty['after'].pipe(func_i13,
        prices_group_b_products.at[0, 'after'], prices_group_b_products.at[4, 'after'],
        calc_export_customs_duty.at[0, 'after'], calc_export_customs_duty.at[1, 'after'])
    print(f"I13 {calc_export_customs_duty.at[2, 'after']} ")

    # H14
    def func_h14(df, H13, H3, H7):
        return H13/(H3*H7)

    calc_export_customs_duty.at[3, 'before'] = calc_export_customs_duty['before'].pipe(func_h14,
        calc_export_customs_duty.at[2, 'before'], prices_group_b_products.at[0, 'before'],
        prices_group_b_products.at[4, 'before'])
    print(f"H14 {calc_export_customs_duty.at[3, 'before']} ")

    # I14
    def func_i14(df, I13, I3, I7):
        return I13/(I3*I7)

    calc_export_customs_duty.at[3, 'after'] = calc_export_customs_duty['after'].pipe(func_i14,
        calc_export_customs_duty.at[2, 'after'], prices_group_b_products.at[0, 'after'],
        prices_group_b_products.at[4, 'after'])
    print(f"I14 {calc_export_customs_duty.at[3, 'after']} ")

    # H17
    def func_h17(df, H4, H7, H15, H16):
        return (H4*H7-H15)*H16

    calc_export_customs_duty.at[6, 'before'] = calc_export_customs_duty['before'].pipe(func_h17,
        prices_group_b_products.at[1, 'before'], prices_group_b_products.at[4, 'before'],
        calc_export_customs_duty.at[4, 'before'], calc_export_customs_duty.at[5, 'before'])
    print(f"H17 {calc_export_customs_duty.at[6, 'before']} ")

    # I17
    def func_i17(df, I4, I7, I15, I16):
        return (I4*I7-I15)*I16

    calc_export_customs_duty.at[6, 'after'] = calc_export_customs_duty['after'].pipe(func_i17,
        prices_group_b_products.at[1, 'after'], prices_group_b_products.at[4, 'after'],
        calc_export_customs_duty.at[4, 'after'], calc_export_customs_duty.at[5, 'after'])
    print(f"I17 {calc_export_customs_duty.at[6, 'after']} ")

    # H18
    def func_h18(df, H17, H4, H7):
        return H17/(H4*H7)

    calc_export_customs_duty.at[7, 'before'] = calc_export_customs_duty['before'].pipe(func_h18,
        calc_export_customs_duty.at[6, 'before'], prices_group_b_products.at[1, 'before'],
        prices_group_b_products.at[4, 'before'])
    print(f"H18 {calc_export_customs_duty.at[7, 'before']} ")

    # I18
    def func_i18(df, I17, I4, I7):
        return I17/(I4*I7)

    calc_export_customs_duty.at[7, 'after'] = calc_export_customs_duty['after'].pipe(func_i18,
        calc_export_customs_duty.at[6, 'after'], prices_group_b_products.at[1, 'after'],
        prices_group_b_products.at[4, 'after'])
    print(f"I18 {calc_export_customs_duty.at[7, 'after']} ")


    result_to_front = {}

    result_to_front[
        'prices_on_world_market_of_group_b_products'] = prices_group_b_products.to_dict(
        'index')
    result_to_front[
        'calculation_of_amount_of_export_customs_duty'] = calc_export_customs_duty.to_dict(
        'index')
    result_to_front['domestic_market_of_group_b_products'] = domestic_market_of_group_b_products.to_dict('index')
    result_to_front['internal_market_of_product_a'] = internal_market_of_product_a.to_dict('index')
    result_to_front['internal_production_and_balance_of_goods_a'] = int_prod_balance_of_goods_a.to_dict(
        'index')
    result_to_front['internal_production_of_goods_c'] = int_prod_of_goods_c.to_dict('index')
    result_to_front['production_and_balance_of_group_b_goods'] = prod_bal_of_group_b_goods.to_dict(
        'index')
    result_to_front['prices'] = prices.to_dict('index')
    result_to_front['production_and_consumption'] = production_and_consumption.to_dict('index')
    result_to_front['cost_effects'] = cost_effects.to_dict('index')
    return result_to_front


input_data = InputDataBase(user_data)
result = oil_export(input_data)
# pprint(result)
