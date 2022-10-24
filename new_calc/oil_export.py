import numpy as np
import pandas as pd
import os
from pprint import pprint

example_data = {'PW_B1_before': 829.0, 'PW_B1_after': 829.0, 'PW_B2_before': 226.8, 'PW_B2_after': 226.8,
                'ER_before': 72.32, 'ER_after': 72.32, 'TD_before': 0.0, 'TD_after': 0.0, 'Pb_B1_before': 82500.0,
                'Pb_B1_after': 82500.0, 'tb_B1_before': 0.0, 'tb_B1_after': 0.7, 'Pb_B2_before': 13875.0,
                'Pb_B2_after': 13875.0, 'tb_B2_before': 0.0, 'tb_B2_after': 0.7, 'PI_B1': 48942.7, 'PI_B2': 13061.9,
                'PI_A': 23415.2, 'QSI_A': 13.761, 'QSW_RUS_A_before': 0.723, 'QSW_RUS_A_after': 0.0, 'i_cost_before': 1.0,
                'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0, 'shift_QSI_A_after': 0.0, 'PI_С': 106430.8,
                'QDI_С': 2.048, 'QDI_B2': 3.567}

user_data = {'PW_B1_before': 829.0, 'PW_B1_after': 829.0, 'PW_B2_before': 226.8, 'PW_B2_after': 226.8,
                'ER_before': 72.32, 'ER_after': 72.32, 'TD_before': 0.0, 'TD_after': 0.0, 'Pb_B1_before': 82500.0,
                'Pb_B1_after': 82500.0, 'tb_B1_before': 0.0, 'tb_B1_after': 0.7, 'Pb_B2_before': 13875.0,
                'Pb_B2_after': 13875.0, 'tb_B2_before': 0.0, 'tb_B2_after': 0.7, 'PI_B1': 48942.7, 'PI_B2': 13061.9,
                'PI_A': 23415.2, 'QSI_A': 13.761, 'QSW_RUS_A_before': 0.723, 'QSW_RUS_A_after': 0.0, 'i_cost_before': 1.0,
                'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0, 'shift_QSI_A_after': 0.0, 'PI_С': 106430.8,
                'QDI_С': 2.048, 'QDI_B2': 3.567}




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
    """Получаем данные из модели"""

    mydir = 'C:/Users/Professional/Desktop/parser/new_calc/'
    myfile = 'Экспорт_масло_легенда.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:Q', index_col=0)

    # Список товаров
    list_of_products = df[:4][['Список товаров', 'Вклад в ИПЦ']]

    # Эластичности по собственной цене
    elasticity_at_its_own_price = df.iloc[6:12, 0:1]
    elasticity_at_its_own_price = elasticity_at_its_own_price.rename(columns={'Список товаров': 'Эластичности по '
                                                                                                'собственной цене'})

    # Коэффициенты выхода продукции
    output_coefficients = df.iloc[14:16, 0:1]
    output_coefficients = output_coefficients.rename(columns={'Список товаров': 'Коэффициенты выхода продукции'})

    # Цены на мировом рынке товаров группы B
    prices_group_b_products = df.iloc[1:7, 3:9]
    prices_group_b_products.index = np.arange(0, len(prices_group_b_products))
    prices_group_b_products = prices_group_b_products.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'currency',
                                                                      'Unnamed: 6': 'designation', 'до': 'before',
                                                                      'после': 'after', 'Unnamed: 9': 'status'})

    # Расчет суммы вывозной таможенной пошлины
    calc_export_customs_duty = df.iloc[9:17, 3:9]
    calc_export_customs_duty.index = np.arange(0, len(calc_export_customs_duty))
    calc_export_customs_duty = calc_export_customs_duty.rename(columns={'Unnamed: 4': 'title', 'Unnamed: 5': 'measure',
                                                                        'Unnamed: 6': 'designation', 'до': 'before',
                                                                        'после': 'after', 'Unnamed: 9': 'status'})

    # Внутренний рынок товаров группы B
    domestic_market_of_group_b_products = df.iloc[19:21, 3:8]
    domestic_market_of_group_b_products.index = np.arange(0, len(domestic_market_of_group_b_products))
    domestic_market_of_group_b_products = domestic_market_of_group_b_products.rename(columns={'Unnamed: 4': 'title',
                                                                                              'Unnamed: 5': 'measure',
                                                                                              'Unnamed: 6': 'designation',
                                                                                              'до': 'before',
                                                                                              'после': 'after',
                                                                                              'Unnamed: 9': 'status'})
    # Внутренний рынок товара А
    internal_market_of_product_a = df.iloc[23:26, 3:8]
    internal_market_of_product_a.index = np.arange(0, len(internal_market_of_product_a))
    internal_market_of_product_a = internal_market_of_product_a.rename(columns={'Unnamed: 4': 'title',
                                                                                'Unnamed: 5': 'measure',
                                                                                'Unnamed: 6': 'designation',
                                                                                'до': 'before',
                                                                                'после': 'after',
                                                                                'Unnamed: 9': 'status'})
    # Внутреннее производство и баланс товара А
    int_prod_balance_of_goods_a = df.iloc[28:33, 3:9]
    int_prod_balance_of_goods_a.index = np.arange(0, len(int_prod_balance_of_goods_a))
    int_prod_balance_of_goods_a = int_prod_balance_of_goods_a.rename(columns={'Unnamed: 4': 'title',
                                                                              'Unnamed: 5': 'measure',
                                                                              'Unnamed: 6': 'designation',
                                                                              'до': 'before',
                                                                              'после': 'after',
                                                                              'Unnamed: 9': 'status'})
    # Внутреннее производство товара С
    int_prod_of_goods_c = df.iloc[35:39, 3:8]
    int_prod_of_goods_c.index = np.arange(0, len(int_prod_of_goods_c))
    int_prod_of_goods_c = int_prod_of_goods_c.rename(columns={'Unnamed: 4': 'title',
                                                              'Unnamed: 5': 'measure',
                                                              'Unnamed: 6': 'designation',
                                                              'до': 'before',
                                                              'после': 'after',
                                                              'Unnamed: 9': 'status'})
    # Производство и баланс товаров группы B
    prod_bal_of_group_b_goods = df.iloc[41:47, 3:8]
    prod_bal_of_group_b_goods.index = np.arange(0, len(prod_bal_of_group_b_goods))
    prod_bal_of_group_b_goods = prod_bal_of_group_b_goods.rename(columns={'Unnamed: 4': 'title',
                                                                          'Unnamed: 5': 'measure',
                                                                          'Unnamed: 6': 'designation',
                                                                          'до': 'before',
                                                                          'после': 'after',
                                                                          'Unnamed: 9': 'status'
                                                                          })
    # Цены
    prices = df.iloc[2:7, 10:16]
    prices.index = np.arange(0, len(prices))
    prices = prices.rename(columns={'Результаты': 'title', 'Unnamed: 12': 'measure', 'до.1': 'before',
                                    'после.1': 'after', 'Прирост': 'increment', 'Unnamed: 16': 'increment_pr'})
    # Производство и потребление
    production_and_consumption = df.iloc[9:17, 10:16]
    production_and_consumption.index = np.arange(0, len(production_and_consumption))
    production_and_consumption = production_and_consumption.rename(columns={'Результаты': 'title',
                                                                            'Unnamed: 12': 'measure',
                                                                            'до.1': 'before',
                                                                            'после.1': 'after',
                                                                            'Прирост': 'increment',
                                                                            'Unnamed: 16': 'increment_pr'})
    # Стоимостные эффекты
    cost_effects = df.iloc[20:57, 10:16]
    cost_effects.index = np.arange(0, len(cost_effects))
    cost_effects = cost_effects.rename(columns={'Результаты': 'title', 'Unnamed: 12': 'measure',
                                                'до.1': 'before', 'после.1': 'after',
                                                'Прирост': 'increment', 'Unnamed: 16': 'increment_pr'})

    """Вводим новые значения"""

    # Цены на мировом рынке товаров группы B
    prices_group_b_products.at[0, 'before'] = input_data.PW_B1_before
    prices_group_b_products.at[0, 'after'] = input_data.PW_B1_after
    prices_group_b_products.at[0, 'status'] = prices_group_b_products['status'].pipe(lambda x: 'Параметр изменен'
    if prices_group_b_products.at[0, 'before'] != prices_group_b_products.at[0, 'after'] else 'Параметр не изменен')

    prices_group_b_products.at[1, 'before'] = input_data.PW_B2_before
    prices_group_b_products.at[1, 'after'] = input_data.PW_B2_after
    prices_group_b_products.at[1, 'status'] = prices_group_b_products['status'].pipe(lambda x: 'Параметр изменен'
    if prices_group_b_products.at[1, 'before'] != prices_group_b_products.at[1, 'after'] else 'Параметр не изменен')

    prices_group_b_products.at[4, 'before'] = input_data.ER_before
    prices_group_b_products.at[4, 'after'] = input_data.ER_after
    prices_group_b_products.at[4, 'status'] = prices_group_b_products['status'].pipe(lambda x: 'Параметр изменен'
    if prices_group_b_products.at[4, 'before'] != prices_group_b_products.at[4, 'after'] else 'Параметр не изменен')

    prices_group_b_products.at[5, 'before'] = input_data.TD_before
    prices_group_b_products.at[5, 'after'] = input_data.TD_after
    prices_group_b_products.at[5, 'status'] = prices_group_b_products['status'].pipe(lambda x: 'Параметр изменен'
    if prices_group_b_products.at[5, 'before'] != prices_group_b_products.at[5, 'after'] else 'Параметр не изменен')

    # Расчет суммы вывозной таможенной пошлины
    calc_export_customs_duty.at[0, 'before'] = input_data.Pb_B1_before
    calc_export_customs_duty.at[0, 'after'] = input_data.Pb_B1_after
    calc_export_customs_duty.at[0, 'status'] = calc_export_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_export_customs_duty.at[0, 'before'] != calc_export_customs_duty.at[0, 'after'] else 'Параметр не изменен')

    calc_export_customs_duty.at[1, 'before'] = input_data.tb_B1_before
    calc_export_customs_duty.at[1, 'after'] = input_data.tb_B1_after
    calc_export_customs_duty.at[1, 'status'] = calc_export_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_export_customs_duty.at[1, 'before'] != calc_export_customs_duty.at[1, 'after'] else 'Параметр не изменен')

    calc_export_customs_duty.at[4, 'before'] = input_data.Pb_B2_before
    calc_export_customs_duty.at[4, 'after'] = input_data.Pb_B2_after
    calc_export_customs_duty.at[4, 'status'] = calc_export_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_export_customs_duty.at[4, 'before'] != calc_export_customs_duty.at[4, 'after'] else 'Параметр не изменен')

    calc_export_customs_duty.at[5, 'before'] = input_data.tb_B2_before
    calc_export_customs_duty.at[5, 'after'] = input_data.tb_B2_after
    calc_export_customs_duty.at[5, 'status'] = calc_export_customs_duty['status'].pipe(lambda x: 'Параметр изменен'
    if calc_export_customs_duty.at[5, 'before'] != calc_export_customs_duty.at[5, 'after'] else 'Параметр не изменен')

    # Внутренний рынок товаров группы B
    domestic_market_of_group_b_products.at[0, 'before'] = input_data.PI_B1
    domestic_market_of_group_b_products.at[1, 'before'] = input_data.PI_B2

    # Внутренний рынок товара А
    internal_market_of_product_a.at[2, 'before'] = input_data.PI_A

    # Внутреннее производство и баланс товара А
    int_prod_balance_of_goods_a.at[0, 'before'] = input_data.QSI_A
    int_prod_balance_of_goods_a.at[1, 'before'] = input_data.QSW_RUS_A_before
    int_prod_balance_of_goods_a.at[1, 'after'] = input_data.QSW_RUS_A_after
    int_prod_balance_of_goods_a.at[2, 'before'] = input_data.i_cost_before
    int_prod_balance_of_goods_a.at[2, 'after'] = input_data.i_cost_after
    int_prod_balance_of_goods_a.at[2, 'status'] = int_prod_balance_of_goods_a['status'].pipe(
        lambda x: 'Параметр изменен' if int_prod_balance_of_goods_a.at[2, 'before'] !=
                                        int_prod_balance_of_goods_a.at[2, 'after'] else 'Параметр не изменен')
    int_prod_balance_of_goods_a.at[3, 'before'] = input_data.shift_QSI_A_before
    int_prod_balance_of_goods_a.at[3, 'after'] = input_data.shift_QSI_A_after
    int_prod_balance_of_goods_a.at[3, 'status'] = int_prod_balance_of_goods_a['status'].pipe(
        lambda x: 'Параметр изменен' if int_prod_balance_of_goods_a.at[3, 'before'] !=
                                        int_prod_balance_of_goods_a.at[3, 'after'] else 'Параметр не изменен')
    # Внутреннее производство товара С
    int_prod_of_goods_c.at[0, 'before'] = input_data.PI_С
    int_prod_of_goods_c.at[2, 'before'] = input_data.QDI_С

    # Производство и баланс товаров группы B
    prod_bal_of_group_b_goods.at[4, 'before'] = input_data.QDI_B2

    """Перерасчет ячеек с новыми значениями"""

    # H13
    def func_h13(df, H3, H7, H11, H12):
        H13 = (H3 * H7 - H11) * H12
        return max(0, H13)

    calc_export_customs_duty.at[2, 'before'] = calc_export_customs_duty['before'].pipe(func_h13,
                                                                            prices_group_b_products.at[0, 'before'],
                                                                            prices_group_b_products.at[4, 'before'],
                                                                            calc_export_customs_duty.at[0, 'before'],
                                                                            calc_export_customs_duty.at[1, 'before'])

    # H5
    def func_h5(df, H3, H21, H8, H13, H7):
        return H3 - ((H21 / (1 - H8) + H13) / H7)

    prices_group_b_products.at[2, 'before'] = prices_group_b_products['before'].pipe(func_h5,
                    prices_group_b_products.at[0, 'before'], domestic_market_of_group_b_products.at[0, 'before'],
                    prices_group_b_products.at[5, 'before'], calc_export_customs_duty.at[2, 'before'],
                    prices_group_b_products.at[4, 'before'])
    # I5
    prices_group_b_products.at[2, 'after'] = prices_group_b_products.at[2, 'before']

    # H17
    def func_h17(df, H4, H7, H15, H16):
        H17 = (H4 * H7 - H15) * H16
        return max(0, H17)

    calc_export_customs_duty.at[6, 'before'] = calc_export_customs_duty['before'].pipe(func_h17,
                    prices_group_b_products.at[1, 'before'], prices_group_b_products.at[4, 'before'],
                    calc_export_customs_duty.at[4, 'before'], calc_export_customs_duty.at[5, 'before'])

    # H6
    def func_h6(df, H4, H22, H8, H17, H7):
        return H4 - ((H22 / (1 - H8) + H17) / H7)

    prices_group_b_products.at[3, 'before'] = prices_group_b_products['before'].pipe(func_h6,
                   prices_group_b_products.at[1, 'before'], domestic_market_of_group_b_products.at[1, 'before'],
                   prices_group_b_products.at[5, 'before'], calc_export_customs_duty.at[6, 'before'],
                   prices_group_b_products.at[4, 'before'])

    # I6
    prices_group_b_products.at[3, 'after'] = prices_group_b_products.at[3, 'before']

    # I13
    def func_i13(df, I3, I7, I11, I12):
        I13 = (I3 * I7 - I11) * I12
        return max(0, I13)

    calc_export_customs_duty.at[2, 'after'] = calc_export_customs_duty['after'].pipe(func_i13,
                 prices_group_b_products.at[0, 'after'], prices_group_b_products.at[4, 'after'],
                 calc_export_customs_duty.at[0, 'after'], calc_export_customs_duty.at[1, 'after'])

    # H14
    def func_h14(df, H13, H3, H7):
        return H13 / (H3 * H7)

    calc_export_customs_duty.at[3, 'before'] = calc_export_customs_duty['before'].pipe(func_h14,
                   calc_export_customs_duty.at[2, 'before'], prices_group_b_products.at[0, 'before'],
                   prices_group_b_products.at[4, 'before'])

    # I14
    def func_i14(df, I13, I3, I7):
        return I13 / (I3 * I7)

    calc_export_customs_duty.at[3, 'after'] = calc_export_customs_duty['after'].pipe(func_i14,
                 calc_export_customs_duty.at[2, 'after'], prices_group_b_products.at[0, 'after'],
                 prices_group_b_products.at[4, 'after'])

    # I17
    def func_i17(df, I4, I7, I15, I16):
        I17 = (I4 * I7 - I15) * I16
        return max(0, I17)

    calc_export_customs_duty.at[6, 'after'] = calc_export_customs_duty['after'].pipe(func_i17,
                prices_group_b_products.at[1, 'after'], prices_group_b_products.at[4, 'after'],
                calc_export_customs_duty.at[4, 'after'], calc_export_customs_duty.at[5, 'after'])

    # H18
    def func_h18(df, H17, H4, H7):
        return H17 / (H4 * H7)

    calc_export_customs_duty.at[7, 'before'] = calc_export_customs_duty['before'].pipe(func_h18,
               calc_export_customs_duty.at[6, 'before'], prices_group_b_products.at[1, 'before'],
               prices_group_b_products.at[4, 'before'])

    # I18
    def func_i18(df, I17, I4, I7):
        return I17 / (I4 * I7)

    calc_export_customs_duty.at[7, 'after'] = calc_export_customs_duty['after'].pipe(func_i18,
             calc_export_customs_duty.at[6, 'after'], prices_group_b_products.at[1, 'after'],
             prices_group_b_products.at[4, 'after'])
    
    # I21
    def func_i21(df, I3, I5, I7, I13, I8):
        return ((I3 - I5) * I7 - I13) * (1 - I8)

    domestic_market_of_group_b_products.at[0, 'after'] = domestic_market_of_group_b_products['after'].pipe(func_i21,
           prices_group_b_products.at[0, 'after'], prices_group_b_products.at[2, 'after'],
           prices_group_b_products.at[4, 'after'],calc_export_customs_duty.at[2, 'after'],
           prices_group_b_products.at[5, 'after'])

    # I22
    def func_i22(df, I4, I6, I7, I17, I8):
        return ((I4 - I6) * I7 - I17) * (1 - I8)

    domestic_market_of_group_b_products.at[1, 'after'] = domestic_market_of_group_b_products['after'].pipe(func_i22,
           prices_group_b_products.at[1, 'after'], prices_group_b_products.at[3, 'after'],
           prices_group_b_products.at[4, 'after'], calc_export_customs_duty.at[6, 'after'],
           prices_group_b_products.at[5, 'after'])

    # H25
    def func_h25(df, H21, B16, H22, B17):
        return H21 * B16 + H22 * B17

    internal_market_of_product_a.at[0, 'before'] = internal_market_of_product_a['before'].pipe(func_h25,
           domestic_market_of_group_b_products.at[0, 'before'],
           output_coefficients.loc['T_A_to_B1', 'Коэффициенты выхода продукции'],
           domestic_market_of_group_b_products.at[1, 'before'],
           output_coefficients.loc['T_A_to_B2', 'Коэффициенты выхода продукции'])

    # I25
    def func_i25(df, I21, B16, I22, B17):
        return I21 * B16 + I22 * B17

    internal_market_of_product_a.at[0, 'after'] = internal_market_of_product_a['after'].pipe(func_i25,
             domestic_market_of_group_b_products.at[0, 'after'],
             output_coefficients.loc['T_A_to_B1', 'Коэффициенты выхода продукции'],
             domestic_market_of_group_b_products.at[1, 'after'],
             output_coefficients.loc['T_A_to_B2', 'Коэффициенты выхода продукции'])

    # H26
    def func_h26(df, H25, H27):
        return H25 - H27

    internal_market_of_product_a.at[1, 'before'] = internal_market_of_product_a['before'].pipe(func_h26,
           internal_market_of_product_a.at[0, 'before'],
           internal_market_of_product_a.at[2, 'before'])

    # I26
    internal_market_of_product_a.at[1, 'after'] = internal_market_of_product_a.at[1, 'before']

    # I27
    def func_i27(df, I25, I26):
        return I25 - I26

    internal_market_of_product_a.at[2, 'after'] = internal_market_of_product_a['after'].pipe(func_i27,
             internal_market_of_product_a.at[0, 'after'], internal_market_of_product_a.at[1, 'after'])

    # H34
    def func_h34(df, H30, H33, H27, H32, B8):
        return H30 / (1 + H33) / (H27 / H32) ** B8

    int_prod_balance_of_goods_a.at[4, 'before'] = int_prod_balance_of_goods_a['before'].pipe(func_h34,
             int_prod_balance_of_goods_a.at[0, 'before'], int_prod_balance_of_goods_a.at[3, 'before'],
             internal_market_of_product_a.at[2, 'before'], int_prod_balance_of_goods_a.at[2, 'before'],
             elasticity_at_its_own_price.loc['e_SI_A', 'Эластичности по собственной цене'])

    # I30
    def func_i30(df, H34, I33, I27, I32, B8):
        return H34 * (1 + I33) * (I27 / I32) ** B8

    int_prod_balance_of_goods_a.at[0, 'after'] = int_prod_balance_of_goods_a['after'].pipe(func_i30,
            int_prod_balance_of_goods_a.at[4, 'before'], int_prod_balance_of_goods_a.at[3, 'after'],
            internal_market_of_product_a.at[2, 'after'], int_prod_balance_of_goods_a.at[2, 'after'],
            elasticity_at_its_own_price.loc['e_SI_A', 'Эластичности по собственной цене'])

    # H38
    def func_h38(df, H37, H21):
        return H37 - H21

    int_prod_of_goods_c.at[1, 'before'] = int_prod_of_goods_c['before'].pipe(func_h38,
             int_prod_of_goods_c.at[0, 'before'], domestic_market_of_group_b_products.at[0, 'before'])

    # I38
    int_prod_of_goods_c.at[1, 'after'] = int_prod_of_goods_c.at[1, 'before']

    # I37
    def func_i37(df, I21, I38):
        return I21 + I38

    int_prod_of_goods_c.at[0, 'after'] = int_prod_of_goods_c['after'].pipe(func_i37,
            domestic_market_of_group_b_products.at[0, 'after'], int_prod_of_goods_c.at[1, 'after'])

    # H40
    def func_h40(df, H39, H37, B9):
        return H39 / (H37 ** B9)

    int_prod_of_goods_c.at[3, 'before'] = int_prod_of_goods_c['before'].pipe(func_h40,
             int_prod_of_goods_c.at[2, 'before'], int_prod_of_goods_c.at[0, 'before'],
             elasticity_at_its_own_price.loc['e_DI_C', 'Эластичности по собственной цене'])

    # I39
    def func_i39(df, H40, I37, B9):
        return H40 * (I37) ** B9

    int_prod_of_goods_c.at[2, 'after'] = int_prod_of_goods_c['after'].pipe(func_i39,
           int_prod_of_goods_c.at[3, 'before'], int_prod_of_goods_c.at[0, 'after'],
           elasticity_at_its_own_price.loc['e_DI_C', 'Эластичности по собственной цене'])

    # H43
    def func_h43(df, H30, H31, B16):
        return (H30 - H31) * B16

    prod_bal_of_group_b_goods.at[0, 'before'] = prod_bal_of_group_b_goods['before'].pipe(func_h43,
             int_prod_balance_of_goods_a.at[0, 'before'], int_prod_balance_of_goods_a.at[1, 'before'],
             output_coefficients.loc['T_A_to_B1', 'Коэффициенты выхода продукции'])

    # I43
    def func_i43(df, I30, I31, B16):
        return (I30 - I31) * B16

    prod_bal_of_group_b_goods.at[0, 'after'] = prod_bal_of_group_b_goods['after'].pipe(func_i43,
           int_prod_balance_of_goods_a.at[0, 'after'], int_prod_balance_of_goods_a.at[1, 'after'],
           output_coefficients.loc['T_A_to_B1', 'Коэффициенты выхода продукции'])

    # H44
    prod_bal_of_group_b_goods.at[1, 'before'] = int_prod_of_goods_c.at[2, 'before']

    # I44
    prod_bal_of_group_b_goods.at[1, 'after'] = int_prod_of_goods_c.at[2, 'after']

    # H45
    def func_h45(df, H43, H44):
        return H43 - H44

    prod_bal_of_group_b_goods.at[2, 'before'] = prod_bal_of_group_b_goods['before'].pipe(func_h45,
             prod_bal_of_group_b_goods.at[0, 'before'], prod_bal_of_group_b_goods.at[1, 'before'])


    # I45
    def func_i45(df, I43, I44):
        return I43 - I44

    prod_bal_of_group_b_goods.at[2, 'after'] = prod_bal_of_group_b_goods['after'].pipe(func_i45,
           prod_bal_of_group_b_goods.at[0, 'after'], prod_bal_of_group_b_goods.at[1, 'after'])

    # H46
    def func_h46(df, H30, H31, B17):
        return (H30 - H31) * B17

    prod_bal_of_group_b_goods.at[3, 'before'] = prod_bal_of_group_b_goods['before'].pipe(func_h46,
             int_prod_balance_of_goods_a.at[0, 'before'], int_prod_balance_of_goods_a.at[1, 'before'],
             output_coefficients.loc['T_A_to_B2', 'Коэффициенты выхода продукции'])

    # I46
    def func_i46(df, I30, I31, B17):
        return (I30 - I31) * B17

    prod_bal_of_group_b_goods.at[3, 'after'] = prod_bal_of_group_b_goods['after'].pipe(func_i46,
           int_prod_balance_of_goods_a.at[0, 'after'], int_prod_balance_of_goods_a.at[1, 'after'],
           output_coefficients.loc['T_A_to_B2', 'Коэффициенты выхода продукции'])

    # I47
    def func_i47(df, H47, I22, H22, B9):
        return H47*(I22/H22)**B9

    prod_bal_of_group_b_goods.at[4, 'after'] = prod_bal_of_group_b_goods['after'].pipe(func_i47,
                                          prod_bal_of_group_b_goods.at[4, 'before'],
                                          domestic_market_of_group_b_products.at[1, 'after'],
                                          domestic_market_of_group_b_products.at[1, 'before'],
                                          elasticity_at_its_own_price.loc['e_DI_C', 'Эластичности по собственной цене'])

    # H48
    def func_h48(df, H46, H47):
        return H46 - H47

    prod_bal_of_group_b_goods.at[5, 'before'] = prod_bal_of_group_b_goods['before'].pipe(func_h48,
             prod_bal_of_group_b_goods.at[3, 'before'], prod_bal_of_group_b_goods.at[4, 'before'])


    # I48
    def func_i48(df, I46, I47):
        return I46 - I47

    prod_bal_of_group_b_goods.at[5, 'after'] = prod_bal_of_group_b_goods['after'].pipe(func_i48,
           prod_bal_of_group_b_goods.at[3, 'after'], prod_bal_of_group_b_goods.at[4, 'after'])

    # N4
    prices.at[0, 'before'] = internal_market_of_product_a.at[2, 'before']
    # O4
    prices.at[0, 'after'] = internal_market_of_product_a.at[2, 'after']
    # P4
    prices.at[0, 'increment'] = prices.at[0, 'after'] - prices.at[0, 'before']
    # Q4
    prices.at[0, 'increment_pr'] = prices.at[0, 'after'] / prices.at[0, 'before'] - 1

    # N5
    prices.at[1, 'before'] = domestic_market_of_group_b_products.at[0, 'before']
    # O5
    prices.at[1, 'after'] = domestic_market_of_group_b_products.at[0, 'after']
    # P5
    prices.at[1, 'increment'] = prices.at[1, 'after'] - prices.at[1, 'before']
    # Q5
    prices.at[1, 'increment_pr'] = prices.at[1, 'after'] / prices.at[1, 'before'] - 1

    # N6
    prices.at[2, 'before'] = domestic_market_of_group_b_products.at[1, 'before']
    # O6
    prices.at[2, 'after'] = domestic_market_of_group_b_products.at[1, 'after']
    # P6
    prices.at[2, 'increment'] = prices.at[2, 'after'] - prices.at[2, 'before']
    # Q6
    prices.at[2, 'increment_pr'] = prices.at[2, 'after'] / prices.at[2, 'before'] - 1

    # N7
    prices.at[3, 'before'] = int_prod_of_goods_c.at[0, 'before']
    # O7
    prices.at[3, 'after'] = int_prod_of_goods_c.at[0, 'after']
    # P7
    prices.at[3, 'increment'] = prices.at[3, 'after'] - prices.at[3, 'before']
    # Q7
    prices.at[3, 'increment_pr'] = prices.at[3, 'after'] / prices.at[3, 'before'] - 1

    # P8
    prices.at[4, 'increment'] = prices.at[3, 'increment_pr'] * list_of_products.at['C', 'Вклад в ИПЦ'] / 100

    # N11
    production_and_consumption.at[0, 'before'] = int_prod_balance_of_goods_a.at[0, 'before']
    # O11
    production_and_consumption.at[0, 'after'] = int_prod_balance_of_goods_a.at[0, 'after']
    # P11
    production_and_consumption.at[0, 'increment'] = production_and_consumption.at[0, 'after'] - \
                                                    production_and_consumption.at[0, 'before']
    # Q11
    production_and_consumption.at[0, 'increment_pr'] = production_and_consumption.at[0, 'after'] / \
                                                       production_and_consumption.at[0, 'before'] - 1

    # N12
    production_and_consumption.at[1, 'before'] = prod_bal_of_group_b_goods.at[0, 'before']
    # O12
    production_and_consumption.at[1, 'after'] = prod_bal_of_group_b_goods.at[0, 'after']
    # P12
    production_and_consumption.at[1, 'increment'] = production_and_consumption.at[1, 'after'] - \
                                                    production_and_consumption.at[1, 'before']
    # Q12
    production_and_consumption.at[1, 'increment_pr'] = production_and_consumption.at[1, 'after'] / \
                                                       production_and_consumption.at[1, 'before'] - 1

    # N13
    production_and_consumption.at[2, 'before'] = prod_bal_of_group_b_goods.at[1, 'before']
    # O13
    production_and_consumption.at[2, 'after'] = prod_bal_of_group_b_goods.at[1, 'after']
    # P13
    production_and_consumption.at[2, 'increment'] = production_and_consumption.at[2, 'after'] - \
                                                    production_and_consumption.at[2, 'before']
    # Q13
    production_and_consumption.at[2, 'increment_pr'] = production_and_consumption.at[2, 'after'] / \
                                                       production_and_consumption.at[2, 'before'] - 1

    # N14
    production_and_consumption.at[3, 'before'] = prod_bal_of_group_b_goods.at[2, 'before']
    # O14
    production_and_consumption.at[3, 'after'] = prod_bal_of_group_b_goods.at[2, 'after']
    # P14
    production_and_consumption.at[3, 'increment'] = production_and_consumption.at[3, 'after'] - \
                                                    production_and_consumption.at[3, 'before']
    # Q14
    production_and_consumption.at[3, 'increment_pr'] = production_and_consumption.at[3, 'after'] / \
                                                       production_and_consumption.at[3, 'before'] - 1

    # N15
    production_and_consumption.at[4, 'before'] = prod_bal_of_group_b_goods.at[3, 'before']
    # O15
    production_and_consumption.at[4, 'after'] = prod_bal_of_group_b_goods.at[3, 'after']
    # P15
    production_and_consumption.at[4, 'increment'] = production_and_consumption.at[4, 'after'] - \
                                                    production_and_consumption.at[4, 'before']
    # Q15
    production_and_consumption.at[4, 'increment_pr'] = production_and_consumption.at[4, 'after'] / \
                                                       production_and_consumption.at[4, 'before'] - 1

    # N16
    production_and_consumption.at[5, 'before'] = prod_bal_of_group_b_goods.at[4, 'before']
    # O16
    production_and_consumption.at[5, 'after'] = prod_bal_of_group_b_goods.at[4, 'after']
    # P16
    production_and_consumption.at[5, 'increment'] = production_and_consumption.at[5, 'after'] - \
                                                    production_and_consumption.at[5, 'before']
    # Q16
    production_and_consumption.at[5, 'increment_pr'] = production_and_consumption.at[5, 'after'] / \
                                                       production_and_consumption.at[5, 'before'] - 1

    # N17
    production_and_consumption.at[6, 'before'] = prod_bal_of_group_b_goods.at[5, 'before']
    # O17
    production_and_consumption.at[6, 'after'] = prod_bal_of_group_b_goods.at[5, 'after']
    # P17
    production_and_consumption.at[6, 'increment'] = production_and_consumption.at[6, 'after'] - \
                                                    production_and_consumption.at[6, 'before']
    # Q17
    production_and_consumption.at[6, 'increment_pr'] = production_and_consumption.at[6, 'after'] / \
                                                       production_and_consumption.at[6, 'before'] - 1


    # N18
    production_and_consumption.at[7, 'before'] = int_prod_of_goods_c.at[2, 'before']
    # O18
    production_and_consumption.at[7, 'after'] = int_prod_of_goods_c.at[2, 'after']
    # P18
    production_and_consumption.at[7, 'increment'] = production_and_consumption.at[7, 'after'] - \
                                                    production_and_consumption.at[7, 'before']
    # Q18
    production_and_consumption.at[7, 'increment_pr'] = production_and_consumption.at[7, 'after'] / \
                                                       production_and_consumption.at[7, 'before'] - 1

    # N22
    def func_n22(df, H45, H3, H48, H4, H7):
        return (H45 * H3 + H48 * H4) * H7

    cost_effects.at[0, 'before'] = cost_effects['before'].pipe(func_n22, prod_bal_of_group_b_goods.at[2, 'before'],
                                                               prices_group_b_products.at[0, 'before'],
                                                               prod_bal_of_group_b_goods.at[5, 'before'],
                                                               prices_group_b_products.at[1, 'before'],
                                                               prices_group_b_products.at[4, 'before'])
    # O22
    def func_o22(df, I45, I3, I48, I4, I7):
        return (I45 * I3 + I48 * I4) * I7

    cost_effects.at[0, 'after'] = cost_effects['after'].pipe(func_o22, prod_bal_of_group_b_goods.at[2, 'after'],
                                                             prices_group_b_products.at[0, 'after'],
                                                             prod_bal_of_group_b_goods.at[5, 'after'],
                                                             prices_group_b_products.at[1, 'after'],
                                                             prices_group_b_products.at[4, 'after'])

    # P22
    cost_effects.at[0, 'increment'] = cost_effects.at[0, 'after'] - cost_effects.at[0, 'before']
    # Q22
    cost_effects.at[0, 'increment_pr'] = cost_effects.at[0, 'after'] / cost_effects.at[0, 'before'] - 1

    # N23
    def func_n23(df, H13, H45, H17, H48):
        return H13 * H45 + H17 * H48

    cost_effects.at[1, 'before'] = cost_effects['before'].pipe(func_n23, calc_export_customs_duty.at[2, 'before'],
                                                               prod_bal_of_group_b_goods.at[2, 'before'],
                                                               calc_export_customs_duty.at[6, 'before'],
                                                               prod_bal_of_group_b_goods.at[5, 'before'])
    # O23
    def func_o23(df, I13, I45, I17, I48):
        return I13 * I45 + I17 * I48

    cost_effects.at[1, 'after'] = cost_effects['after'].pipe(func_o23, calc_export_customs_duty.at[2, 'after'],
                                                             prod_bal_of_group_b_goods.at[2, 'after'],
                                                             calc_export_customs_duty.at[6, 'after'],
                                                             prod_bal_of_group_b_goods.at[5, 'after'])
    # P23
    cost_effects.at[1, 'increment'] = cost_effects.at[1, 'after'] - cost_effects.at[1, 'before']

    # Q23
    def func_q23(df, O23, N23):
        try:
            Q23 = O23 / N23 - 1
        except ZeroDivisionError:
            Q23 = '-'
        else:
            Q23 = '-'
        return Q23
    cost_effects.at[1, 'increment_pr'] = cost_effects['increment_pr'].pipe(func_q23, cost_effects.at[1, 'after'],
                                                                           cost_effects.at[1, 'before'])


    # N26
    def func_n26(df, N11, N4, O4, O11):
        return -(N11 * (N4 - O4) - 0.5 * (N4 - O4) * (N11 - O11))

    cost_effects.at[4, 'before'] = cost_effects['before'].pipe(func_n26, production_and_consumption.at[0, 'before'],
                                                               prices.at[0, 'before'], prices.at[0, 'after'],
                                                               production_and_consumption.at[0, 'after'])
    # N28
    def func_n28(df, N5, O5, N13, O13):
        return (N5 - O5) * N13 + 0.5 * (N5 - O5) * (O13 - N13)

    cost_effects.at[6, 'before'] = cost_effects['before'].pipe(func_n28, prices.at[1, 'before'],
                                                               prices.at[1, 'after'],
                                                               production_and_consumption.at[2, 'before'],
                                                               production_and_consumption.at[2, 'after'])
    # N29
    def func_n29(df, N6, O6, N16, O16):
        return (N6 - O6) * N16 + 0.5 * (N6 - O6) * (O16 - N16)

    cost_effects.at[7, 'before'] = cost_effects['before'].pipe(func_n29, prices.at[2, 'before'],
                                                               prices.at[2, 'after'],
                                                               production_and_consumption.at[5, 'before'],
                                                               production_and_consumption.at[5, 'after'])
    # N27
    def func_n27(df, N28, N29):
        return N28 + N29

    cost_effects.at[5, 'before'] = cost_effects['before'].pipe(func_n27, cost_effects.at[6, 'before'],
                                                               cost_effects.at[7, 'before'])
    
    # N30
    def func_n30(df, N26, N27, P23):
        return N26 + N27 + P23

    cost_effects.at[8, 'before'] = cost_effects['before'].pipe(func_n30, cost_effects.at[4, 'before'],
                                                               cost_effects.at[5, 'before'],
                                                               cost_effects.at[1, 'increment'])

    # N33
    def func_n33(df, N11, O4, N4, O11):
        return N11 * (O4 - N4) + 0.5 * (O4 - N4) * (O11 - N11)

    cost_effects.at[11, 'before'] = cost_effects['before'].pipe(func_n33, production_and_consumption.at[0, 'before'],
                                                                prices.at[0, 'after'], prices.at[0, 'before'],
                                                                production_and_consumption.at[0, 'after'])

    # N34
    def func_n34(df, N4, O11, N11, O4):
        return N4 * (O11 - N11) + 0.5 * (O4 - N4) * (O11 - N11)

    cost_effects.at[12, 'before'] = cost_effects['before'].pipe(func_n34, prices.at[0, 'before'],
                                                                production_and_consumption.at[0, 'after'],
                                                                production_and_consumption.at[0, 'before'],
                                                                prices.at[0, 'after'])

    # N32
    def func_n32(df, N33, N34):
        return N33 + N34

    cost_effects.at[10, 'before'] = cost_effects['before'].pipe(func_n32, cost_effects.at[11, 'before'],
                                                                cost_effects.at[12, 'before'])

    # N37
    def func_n37(df, N12, O5, N5, O12):
        return N12 * (O5 - N5) + 0.5 * (O5 - N5) * (O12 - N12)

    cost_effects.at[15, 'before'] = cost_effects['before'].pipe(func_n37, production_and_consumption.at[1, 'before'],
                                                                prices.at[1, 'after'], prices.at[1, 'before'],
                                                                production_and_consumption.at[1, 'after'])

    # N38
    def func_n38(df, N5, O15, N15, O5):
        return N5 * (O15 - N15) + 0.5 * (O5 - N5) * (O15 - N15)

    cost_effects.at[16, 'before'] = cost_effects['before'].pipe(func_n38, prices.at[1, 'before'],
                                                                production_and_consumption.at[4, 'after'],
                                                                production_and_consumption.at[4, 'before'],
                                                                prices.at[1, 'after'])

    # N36
    def func_n36(df, N37, N38):
        return N37 + N38

    cost_effects.at[14, 'before'] = cost_effects['before'].pipe(func_n36, cost_effects.at[15, 'before'],
                                                                cost_effects.at[16, 'before'])

    # N41
    def func_n41(df, N13, O5, N5, O13):
        return N13 * (O5 - N5) + 0.5 * (O5 - N5) * (O13 - N13)

    cost_effects.at[19, 'before'] = cost_effects['before'].pipe(func_n41, production_and_consumption.at[2, 'before'],
                                                                prices.at[1, 'after'], prices.at[1, 'before'],
                                                                production_and_consumption.at[2, 'after'])

    # N42
    def func_n42(df, N5, O13, N13, O5):
        return N5 * (O13 - N13) + 0.5 * (O13 - N13) * (O5 - N5)

    cost_effects.at[20, 'before'] = cost_effects['before'].pipe(func_n42, prices.at[1, 'before'],
                                                                production_and_consumption.at[2, 'after'],
                                                                production_and_consumption.at[2, 'before'],
                                                                prices.at[1, 'after'])
    # N40
    def func_n40(df, N41, N42):
        return N41 + N42

    cost_effects.at[18, 'before'] = cost_effects['before'].pipe(func_n40, cost_effects.at[19, 'before'],
                                                                cost_effects.at[20, 'before'])

    # N45
    def func_n45(df, N15, O6, N6, O15):
        return N15 * (O6 - N6) + 0.5 * (O6 - N6) * (O15 - N15)

    cost_effects.at[23, 'before'] = cost_effects['before'].pipe(func_n45, production_and_consumption.at[4, 'before'],
                                                                prices.at[2, 'after'], prices.at[2, 'before'],
                                                                production_and_consumption.at[4, 'after'])

    # N46
    def func_n46(df, N6, O15, N15, O6):
        return N6 * (O15 - N15) + 0.5 * (O6 - N6) * (O15 - N15)

    cost_effects.at[24, 'before'] = cost_effects['before'].pipe(func_n46, prices.at[2, 'before'],
                                                                production_and_consumption.at[4, 'after'],
                                                                production_and_consumption.at[4, 'before'],
                                                                prices.at[2, 'after'])

    # N44
    def func_n44(df, N45, N46):
        return N45 + N46

    cost_effects.at[22, 'before'] = cost_effects['before'].pipe(func_n44, cost_effects.at[23, 'before'],
                                                                cost_effects.at[24, 'before'])

    # N49
    def func_n49(df, N16, O6, N6, O16):
        return N16 * (O6 - N6) + 0.5 * (O6 - N6) * (O16 - N16)

    cost_effects.at[27, 'before'] = cost_effects['before'].pipe(func_n49, production_and_consumption.at[5, 'before'],
                                                                prices.at[2, 'after'], prices.at[2, 'before'],
                                                                production_and_consumption.at[5, 'after'])

    # N50
    def func_n50(df, N6, O16, N16, O6):
        return N6 * (O16 - N16) + 0.5 * (O16 - N16) * (O6 - N6)

    cost_effects.at[28, 'before'] = cost_effects['before'].pipe(func_n50, prices.at[2, 'before'],
                                                                production_and_consumption.at[5, 'after'],
                                                                production_and_consumption.at[5, 'before'],
                                                                prices.at[2, 'after'])

    # N48
    def func_n48(df, N49, N50):
        return N49 + N50

    cost_effects.at[26, 'before'] = cost_effects['before'].pipe(func_n48, cost_effects.at[27, 'before'],
                                                                cost_effects.at[28, 'before'])

    # N53
    def func_n53(df, N18, O7, N7, O18):
        return N18 * (O7 - N7) + 0.5 * (O7 - N7) * (O18 - N18)

    cost_effects.at[31, 'before'] = cost_effects['before'].pipe(func_n53, production_and_consumption.at[7, 'before'],
                                                                prices.at[3, 'after'], prices.at[3, 'before'],
                                                                production_and_consumption.at[7, 'after'])

    # N54
    def func_n54(df, N7, O18, N18, O7):
        return N7 * (O18 - N18) + 0.5 * (O7 - N7) * (O18 - N18)

    cost_effects.at[32, 'before'] = cost_effects['before'].pipe(func_n54, prices.at[3, 'before'],
                                                                production_and_consumption.at[7, 'after'],
                                                                production_and_consumption.at[7, 'before'],
                                                                prices.at[3, 'after'])

    # N52
    def func_n52(df, N53, N54):
        return N53 + N54

    cost_effects.at[30, 'before'] = cost_effects['before'].pipe(func_n52, cost_effects.at[31, 'before'],
                                                                cost_effects.at[32, 'before'])

    # N57
    def func_n57(df, N18, O7, N7, O18):
        return N18 * (O7 - N7) + 0.5 * (O7 - N7) * (O18 - N18)

    cost_effects.at[35, 'before'] = cost_effects['before'].pipe(func_n57, production_and_consumption.at[7, 'before'],
                                                                prices.at[3, 'after'], prices.at[3, 'before'],
                                                                production_and_consumption.at[7, 'after'])

    # N58
    def func_n58(df, N7, O18, N18, O7):
        return N7 * (O18 - N18) + 0.5 * (O18 - N18) * (O7 - N7)

    cost_effects.at[36, 'before'] = cost_effects['before'].pipe(func_n58, prices.at[3, 'before'],
                                                                production_and_consumption.at[7, 'after'],
                                                                production_and_consumption.at[7, 'before'],
                                                                prices.at[3, 'after'])

    # N56
    def func_n56(df, N57, N58):
        return N57 + N58

    cost_effects.at[34, 'before'] = cost_effects['before'].pipe(func_n56, cost_effects.at[35, 'before'],
                                                                cost_effects.at[36, 'before'])

    result_to_front = {
        'table1': [
            {
                'id': '1',
                'title': 'Мировая цена товара B1',
                'measure': 'долл США',
                'params': 'PW_B1',
                'basebalance': prices_group_b_products.at[0, 'before'],
                'newbalance': prices_group_b_products.at[0, 'after']
            },
            {
                'id': '2',
                'title': 'Мировая цена товара B2',
                'measure': 'долл США',
                'params': 'PW_B2',
                'basebalance': prices_group_b_products.at[1, 'before'],
                'newbalance': prices_group_b_products.at[1, 'after']
            },
            {
                'id': '3',
                'title': 'Стоимость услуг трейдеров товара B1',
                'measure': 'долл США',
                'params': 'CT_B1',
                'basebalance': prices_group_b_products.at[2, 'before'],
                'newbalance': prices_group_b_products.at[2, 'after']
            },
            {
                'id': '4',
                'title': 'Стоимость услуг трейдеров товара B2',
                'measure': 'долл США',
                'params': 'CT_B2',
                'basebalance': prices_group_b_products.at[3, 'before'],
                'newbalance': prices_group_b_products.at[3, 'after']
            },
            {
                'id': '5',
                'title': 'Обменный курс',
                'measure': 'руб/долл США',
                'params': 'ER',
                'basebalance': prices_group_b_products.at[4, 'before'],
                'newbalance': prices_group_b_products.at[4, 'after']
            },
            {
                'id': '6',
                'title': 'Дисконт к эквивалентной цене',
                'measure': '',
                'params': 'TD',
                'basebalance': prices_group_b_products.at[5, 'before'],
                'newbalance': prices_group_b_products.at[5, 'after']
            }
        ],
        'table2': [
            {
                'id': '1',
                'title': 'Базовая цена товара B1',
                'measure': 'руб/т',
                'params': 'Pb_B1',
                'basebalance': calc_export_customs_duty.at[0, 'before'],
                'newbalance': calc_export_customs_duty.at[0, 'after']
            },
            {
                'id': '2',
                'title': 'Ставка вывозной пошлины товара B1',
                'measure': '',
                'params': 'tb_B1',
                'basebalance': calc_export_customs_duty.at[1, 'before'],
                'newbalance': calc_export_customs_duty.at[1, 'after']
            },
            {
                'id': '3',
                'title': 'Вывозная таможенная пошлина на товар B1',
                'measure': 'руб/т',
                'params': 'tax_B1',
                'basebalance': calc_export_customs_duty.at[2, 'before'],
                'newbalance': calc_export_customs_duty.at[2, 'after']
            },
            {
                'id': '4',
                'title': 'Адвалорная ставка пошлины на товар B1',
                'measure': '',
                'params': 't_B1',
                'basebalance': calc_export_customs_duty.at[3, 'before'],
                'newbalance': calc_export_customs_duty.at[3, 'after']
            },
            {
                'id': '5',
                'title': 'Базовая цена товара B2',
                'measure': 'руб/т',
                'params': 'Pb_B2',
                'basebalance': calc_export_customs_duty.at[4, 'before'],
                'newbalance': calc_export_customs_duty.at[4, 'after']
            },
            {
                'id': '6',
                'title': 'Ставка вывозной пошлины товара B2',
                'measure': '',
                'params': 'tb_B2',
                'basebalance': calc_export_customs_duty.at[5, 'before'],
                'newbalance': calc_export_customs_duty.at[5, 'after']
            },
            {
                'id': '7',
                'title': 'Вывозная таможенная пошлина на товар B2',
                'measure': 'руб/т',
                'params': 'tax_B2',
                'basebalance': calc_export_customs_duty.at[6, 'before'],
                'newbalance': calc_export_customs_duty.at[6, 'after']
            },
            {
                'id': '8',
                'title': 'Адвалорная ставка пошлины на товар B2',
                'measure': '',
                'params': 't_B2',
                'basebalance': calc_export_customs_duty.at[7, 'before'],
                'newbalance': calc_export_customs_duty.at[7, 'after']
            }
        ],
        'table3': [
            {
                'id': '1',
                'title': 'Внутренняя цена товара B1',
                'measure': 'руб/т',
                'params': 'PI_B1',
                'basebalance': domestic_market_of_group_b_products.at[0, 'before'],
                'newbalance': domestic_market_of_group_b_products.at[0, 'after']
            },
            {
                'id': '2',
                'title': 'Внутренняя цена товара B2',
                'measure': 'руб/т',
                'params': 'PI_B2',
                'basebalance': domestic_market_of_group_b_products.at[1, 'before'],
                'newbalance': domestic_market_of_group_b_products.at[1, 'after']
            }
        ],
        'table4': [
            {
                'id': '1',
                'title': 'Стоимость продуктов переработки 1 единицы товара А',
                'measure': 'руб/т',
                'params': 'VP_A',
                'basebalance': internal_market_of_product_a.at[0, 'before'],
                'newbalance': internal_market_of_product_a.at[0, 'after']
            },
            {
                'id': '2',
                'title': 'Стоимость переработки 1 единицы товара А',
                'measure': 'руб/т',
                'params': 'VT_A',
                'basebalance': internal_market_of_product_a.at[1, 'before'],
                'newbalance': internal_market_of_product_a.at[1, 'after']
            },
            {
                'id': '3',
                'title': 'Внутренняя цена товара А',
                'measure': 'руб/т',
                'params': 'PI_A',
                'basebalance': internal_market_of_product_a.at[2, 'before'],
                'newbalance': internal_market_of_product_a.at[2, 'after']
            }
        ],
        'table5': [
            {
                'id': '1',
                'title': 'Объем внутреннего производства товара А',
                'measure': 'млн тонн',
                'params': 'QSI_A',
                'basebalance': int_prod_balance_of_goods_a.at[0, 'before'],
                'newbalance': int_prod_balance_of_goods_a.at[0, 'after']
            },
            {
                'id': '2',
                'title': 'Экспорт товара А (экзогенно)',
                'measure': 'млн тонн',
                'params': 'QSW_RUS_A',
                'basebalance': int_prod_balance_of_goods_a.at[1, 'before'],
                'newbalance': int_prod_balance_of_goods_a.at[1, 'after']
            },
            {
                'id': '3',
                'title': 'Индекс превышения затрат на производство над ценами',
                'measure': '',
                'params': 'i_cost',
                'basebalance': int_prod_balance_of_goods_a.at[2, 'before'],
                'newbalance': int_prod_balance_of_goods_a.at[2, 'after']
            },
            {
                'id': '4',
                'title': 'Экзогенный сдвиг во внутреннем предложении товара А',
                'measure': '',
                'params': 'shift_QSI_A',
                'basebalance': int_prod_balance_of_goods_a.at[3, 'before'],
                'newbalance': int_prod_balance_of_goods_a.at[3, 'after']
            },
            {
                'id': '5',
                'title': 'Калибруемый вспомогательный параметр',
                'measure': '',
                'params': 'Z_QSI_A',
                'basebalance': int_prod_balance_of_goods_a.at[4, 'before'],
                'newbalance': int_prod_balance_of_goods_a.at[4, 'after']
            }
        ],
        'table6': [
            {
                'id': '1',
                'title': 'Внутренняя цена товара С',
                'measure': 'руб/т',
                'params': 'PI_С',
                'basebalance': int_prod_of_goods_c.at[0, 'before'],
                'newbalance': int_prod_of_goods_c.at[0, 'after']
            },
            {
                'id': '2',
                'title': 'Затраты на производство и обращение товара С (без учета стоимости В)',
                'measure': 'руб/т',
                'params': 'VT_C',
                'basebalance': int_prod_of_goods_c.at[1, 'before'],
                'newbalance': int_prod_of_goods_c.at[1, 'after']
            },
            {
                'id': '3',
                'title': 'Внутренний спрос на товар С',
                'measure': 'млн тонн',
                'params': 'QDI_С',
                'basebalance': int_prod_of_goods_c.at[2, 'before'],
                'newbalance': int_prod_of_goods_c.at[2, 'after']
            },
            {
                'id': '4',
                'title': 'Калибруемый вспомогательный параметр',
                'measure': '',
                'params': 'Z_QDI_C',
                'basebalance': int_prod_of_goods_c.at[3, 'before'],
                'newbalance': int_prod_of_goods_c.at[3, 'after']
            }
        ],
        'table7': [
            {
                'id': '1',
                'title': 'Объем внутреннего производства товара B1',
                'measure': 'млн тонн',
                'params': 'QSI_B1',
                'basebalance': prod_bal_of_group_b_goods.at[0, 'before'],
                'newbalance': prod_bal_of_group_b_goods.at[0, 'after']
            },
            {
                'id': '2',
                'title': 'Внутренний спрос на товар B1',
                'measure': 'млн тонн',
                'params': 'QDI_B1',
                'basebalance': prod_bal_of_group_b_goods.at[1, 'before'],
                'newbalance': prod_bal_of_group_b_goods.at[1, 'after']
            },
            {
                'id': '3',
                'title': 'Экспорт товара B1',
                'measure': 'млн тонн',
                'params': 'QSW_RUS_B1',
                'basebalance': prod_bal_of_group_b_goods.at[2, 'before'],
                'newbalance': prod_bal_of_group_b_goods.at[2, 'after']
            },
            {
                'id': '4',
                'title': 'Объем внутреннего производства товара B2',
                'measure': 'млн тонн',
                'params': 'QSI_B2',
                'basebalance': prod_bal_of_group_b_goods.at[3, 'before'],
                'newbalance': prod_bal_of_group_b_goods.at[3, 'after']
            },
            {
                'id': '5',
                'title': 'Внутренний спрос на товар B2',
                'measure': 'млн тонн',
                'params': 'QDI_B2',
                'basebalance': prod_bal_of_group_b_goods.at[4, 'before'],
                'newbalance': prod_bal_of_group_b_goods.at[4, 'after']
            },
            {
                'id': '6',
                'title': 'Экспорт товара B2',
                'measure': 'млн тонн',
                'params': 'QSW_RUS_B2',
                'basebalance': prod_bal_of_group_b_goods.at[5, 'before'],
                'newbalance': prod_bal_of_group_b_goods.at[5, 'after']
            }
        ],
        'fintable1': [
            {
                'id': '1',
                'title': 'Внутреняя цена товара А',
                'measure': 'долл США',
                'basebalance': prices.at[0, 'before'],
                'newbalance': prices.at[0, 'after'],
                'growth': prices.at[0, 'increment'],
                'growthpercent': prices.at[0, 'increment_pr']
            },
            {
                'id': '2',
                'title': 'Внутренняя цена товара B1',
                'measure': 'руб/т',
                'basebalance': prices.at[1, 'before'],
                'newbalance': prices.at[1, 'after'],
                'growth': prices.at[1, 'increment'],
                'growthpercent': prices.at[1, 'increment_pr']
            },
            {
                'id': '3',
                'title': 'Внутренняя цена товара B2',
                'measure': 'руб/т',
                'basebalance': prices.at[2, 'before'],
                'newbalance': prices.at[2, 'after'],
                'growth': prices.at[2, 'increment'],
                'growthpercent': prices.at[2, 'increment_pr']
            },
            {
                'id': '4',
                'title': 'Цена товара С',
                'measure': 'руб/т',
                'basebalance': prices.at[3, 'before'],
                'newbalance': prices.at[3, 'after'],
                'growth': prices.at[3, 'increment'],
                'growthpercent': prices.at[3, 'increment_pr']
            },
            {
                'id': '5',
                'title': 'Изменение ИПЦ',
                'measure': 'руб/т',
                'basebalance': prices.at[4, 'before'],
                'newbalance': prices.at[4, 'after'],
                'growth': prices.at[4, 'increment'],
                'growthpercent': prices.at[4, 'increment_pr']
            }
        ],
        'fintable2': [
            {
                'id': '1',
                'title': 'Внутреннее производство товара А',
                'measure': 'млн тонн',
                'basebalance': production_and_consumption.at[0, 'before'],
                'newbalance': production_and_consumption.at[0, 'after'],
                'growth': production_and_consumption.at[0, 'increment'],
                'growthpercent': production_and_consumption.at[0, 'increment_pr']
            },
            {
                'id': '2',
                'title': 'Внутреннее производство товара B1',
                'measure': 'млн тонн',
                'basebalance': production_and_consumption.at[1, 'before'],
                'newbalance': production_and_consumption.at[1, 'after'],
                'growth': production_and_consumption.at[1, 'increment'],
                'growthpercent': production_and_consumption.at[1, 'increment_pr']
            },
            {
                'id': '3',
                'title': 'Внутреннее потребление товара B1',
                'measure': 'млн тонн',
                'basebalance': production_and_consumption.at[2, 'before'],
                'newbalance': production_and_consumption.at[2, 'after'],
                'growth': production_and_consumption.at[2, 'increment'],
                'growthpercent': production_and_consumption.at[2, 'increment_pr']
            },
            {
                'id': '4',
                'title': 'Экспорт товара B1',
                'measure': 'млн тонн',
                'basebalance': production_and_consumption.at[3, 'before'],
                'newbalance': production_and_consumption.at[3, 'after'],
                'growth': production_and_consumption.at[3, 'increment'],
                'growthpercent': production_and_consumption.at[3, 'increment_pr']
            },
            {
                'id': '5',
                'title': 'Внутреннее производство товара B2',
                'measure': 'млн тонн',
                'basebalance': production_and_consumption.at[4, 'before'],
                'newbalance': production_and_consumption.at[4, 'after'],
                'growth': production_and_consumption.at[4, 'increment'],
                'growthpercent': production_and_consumption.at[4, 'increment_pr']
            },
            {
                'id': '6',
                'title': 'Внутреннее потребление товара B2',
                'measure': 'млн тонн',
                'basebalance': production_and_consumption.at[5, 'before'],
                'newbalance': production_and_consumption.at[5, 'after'],
                'growth': production_and_consumption.at[5, 'increment'],
                'growthpercent': production_and_consumption.at[5, 'increment_pr']
            },
            {
                'id': '7',
                'title': 'Экспорт товара B2',
                'measure': 'млн тонн',
                'basebalance': production_and_consumption.at[6, 'before'],
                'newbalance': production_and_consumption.at[6, 'after'],
                'growth': production_and_consumption.at[6, 'increment'],
                'growthpercent': production_and_consumption.at[6, 'increment_pr']
            },
            {
                'id': '8',
                'title': 'Производство/потребление товара С',
                'measure': 'млн тонн',
                'basebalance': production_and_consumption.at[7, 'before'],
                'newbalance': production_and_consumption.at[7, 'after'],
                'growth': production_and_consumption.at[7, 'increment'],
                'growthpercent': production_and_consumption.at[7, 'increment_pr']
            }
        ],
        'fintable3': [
            {
                'id': '1',
                'title': 'Эффект платежного баланса',
                'measure': 'долл США * руб/долл США * млн тонн',
                'basebalance': cost_effects.at[0, 'before'],
                'newbalance': cost_effects.at[0, 'after'],
                'growth': cost_effects.at[0, 'increment'],
                'growthpercent': cost_effects.at[0, 'increment_pr']
            },
            {
                'id': '2',
                'title': 'Эффект таможенных сборов',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[1, 'before'],
                'newbalance': cost_effects.at[1, 'after'],
                'growth': cost_effects.at[1, 'increment'],
                'growthpercent': cost_effects.at[1, 'increment_pr']
            }
        ],
        'fintable4': [
            {
                'id': '1',
                'title': '- излишек производителя товара А',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[4, 'before']
            },
            {
                'id': '2',
                'title': ' - излишек косвенных потребителей товара А',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[5, 'before']
            },
            {
                'id': '3',
                'title': '  - в т.ч. потребителей товара B1/C',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[6, 'before']
            },
            {
                'id': '4',
                'title': ' - в т.ч. потребителей товара B2',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[7, 'before']
            },
            {
                'id': '5',
                'title': 'Эффект экономических потерь',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[8, 'before']
            },
            {
                'id': '6',
                'title': 'Изменение оборота производителей товара А:',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[10, 'before']
            },
            {
                'id': '7',
                'title': '- изменение оборота из-за изменения цен',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[11, 'before']
            },
            {
                'id': '8',
                'title': ' - изменение объема производства',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[12, 'before']
            },
            {
                'id': '9',
                'title': 'Изменение оборота производителей товара B1:',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[14, 'before']
            },
            {
                'id': '10',
                'title': '- изменение оборота из-за изменения цен',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[15, 'before']
            },
            {
                'id': '11',
                'title': '- изменение объема производства',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[16, 'before']
            },
            {
                'id': '12',
                'title': 'Изменение суммы покупок потребителей товара B1:',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[18, 'before']
            },
            {
                'id': '13',
                'title': ' - переплата потребителей из-за изменения цен',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[19, 'before']
            },
            {
                'id': '14',
                'title': '  - изменение объема потребления',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[20, 'before']
            },
            {
                'id': '15',
                'title': 'Изменение оборота производителей товара B2:',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[22, 'before']
            },
            {
                'id': '16',
                'title': ' - изменение оборота из-за изменения цен',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[23, 'before']
            },
            {
                'id': '17',
                'title': ' - изменение объема производства',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[24, 'before']
            },
            {
                'id': '18',
                'title': 'Изменение суммы покупок потребителей товара B2:',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[26, 'before']
            },
            {
                'id': '19',
                'title': ' - переплата потребителей из-за изменения цен',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[27, 'before']
            },
            {
                'id': '20',
                'title': ' - изменение объема потребления',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[28, 'before']
            },
            {
                'id': '21',
                'title': 'Изменение оборота производителей товара C:',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[30, 'before']
            },
            {
                'id': '22',
                'title': '- изменение оборота из-за изменения цен',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[31, 'before']
            },
            {
                'id': '23',
                'title': ' - изменение объема производства',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[32, 'before']
            },
            {
                'id': '24',
                'title': 'Изменение суммы покупок потребителей товара С:',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[34, 'before']
            },
            {
                'id': '25',
                'title': '- переплата потребителей из-за изменения цен',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[35, 'before']
            },
            {
                'id': '26',
                'title': ' - изменение объема потребления',
                'measure': 'руб/т * млн тонн',
                'basebalance': cost_effects.at[36, 'before']
            }
        ]
    }
    print(cost_effects.to_markdown())
    return result_to_front


input_data = InputDataBase(user_data)
result = oil_export(input_data)

